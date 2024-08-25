from django.db.models import F, FloatField
from django.db.models.functions import Cast
from rural_producers.services import (
    get_many_rural_producers_service,
    get_rural_producer_by_crop_service,
)


def get_farms_by_crop_service():
    possible_crops = ["soja", "milho", "algodão", "café", "cana de açucar"]

    results = []
    sum_farms = 0

    for crop in possible_crops:
        queryset = get_rural_producer_by_crop_service(crop)

        count = queryset.count()
        sum_farms = sum_farms + count

        results.append({"crop": crop, "count": count, "percentage": 0, "angle": 0})

    for index, result in enumerate(results):
        results[index]["percentage"] = (results[index]["count"] / sum_farms) * 100
        results[index]["angle"] = (results[index]["count"] / sum_farms) * 360

    return results
