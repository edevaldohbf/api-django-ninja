from ninja import Schema
from typing import Literal, Optional


class RuralProducerPatchSchema(Schema):
    cpf_or_cnpj: Optional[str] = None
    producer_name: Optional[str] = None
    farm_name: Optional[str] = None
    city: Optional[str] = None
    state: Optional[
        Literal[
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
    ] = None
    total_farm_area: Optional[int] = None
    arable_farm_area: Optional[int] = None
    vegetation_farm_area: Optional[int] = None
    cultivated_crops: Optional[
        list[Literal["soja", "milho", "algodão", "café", "cana de açucar"]]
    ] = None
