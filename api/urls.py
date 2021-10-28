from rest_framework import routers
from api.views import HistoryViewSet
from django.urls import path


urlpatterns = [
    path('history/', HistoryViewSet.as_view(), name='history'),
]