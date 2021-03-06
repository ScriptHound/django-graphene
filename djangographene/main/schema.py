import graphene
from graphene_django.types import DjangoObjectType
from main.models import DummyModel


class DummyType(DjangoObjectType):
    class Meta:
        model = DummyModel


class Query(graphene.ObjectType):
    all_dummies = graphene.List(DummyType)

    def resolve_all_dummies(self, info, **kwargs):
        return DummyModel.objects.all()
