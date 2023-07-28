from .models import Massage
from rest_framework import routers, serializers, viewsets


class MassageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Massage
        fields = '__all__'

