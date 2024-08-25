from rural_producers.models import RuralProducers


def create_rural_producer_service(payload):
    payload.cultivated_crops = list(set(payload.cultivated_crops))

    rural_producer = RuralProducers.objects.create(**payload.dict())

    return rural_producer
