from rest_framework import generics

from users.serializers import SignUpSerializer


# Create your views here.


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = SignUpSerializer

    def perform_create(self, serializer):
        new_user = serializer.save()
        new_user.set_password(new_user.password)
        new_user.save()
