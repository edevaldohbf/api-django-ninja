from django.db import models
from django.contrib.postgres.fields import ArrayField


class RuralProducers(models.Model):
    cpf_or_cnpj = models.CharField(null=False, unique=True)
    producer_name = models.CharField(null=False)
    farm_name = models.CharField(null=False)
    city = models.CharField(null=False)
    state = models.CharField(null=False)
    total_farm_area = models.IntegerField(null=False)  # in Hectares
    arable_farm_area = models.IntegerField(null=False)  # in Hectares
    vegetation_farm_area = models.IntegerField(null=False)  # in Hectares
    cultivated_crops = ArrayField(models.CharField(max_length=15), size=5, default=list)
