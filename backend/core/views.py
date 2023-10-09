from django.http import JsonResponse
from .models import FinalDb
from rest_framework import pagination
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from haystack.query import SearchQuerySet
from django.db.models import Q
from rest_framework import generics, filters
from haystack.views import FacetedSearchView




class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 500
    page_size_query_param = 'page_size'
    ordering = 'index'

class SuppliersViewSet2(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    lookup_field = 'index'
    pagination_class = PageNumberSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['название', 'цена', 'поставщик', 'окпд2']

    def get_queryset(self):
        queryset = FinalDb.objects.all().order_by('index')
        цена = self.request.query_params.get('price', None)
        поставщик = self.request.query_params.get('supplier', None)
        объем = self.request.query_params.get('volume', None)
        окпд2 = self.request.query_params.get('okpd', None)
        название = self.request.query_params.get('name', None)
        инн = self.request.query_params.get('inn', None)
        огрн = self.request.query_params.get('ogrn', None)

        if цена:
            queryset = queryset.filter(цена__startswith=цена)
        if поставщик:
            queryset = queryset.filter(поставщик__startswith=поставщик)
        if объем:
            queryset = queryset.filter(объем__startswith=объем)
        if окпд2:
            queryset = queryset.filter(окпд2__startswith=окпд2)
        if название:
            queryset = queryset.filter(название__startswith=название)
        if инн:
            queryset = queryset.filter(инн__startswith=инн)
        if огрн:
            queryset = queryset.filter(огрн__startswith=огрн)

        return queryset

class SuppliersViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    lookup_field = 'index'
    pagination_class = PageNumberSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['название', 'цена', 'поставщик']

    def get_queryset(self):
        queryset = FinalDb.objects.all().order_by('index')

        # Фильтрация по цене
        price = self.request.query_params.get('price', None)
        if price is not None:
            queryset = queryset.filter(цена=price)

        # Фильтрация по поставщику
        supplier = self.request.query_params.get('supplier', None)
        if supplier is not None:
            queryset = queryset.filter(поставщик__icontains=supplier)

        return queryset

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = FinalDb.objects.all().order_by('index')

        цена = self.request.query_params.get('price', None)
        поставщик = self.request.query_params.get('supplier', None)
        объем = self.request.query_params.get('volume', None)

        if цена:
            queryset = queryset.filter(price=цена)
        if поставщик:
            queryset = queryset.filter(supplier=поставщик)
        if объем:
            queryset = queryset.filter(volume=объем)

        return queryset

def get_queryset(self):
    """
    Optionally restricts the returned suppliers, by filtering against
    a `q` query parameter in the URL.
    """
    queryset = FinalDb.objects.all().order_by('index')
    query = self.request.query_params.get('q', None)
    if query:
        queryset = queryset.filter(Q(название__icontains=query))
    return queryset

def search(request):
    query = request.GET.get('q', '').strip()
    suggestions = set()

    # Если строка запроса не пуста
    if query:
        # Если запрос не содержит пробелов
        if ' ' not in query:
            results = FinalDb.objects.filter(название__istartswith=query)
            for result in results:
                words = result.название.split()
                for word in words:
                    if word.lower().startswith(query.lower()):
                        suggestions.add(word.lower())

        # Если запрос заканчивается на пробел
        elif ' ' in query:
            results = FinalDb.objects.filter(название__icontains=query)
            for result in results:
                suggestions.add(result.название)

        # Предоставляем только первые 5 предложений
        suggestions = list(suggestions)[:5]

    return JsonResponse({'results': suggestions})

def okpd_search(request):
    query = request.GET.get('q', '').strip()
    suggestions = []

    if query:
        results = FinalDb.objects.filter(окпд2__icontains=query)
        for result in results:
            suggestions.append(result.окпд2)

        # Provide only the first 5 suggestions
        suggestions = suggestions[:5]

    return JsonResponse({'results': suggestions})




