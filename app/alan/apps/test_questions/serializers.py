from rest_framework import serializers

from apps.test_questions.choices import TestType
from apps.test_questions.models import TestQuestion, TestAnswer, TestResult, TestQuestionAnswer


class TestQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestQuestion
        fields = ('text', 'category', 'speciality', 'photo')


class TestAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestAnswer
        fields = ('text', 'test_question', 'correct', )


class TestQuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestQuestionAnswer
        fields = ('test_result', 'questions', 'answer', 'correct', 'created_at', )


class TestResultSerializer(serializers.ModelSerializer):
    # test_results = TestQuestionAnswerSerializer(many=True)

    class Meta:
        model = TestResult
        fields = ('user', 'type', 'category', 'started_at', 'finished_at', 'test_results')

    def validate(self, data):
        type = data.get('type')
        category = data.get('category')
        if type == TestType.THEMATIC and category is None:
            raise serializers.ValidationError('Категория обезательно назначается на тематическое вид вопросов')
        return data

    def create(self, validated_data):
        user = self.context.get('request').user
        question_answer_data = validated_data.get('test_results')
        validated_data.pop('test_results')
        validated_data['user'] = user
        new_test = TestResult.objects.create(**validated_data)
        new_test.test_results.set(question_answer_data)
        return new_test

