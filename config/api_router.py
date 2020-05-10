from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from stock_money_jpy.users.api.views import UserViewSet
from coins.api.viewsets import CoinsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("coins", CoinsViewSet)


app_name = "api"
urlpatterns = router.urls
