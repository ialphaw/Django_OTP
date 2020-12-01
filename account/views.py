from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from account.permissions import IsPassenger, IsDriver
from account.serializers import DriverSerializer, PassengerSerializer


class DriverInfo(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsDriver]
    serializer_class = DriverSerializer

    def get_object(self):
        return self.request.user.driver


class PassengerInfo(RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsPassenger]
    serializer_class = PassengerSerializer

    def get_object(self):
        return self.request.user.passenger