from .models import UserProfile

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
         model = UserProfile
         fields = ('id',  'email', 'date_of_birth', 'account_type')