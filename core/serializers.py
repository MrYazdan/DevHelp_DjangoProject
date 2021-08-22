from django.contrib.auth import password_validation
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .models import User, Address


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password', 'groups', 'user_permissions']
        read_only_fields = ('is_active', 'is_staff', 'is_superuser', 'username', 'email', 'date_joined')


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password1 = serializers.CharField(max_length=128, write_only=True, required=True)
    new_password2 = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(_('Your old password was entered incorrectly. Please enter it again.'))
        return value

    def validate(self, data):
        if data['new_password1'] != data['new_password2']:
            raise serializers.ValidationError({'new_password2': _("The two password fields didn't match.")})
        if data['old_password'] == data['new_password1'] == data['new_password2']:
            raise serializers.ValidationError({'error': _("The new password is the same as your current password.")})
        password_validation.validate_password(data['new_password1'], self.context['request'].user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['new_password1']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user


class AddressSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Address
        fields = '__all__'
