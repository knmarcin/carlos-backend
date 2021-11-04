from django_filters.rest_framework import DjangoFilterBackend
from api.models import History, Employee, Car
from api.serializers import (HistorySerializer,
                             CreateHistorySerializer,
                             WorkerSerializer,
                             CarSerializer,
                             ClosestServicesSerializer)
from rest_framework import generics, filters



class HistoryViewSet(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['repair_log',
                     'date_of_repair',
                     'employee__name',
                     'car__model',
                     'car__make',
                     'car__year',
                     'car__owner',
                     'car__vin_number',
                     'car__registration']
    filter_fields = ['car__id']
    ordering_fields = ['id']


class HistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer


class CreateHistoryView(generics.CreateAPIView):
    queryset = History.objects.all()
    serializer_class = CreateHistorySerializer


class WorkerViewSet(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = WorkerSerializer


class CarViewSet(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
                     'vin_number',
                     'registration',
                     'make',
                     'model',
                     'year',
                     'owner',
                     'owner_phone_number']
    filter_fields = ['vin_number']
    ordering_fields = ['id']


class CarDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class ClosestServicesViewSet(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = ClosestServicesSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['service_date']
