from django.shortcuts import get_object_or_404
from rural_producers.models import RuralProducers


def delete_rural_producer_service(rural_producer_id):
    rural_producer = get_object_or_404(RuralProducers, id=rural_producer_id)
    rural_producer.delete()

    return rural_producer
