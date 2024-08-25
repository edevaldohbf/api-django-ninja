from ninja import Schema


class FarmsByCropSchema(Schema):
    crop: str
    count: int
    percentage: float
    angle: float
