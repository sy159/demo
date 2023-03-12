from rest_framework import serializers

from apps.accounts.models import UserInfo


class UserInfoModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="userid.username")

    class Meta:
        model = UserInfo
        fields = ('username', 'tel', 'faq', 'create_time')
        read_only_fields = ('create_time',)
