from rest_framework.serializers import ModelSerializer
from account.models import Driver, Passenger


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class PassengerSerializer(ModelSerializer):
    class Meta:
        model = Passenger
        feilds = '__all__'
        