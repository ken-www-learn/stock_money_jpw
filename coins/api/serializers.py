from rest_framework import serializers
from coins.models import Coins


class CoinsSerializer(serializers.ModelSerializer):
    """it contains serializers for your api.
      Serializers allow complex data such as querysets and model instances to be
      converted to native Python datatypes that can then be easily rendered into
      JSON, XML or other content types.
    """
    class Meta:
        model = Coins
        fields = '__all__'
