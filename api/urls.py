from api.views import HistoryViewSet, HistoryDetailView
from django.urls import path


urlpatterns = [
    path('history/', HistoryViewSet.as_view()),
    path('history/<int:pk>/', HistoryDetailView.as_view()),
]
