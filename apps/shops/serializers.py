from rest_framework import serializers

from apps.shops.models import Shop


class ShopModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("id", "name", "address", "create_user_name", "created", "updated")
        read_only_fields = ('create_user_name', 'created', 'updated')

    def create(self, validated_data):
        shop = Shop.objects.create(creat_user=self.context['request'].user, **validated_data)
        return shop
