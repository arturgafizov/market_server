from django.shortcuts import render
from rest_framework import status
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import serializers
from .models import Speciality, Category, Document, Information
from . import swagger_schemas as schemas


@method_decorator(name='list', decorator=swagger_auto_schema(**schemas.speciality_list, ))
class SpecialityViewSet(ModelViewSet):
    http_method_names = ('get', 'post', 'put', 'delete', 'patch')
    serializer_class = serializers.SpecialitySerializer

    def get_queryset(self):
        return Speciality.objects.all()

    @method_decorator(name='retrieve', decorator=swagger_auto_schema(**schemas.speciality_retrieve, ))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @method_decorator(name='create', decorator=swagger_auto_schema(**schemas.speciality_create, ))
    def create(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @method_decorator(name='update', decorator=swagger_auto_schema(**schemas.speciality_update, ))
    def update(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @method_decorator(name='partial_update', decorator=swagger_auto_schema(**schemas.speciality_partial_update))
    def partial_update(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @method_decorator(name='destroy', decorator=swagger_auto_schema(**schemas.speciality_destroy, ))
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)