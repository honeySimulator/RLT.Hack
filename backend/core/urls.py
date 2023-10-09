from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SuppliersViewSet, SuppliersViewSet2, search, okpd_search    # импортировать функцию search

router = DefaultRouter()
router.register('suppliers', SuppliersViewSet, basename='suppliers')
router.register('suppliers2', SuppliersViewSet2, basename='suppliers2')

urlpatterns = [
    path('search/', search, name='search'),
    path('okpd_search/', okpd_search, name='okpd_search'),  # add this path for окпд2 search
    path("", include(router.urls))
]
