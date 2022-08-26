import os
from django.contrib.auth import get_user_model
from django.db import models
import django.utils.timezone
from apps.docs.models import Category, Speciality
from apps.test_questions.choices import TestType

User = get_user_model()

    # продолжительность теста - нету
    # процент прохождения теста - 100%
    # правильный ответ только один
    # сортировка - рандомная


class TestQuestion(models.Model):
    text = models.TextField(verbose_name='Текст вопроса')
    photo = models.ImageField(blank=True, upload_to='test_questions/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category_set')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='Специальность')

    objects = models.Manager()

    @property
    def filename(self):
        return os.path.basename(self.photo)

    def __str__(self):
        return f'#{self.pk} {self.text}'


class TestAnswer(models.Model):
    text = models.TextField(verbose_name='Текст ответа')
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='test_questions',
                                      verbose_name='тестовый вопрос')
    correct = models.BooleanField(verbose_name='Правильность ответа')

    objects = models.Manager()


    def __str__(self):
        return f'#{self.pk} {self.text}'


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users', verbose_name='пользователь')
    type = models.CharField(choices=TestType.choices, max_length=128)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    started_at = models.DateTimeField(auto_now_add=True, verbose_name='Начало')
    finished_at = models.DateTimeField(default=django.utils.timezone.now, verbose_name='Закрыто')
    questions = models.ManyToManyField(TestQuestion, related_name='question_set', verbose_name='вопросы')

    objects = models.Manager()

    def __str__(self):
        return f'#{self.pk} {self.user}'


class TestQuestionAnswer(models.Model):
    test_result = models.ForeignKey(TestResult, on_delete=models.CASCADE, related_name='test_results',
                                    verbose_name='результат теста')
    questions = models.ForeignKey(TestQuestion, on_delete=models.CASCADE, related_name='test_question_set',
                                       verbose_name='Тестовый вопрос')
    answer = models.ForeignKey(TestAnswer, on_delete=models.CASCADE, related_name='test_answers',
                                    verbose_name='Тестовый ответ')
    correct = models.BooleanField(verbose_name='Правильность ответа')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    objects = models.Manager()
