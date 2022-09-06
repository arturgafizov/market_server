from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils.decorators import method_decorator

from . import swagger_schemas as schemas
from . import serializers
from .models import TestResult, TestAnswer
from .services import TestQuestions


class TestResultView(GenericAPIView):
    serializer_class = serializers.TestResultSerializer

    @method_decorator(name='create', decorator=swagger_auto_schema(**schemas.tags_result_create, ))
    def post(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class CurrentUserTestResultView(APIView):

    @method_decorator(name='list', decorator=swagger_auto_schema(**schemas.tags_question_answer_user_list, ))
    def get(self, request):
        user = request.user
        test_result = TestResult.objects.filter(user_id=user)
        serializer = serializers.TestResultSerializer(test_result, many=True)
        return Response(serializer.data)


class TestQuestionAnswerView(GenericAPIView):
    serializer_class = serializers.TestQuestionAnswerSerializer

    @method_decorator(name='create', decorator=swagger_auto_schema(**schemas.tags_question_answer_user_create, ))
    def post(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        TestQuestions.get_test_result(serializer.data)
        return Response({'detail': True}, status=status.HTTP_200_OK)


class GetTestResultView(GenericAPIView):
    permission_classes = []
    serializer_class = serializers.GetTestResultSerializer

    @method_decorator(name='get', decorator=swagger_auto_schema(**schemas.tags_quantity_questions_answer_user_get, ))
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        test_result = TestResult.objects.get(id=serializer.data['test_result_id'])
        res = TestQuestions.get_user_test_result(test_result.id)
        return Response({'detail': res}, status=status.HTTP_200_OK)
