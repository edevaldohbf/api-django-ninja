from ninja import Router, Schema
from rural_producers.models import RuralProducers
from django.db.models import Sum, Count, F, FloatField
from django.db.models.functions import Cast
from dashboard.schemas import (
    CountRuralProducersSchema,
    TotalFarmsAreaSchema,
    FarmsByStateSchema,
    FarmsByCropSchema,
    TotalLandUseSchema,
    ErrorSchema,
)
from rural_producers.services import (
    count_rural_producers_service,
    get_total_farms_area_service,
    count_rural_producers_by_state_service,
)
from dashboard.services import (
    get_farms_by_state_service,
    get_farms_by_crop_service,
    get_total_land_use_service,
)

router = Router()


@router.get(
    "count-rural-producers", response={200: CountRuralProducersSchema, 400: ErrorSchema}
)
def count_rural_producers(request):
    "This method count rural producers for dashboard"

    try:
        return {"total_farms_number": count_rural_producers_service()}

    except Exception as error:
        return 400, {"message": str(error)}


@router.get("total-farms-area", response={200: TotalFarmsAreaSchema, 400: ErrorSchema})
def get_total_farms_area(request):
    "This method sums all farm areas from rural producers for dashboard"

    try:
        return {
            "total_farms_area": get_total_farms_area_service()["total_farm_area__sum"]
        }

    except Exception as error:
        return 400, {"message": str(error)}


@router.get(
    "farms-by-state", response={200: list[FarmsByStateSchema], 400: ErrorSchema}
)
def get_farms_by_state(request):
    "This method divides all farms by states"

    try:
        return get_farms_by_state_service()

    except Exception as error:
        return 400, {"message": str(error)}


@router.get("farms-by-crop", response={200: list[FarmsByCropSchema], 400: ErrorSchema})
def get_farms_by_crop(request):
    "This method divides all farms by crop"

    try:
        return get_farms_by_crop_service()

    except Exception as error:
        return 400, {"message": str(error)}


@router.get(
    "total-land-use", response={200: list[TotalLandUseSchema], 400: ErrorSchema}
)
def get_total_land_use(request):
    "This method calculates the percentage of use by vegetation and plantation"

    try:
        return get_total_land_use_service()

    except Exception as error:
        return 400, {"message": str(error)}
