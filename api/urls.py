from api.views import HistoryViewSet, HistoryDetailView, CreateHistoryView, WorkerViewSet, CarViewSet, CarDetailViewSet, ClosestServicesViewSet
from django.urls import path


urlpatterns = [
    path('history/', HistoryViewSet.as_view()),
    path('history/create/', CreateHistoryView.as_view()),
    path('history/<int:pk>/', HistoryDetailView.as_view()),
    path('workers/', WorkerViewSet.as_view()),
    path('cars/', CarViewSet.as_view()),
    path('cars/<int:pk>/', CarDetailViewSet.as_view()),
    path('closest-services/', ClosestServicesViewSet.as_view())
]
