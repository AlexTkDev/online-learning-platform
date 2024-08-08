from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        ref_name = 'UserSerializer'
        fields = '__all__'
