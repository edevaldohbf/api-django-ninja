from ninja import Schema


class TotalLandUseSchema(Schema):
    type: str
    number: int
    percentage: float
    angle: float
