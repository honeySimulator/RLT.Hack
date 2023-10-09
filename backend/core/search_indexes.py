from haystack import indexes
from .models import FinalDb

class SuppliersWithIdsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    название = indexes.CharField(model_attr='название')
    цена = indexes.CharField(model_attr='цена', null=True)
    доставка = indexes.CharField(model_attr='доставка', null=True)
    объем = indexes.CharField(model_attr='объем', null=True)
    поставщик = indexes.CharField(model_attr='поставщик', null=True)
    emails = indexes.CharField(model_attr='emails', null=True)
    phones = indexes.CharField(model_attr='phones', null=True)
    инн = indexes.CharField(model_attr='инн', null=True)
    огрн = indexes.CharField(model_attr='огрн', null=True)
    окпд2 = indexes.CharField(model_attr='окпд2', null=True)

    def get_model(self):
        return FinalDb

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

