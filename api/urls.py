from api.views import HistoryViewSet, HistoryDetailView, CreateHistoryView
from django.urls import path


urlpatterns = [
    path('history/', HistoryViewSet.as_view()),
    path('history/create/', CreateHistoryView.as_view()),
    path('history/<int:pk>/', HistoryDetailView.as_view()),
]
