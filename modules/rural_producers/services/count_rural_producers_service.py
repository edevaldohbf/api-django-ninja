from django.db.models import Count
from rural_producers.models import RuralProducers


def count_rural_producers_service():
    return RuralProducers.objects.all().count()


def count_rural_producers_by_state_service():
    return RuralProducers.objects.values("state").annotate(count=Count("state"))
