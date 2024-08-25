from ninja import Schema


class FarmsByStateSchema(Schema):
    state: str
    count: int
    percentage: float
    angle: float
