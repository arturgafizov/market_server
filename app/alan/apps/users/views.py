import logging
from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from .generators import get_tokens_for_user

User = get_user_model()

logger = logging.getLogger(__name__)


class ViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete')


class UserModelViewSet(ViewSet):
    serializer_class = serializers.UserSerializer
    # parser_classes = (MultiPartParser, JSONParser, )

    def get_queryset(self):
        return User.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(GenericAPIView):
    serializer_class = serializers.LoginSerializer
    permission_classes = []

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['login']
        user = User.objects.get(email=email)
        return (
            Response(get_tokens_for_user(user), status=status.HTTP_200_OK)
        )


class CurrentUserView(APIView):

    def get(self, request):
        user = request.user
        serializer = serializers.CurrentUserSerializers(user)
        return Response(serializer.data)
