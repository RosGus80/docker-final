from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserCreateAPIView

app_name = 'users'

urlpatterns = [
    path('signup/', UserCreateAPIView.as_view(), name='sign_up'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
