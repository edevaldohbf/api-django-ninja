from ninja import Schema
from typing import Literal


class RuralProducerCreateSchema(Schema):
    cpf_or_cnpj: str
    producer_name: str
    farm_name: str
    city: str
    state: Literal[
        "AC",
        "AL",
        "AP",
        "AM",
        "BA",
        "CE",
        "DF",
        "ES",
        "GO",
        "MA",
        "MT",
        "MS",
        "MG",
        "PB",
        "PR",
        "PE",
        "PI",
        "RJ",
        "RN",
        "RS",
        "RO",
        "RR",
        "SC",
        "SP",
        "SE",
        "TO",
    ]
    total_farm_area: int
    arable_farm_area: int
    vegetation_farm_area: int
    cultivated_crops: list[
        Literal["soja", "milho", "algodão", "café", "cana de açucar"]
    ]
