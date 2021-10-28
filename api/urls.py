from rest_framework import routers
from api.views import HistoryViewSet

router = routers.DefaultRouter()
router.register('history', HistoryViewSet, 'history')

urlpatterns = router.urls