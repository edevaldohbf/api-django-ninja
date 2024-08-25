from django.shortcuts import get_object_or_404
from rural_producers.models import RuralProducers


def update_rural_producer_service(rural_producer_id, payload):
    rural_producer = get_object_or_404(RuralProducers, id=rural_producer_id)

    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(rural_producer, attr, value)

    rural_producer.cultivated_crops = list(set(rural_producer.cultivated_crops))

    if (
        rural_producer.total_farm_area
        < rural_producer.arable_farm_area + rural_producer.vegetation_farm_area
    ):
        raise Exception(
            "The sum of the arable and vegetation areas must not be greater than the total area of the farm"
        )

    rural_producer.save()

    return rural_producer
