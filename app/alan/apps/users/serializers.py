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


class PreLoginMobileSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=128)

    def save(self, **kwargs):
        phone = self.validated_data['phone']
        user = User.objects.get(phone=phone)
        code = gen_security_code()
        print(code)
        IdentificationCode.objects.create(user=user, code=code)
        smsc = SMSC()
        smsc.send_sms(phone, code, sender="sms")


class LoginMobileSerializer(serializers.Serializer):
    phone = PhoneNumberField()
    code = serializers.IntegerField()

    def validate(self, attrs):
        try:
            ident_code = IdentificationCode.objects.get(user__phone=attrs['phone'], code=attrs['code'])
        except IdentificationCode.DoesNotExist:
            raise serializers.ValidationError({'Error': _("The code is invalid")})
        code_lifetime = ident_code.time_created + timedelta(minutes=20)
        if code_lifetime < now():
            raise serializers.ValidationError({'Error': _("The code is expired")})
        ident_code.active = False
        ident_code.save()
        return ident_code.user


class CurrentUserSerializers(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'middle_name',  'last_name', 'email', 'phone', 'role', 'position', 'division')

