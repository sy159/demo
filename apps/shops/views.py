from rest_framework.viewsets import ModelViewSet

from apps.shops.models import Shop
from apps.shops.serializers import ShopModelSerializer


class ShopModelViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopModelSerializer

    def list(self, request, *args, **kwargs):
        # 普通用户自能看自己创建的shop
        if not request.user.is_staff:
            self.queryset = Shop.objects.filter(creat_user_id=request.user.id)
        return super().list(self, request, *args, **kwargs)
