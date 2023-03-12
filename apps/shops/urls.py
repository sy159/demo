from __future__ import unicode_literals

from apps.shops.views import ShopModelViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'shops', ShopModelViewSet, basename="shops")

urlpatterns = [
] + router.urls
