from api.models import History
from api.serializers import HistorySerializer
from rest_framework import viewsets

class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer