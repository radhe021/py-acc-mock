from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, CustomerViewSet

app_name = "finapp"

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]