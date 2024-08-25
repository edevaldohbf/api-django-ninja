from django.db.models import F, FloatField
from django.db.models.functions import Cast
from rural_producers.services import (
    get_total_farms_vegetation_area_service,
    get_total_farms_arable_area_service,
)


def get_total_land_use_service():
    total_arable_area = get_total_farms_arable_area_service()["arable_farm_area__sum"]

    total_vegetation_area = get_total_farms_vegetation_area_service()[
        "vegetation_farm_area__sum"
    ]

    total_area = total_arable_area + total_vegetation_area

    arable_area = {
        "type": "total_arable_area",
        "number": total_arable_area,
        "percentage": (total_arable_area / total_area) * 100,
        "angle": (total_arable_area / total_area) * 360,
    }

    vegetation_area = {
        "type": "total_vegetation_area",
        "number": total_vegetation_area,
        "percentage": (total_vegetation_area / total_area) * 100,
        "angle": (total_vegetation_area / total_area) * 360,
    }

    return [arable_area, vegetation_area]
