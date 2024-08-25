from ninja import Router
from pycpfcnpj import cpfcnpj
from rural_producers.schemas import (
    ErrorSchema,
    RuralProducerCreateSchema,
    RuralProducerPatchSchema,
    RuralProducerSchema,
)
from rural_producers.services import (
    create_rural_producer_service,
    get_many_rural_producers_service,
    get_by_id_rural_producer_service,
    update_rural_producer_service,
    delete_rural_producer_service,
)

router = Router()


@router.post("", response={200: RuralProducerSchema, 400: ErrorSchema})
def create_rural_producer(request, payload: RuralProducerCreateSchema):
    "This method creates a rural producer"

    try:
        if not cpfcnpj.validate(payload.cpf_or_cnpj):
            return 400, {"message": "CPF or CNPJ invalid"}

        if (
            payload.total_farm_area
            < payload.arable_farm_area + payload.vegetation_farm_area
        ):
            return 400, {
                "message": "The sum of the arable and vegetation areas must not be greater than the total area of the farm"
            }

        rural_producer = create_rural_producer_service(payload)

        return rural_producer

    except Exception as error:
        return 400, {"message": str(error)}


@router.get("", response=list[RuralProducerSchema])
def get_many_rural_producers(request, filters: str = None):
    "This method list rural producers considering the query params inputed"

    try:
        return get_many_rural_producers_service(filters)

    except Exception as error:
        return 400, {"message": str(error)}


@router.get("{rural_producer_id}", response=RuralProducerSchema)
def get_by_id_rural_producer(request, rural_producer_id: int):
    "This method get one rural producer considering the id used on path params"

    try:
        return get_by_id_rural_producer_service(rural_producer_id)

    except Exception as error:
        return 400, {"message": str(error)}


@router.patch(
    "{rural_producer_id}", response={200: RuralProducerSchema, 400: ErrorSchema}
)
def update_rural_producer(
    request, rural_producer_id: int, payload: RuralProducerPatchSchema
):
    "This method updates one rural producer considering the id used on path params"

    try:
        if payload.cpf_or_cnpj and not cpfcnpj.validate(payload.cpf_or_cnpj):
            return 400, {"message": "CPF or CNPJ invalid"}

        return update_rural_producer_service(rural_producer_id, payload)

    except Exception as error:
        return 400, {"message": str(error)}


@router.delete(
    "{rural_producer_id}", response={200: RuralProducerSchema, 400: ErrorSchema}
)
def delete_rural_producer(request, rural_producer_id: int):
    "This method delete one rural producer considering the id used on path params"

    try:
        return delete_rural_producer_service(rural_producer_id)

    except Exception as error:
        return 400, {"message": str(error)}
