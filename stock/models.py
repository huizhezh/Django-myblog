from django.db import models

# Create your models here.

class stock(models.Model):
    seq = models.IntegerField(primary_key=True, db_column='Seq', blank=True, null=False)
    symbol = models.TextField(db_column='Symbol', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    url = models.TextField(db_column='Url', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'stock'