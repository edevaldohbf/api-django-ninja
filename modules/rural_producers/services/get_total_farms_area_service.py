from rural_producers.models import RuralProducers
from django.db.models import Sum


def get_total_farms_area_service():
    return RuralProducers.objects.aggregate(Sum("total_farm_area"))
