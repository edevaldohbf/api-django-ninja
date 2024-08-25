from rural_producers.models import RuralProducers


def get_many_rural_producers_service(filters):
    if filters:
        list_rural_producer = RuralProducers.filter(filters).order_by("producer_name")

    else:
        list_rural_producer = RuralProducers.objects.all().order_by("producer_name")

    return list_rural_producer
