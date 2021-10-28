from django_filters.rest_framework import DjangoFilterBackend
from api.models import History
from api.serializers import HistorySerializer
from rest_framework import generics, filters

class HistoryViewSet(generics.ListAPIView):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields =['repair_log', 'date_of_repair', 'employee__name']

