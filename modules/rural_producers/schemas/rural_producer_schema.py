from ninja import ModelSchema
from rural_producers.models import RuralProducers


class RuralProducerSchema(ModelSchema):
    class Meta:
        model = RuralProducers
        fields = "__all__"
