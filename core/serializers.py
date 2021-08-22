from rest_framework import serializers
from rest_framework.serializers import Serializer
from django.utils.translation import gettext_lazy as _

from .models import User, Address


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']
        read_only_fields = ('is_active', 'is_staff', 'is_superuser', 'username', 'email', 'date_joined')


class ChangePasswordSerializer(Serializer):
    old_password = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=30)
    confirmed_password = serializers.CharField(required=True, max_length=30)

    def validate(self, data):
        # add here additional check for password strength if needed
        if not self.context['request'].user.check_password(data.get('old_password')):
            raise serializers.ValidationError({_('old_password'): _('Wrong password.')})

        if data.get('confirmed_password') != data.get('password'):
            raise serializers.ValidationError({_('password'): _('Password must be confirmed correctly.')})

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def create(self, validated_data):
        pass


class AddressSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Address
        fields = '__all__'
