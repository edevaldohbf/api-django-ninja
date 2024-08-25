from rural_producers.models import RuralProducers


def get_rural_producer_by_crop_service(crop):
    return RuralProducers.objects.filter(cultivated_crops__contains=[crop])
