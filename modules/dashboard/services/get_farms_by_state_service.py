from django.db.models import F, FloatField
from django.db.models.functions import Cast
from rural_producers.services import (
    count_rural_producers_service,
    count_rural_producers_by_state_service,
)


def get_farms_by_state_service():
    queryset = count_rural_producers_by_state_service()

    total_items = count_rural_producers_service()

    queryset = queryset.annotate(
        percentage=Cast(F("count"), FloatField()) / total_items * 100,
        angle=Cast(F("count"), FloatField()) / total_items * 360,
    )

    return queryset
