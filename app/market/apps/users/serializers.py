from datetime import timedelta
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .backends import EmailBackend
from .generators import gen_security_code
from .models import IdentificationCode
from .smsc import SMSC

User = get_user_model()

error_messages = {
    'not_verified': _('Email not verified'),
    'not_active': _('Your account is not active. Please contact Your administrator'),
    'wrong_credentials': _('Entered email or password is incorrect'),
}


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class LoginSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)

    def validate(self, attrs: dict):
        self.user = self.authenticate(login=attrs['login'], password=attrs['password'])
        if self.user is None:
            raise serializers.ValidationError({'Error': _("The credentials is invalid")})
        if not self.user.is_active:
            raise serializers.ValidationError({'Error': _("The user is not active")})
        return attrs

    def authenticate(self, **kwargs):
        back = EmailBackend()
        return back.authenticate(**kwargs)


class CurrentUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'middle_name',  'last_name', 'email', 'phone', 'role', 'position', )

