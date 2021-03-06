from django.urls import path
from api.views import (HistoryViewSet,
                       HistoryDetailView,
                       CreateHistoryView,
                       WorkerViewSet,
                       WorkerDetailView,
                       CarViewSet,
                       CarDetailViewSet,
                       ClosestServicesViewSet,
                       Dashboard)


urlpatterns = [
    path('dashboard/', Dashboard.as_view()),
    path('history/', HistoryViewSet.as_view()),
    path('history/create/', CreateHistoryView.as_view()),
    path('history/<int:pk>/', HistoryDetailView.as_view()),
    path('workers/', WorkerViewSet.as_view()),
    path('workers/<int:pk>/', WorkerDetailView.as_view()),
    path('cars/', CarViewSet.as_view()),
    path('cars/<int:pk>/', CarDetailViewSet.as_view()),
    path('closest-services/', ClosestServicesViewSet.as_view()),
]
