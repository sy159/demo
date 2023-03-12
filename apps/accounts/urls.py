from __future__ import unicode_literals

from django.urls import path
from apps.accounts.views import LoginApiView, LogoutApiView, UserApiView

urlpatterns = [
    path('login/', LoginApiView.as_view(), name="login"),
    path('logout/', LogoutApiView.as_view(), name="logout"),
    path('users/', UserApiView.as_view(), name="users"),
]
