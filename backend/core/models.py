from django.db import models



class FinalDb(models.Model):
    index = models.IntegerField(primary_key=True)
    название = models.TextField(blank=True, null=True)
    цена = models.TextField(blank=True, null=True)
    доставка = models.TextField(blank=True, null=True)
    объем = models.TextField(blank=True, null=True)
    поставщик = models.TextField(blank=True, null=True)
    emails = models.TextField(blank=True, null=True)
    phones = models.TextField(blank=True, null=True)
    инн = models.TextField(blank=True, null=True)
    огрн = models.TextField(blank=True, null=True)
    окпд2 = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'final_db'

