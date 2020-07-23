import factory
from . import models


class GroupFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Group

    group_name = 'Backend'


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.User

    first_name = factory.Sequence(lambda n: "Agen %03d" % n)
    group = factory.Subfactory(GroupFactory)