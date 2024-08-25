from rural_producers.models import RuralProducers
from django.db.models import Sum


def get_total_farms_arable_area_service():
    return RuralProducers.objects.aggregate(Sum("arable_farm_area"))
