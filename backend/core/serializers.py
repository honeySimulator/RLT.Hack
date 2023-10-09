from rest_framework import serializers
from .models import FinalDb

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = FinalDb
        fields = ("index", "название", "цена", "доставка", "объем", "поставщик", "emails", "phones", "инн", "огрн", "окпд2")
        lookup_field = 'row_number'
        extra_kwargs = {
            'url': {'lookup_field': 'row_number'}
        }
