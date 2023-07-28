from rest_framework import routers
from .views import MassageViewSet

router = routers.DefaultRouter()
router.register(r'all_massages', MassageViewSet)