from django.shortcuts import get_object_or_404
from rural_producers.models import RuralProducers


def get_by_id_rural_producer_service(rural_producer_id):
    return get_object_or_404(RuralProducers, id=rural_producer_id)
