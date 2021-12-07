from django_filters.rest_framework import DjangoFilterBackend
from api.models import History, Employee, Car
from api.serializers import (HistorySerializer,
                             CreateHistorySerializer,
                             WorkerSerializer,
                             CarSerializer,
                             ClosestServicesSerializer,
                             DashboardSerializer)
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
import operator




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


class Dashboard(APIView):
    def get(self, request):
        today = datetime.now()
        workers = Employee.objects.all()

        class Obj:
            def __init__(self):
                self.number_of_repairs_total = History.objects.all().count()
                self.number_of_repairs_this_month = History.objects.filter(
                    date_of_repair__year=today.year,
                    date_of_repair__month=today.month).count()

                self.number_of_repairs_this_year = History.objects.filter(
                    date_of_repair__year=today.year).count()

                return_list = []
                for i in workers:
                    return_list.append({"name": i.name, "count": History.objects.filter(employee=i).count()})
                return_list.sort(key=operator.itemgetter("count"), reverse=True)
                self.number_of_repairs_total_by_workers = return_list

                return_list = []
                for i in workers:
                    return_list.append({"name": i.name, "count": History.objects.filter(
                        employee=i).filter(date_of_repair__year=today.year).count()})

                return_list.sort(key=operator.itemgetter("count"), reverse=True)
                self.number_of_repairs_this_year_by_workers = return_list

                return_list = []
                for i in workers:
                    return_list.append({"name": i.name, "count": History.objects.filter(
                        employee=i).filter(date_of_repair__year=today.year,
                                           date_of_repair__month=today.month).count()})

                return_list.sort(key=operator.itemgetter("count"), reverse=True)
                self.number_of_repairs_this_month_by_workers = return_list

                return_list = []
                months_dict = {
                    1: "Styczeń",
                    2: "Luty",
                    3: "Marzec",
                    4: "Kwiecień",
                    5: "Maj",
                    6: "Czerwiec",
                    7: "Lipiec",
                    8: "Sierpień",
                    9: "Wrzesień",
                    10: "Październik",
                    11: "Listopad",
                    12: "Grudzień"
                }


                for i in months_dict.items():
                    return_list.append({i[0]: i[1], "count": History.objects.filter(date_of_repair__year=today.year,
                                                                                    date_of_repair__month=i).count()})
                self.number_of_repairs_this_year_by_month = return_list


        obj = Obj()
        serializer = DashboardSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
