from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class GetUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetriveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer