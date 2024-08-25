from django.contrib import admin
from rural_producers.models import RuralProducers


@admin.register(RuralProducers)
class RuralProducersAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "cpf_or_cnpj",
        "producer_name",
        "farm_name",
        "city",
        "state",
        "total_farm_area",
        "arable_farm_area",
        "vegetation_farm_area",
        "cultivated_crops",
    )
