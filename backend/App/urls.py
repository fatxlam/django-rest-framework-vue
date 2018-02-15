from django.urls import include, path
from rest_framework import routers
from .views import AppMessageViewSet

router=routers.DefaultRouter()
router.register(r'AppMessage', AppMessageViewSet)

urlpatterns = router.urls
