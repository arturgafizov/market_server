from django.core.validators import FileExtensionValidator
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


from . models import Category, Speciality, Document, Information


class SpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Speciality
        fields = ('name', )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'code')


class DocumentSerializer(serializers.ModelSerializer):
    speciality = serializers.CharField(source='speciality.name')
    category = serializers.CharField(source='category.name')
    file = serializers.FileField(validators=[FileExtensionValidator(['xls', 'xlsx', 'doc', 'docs', 'pdf'])])

    class Meta:
        model = Document
        fields = ('name', 'file', 'speciality', 'category')


class InformationSerializer(serializers.ModelSerializer):
    file = serializers.FileField(validators=[FileExtensionValidator(['xls', 'xlsx', 'doc', 'docs', 'pdf'])])

    class Meta:
        model = Information
        fields = ('created_at', 'name', 'file')
