from rural_producers.models import RuralProducers
from django.db.models import Sum


def get_total_farms_vegetation_area_service():
    return RuralProducers.objects.aggregate(Sum("vegetation_farm_area"))
