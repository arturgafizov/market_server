from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'apps.test_questions'

router = DefaultRouter()
# router.register(r'speciality', views.SpecialityViewSet, basename='speciality')

urlpatterns = [
    path('test-result/', views.TestResultView.as_view(), name='make_test_result'),
    path('test-result/user/', views.CurrentUserTestResultView.as_view(), name='get_user_test_result'),
    path('test-question-answer/user/', views.TestQuestionAnswerView.as_view(), name='make_test_question_answer'),
    path('test-result/get/', views.GetTestResultView.as_view(), name='get_test_result'),
    path('', include(router.urls)),
]
