from rest_framework import viewsets
from coins.models import Coins
from coins.api.serializers import CoinsSerializer


class CoinsViewSet(viewsets.ModelViewSet):
    """Django REST framework allows you to combine the logic for a set of related
     views in a single class, called a ViewSet.
     In other frameworks you may also find conceptually similar implementations
     named something like 'Resources' or 'Controllers'.
     """
    queryset = Coins.objects.all()
    serializer_class = CoinsSerializer
