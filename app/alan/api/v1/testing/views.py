from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from . import serializers
from .services import TestQuestions


# class TestQuestionAnswerView(GenericAPIView):
#     serializer_class = serializers.TestQuestionAnswerSerializer
#
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         print(serializer.data)
#         TestQuestions.get_test_result(serializer.data)
#         return Response({'detail': True}, status=status.HTTP_200_OK)
