from django.contrib import admin

from .models import TestAnswer, TestQuestion, TestResult, TestQuestionAnswer


class QuestionsInline(admin.TabularInline):
    model = TestResult.questions.through


class TestQuestionAnswerInline(admin.TabularInline):
    model = TestQuestionAnswer
    extra = 0


@admin.register(TestAnswer)
class TestAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'question', 'correct')
    list_editable = ('correct', )
    list_per_page = 20
    readonly_fields = ('id',)


@admin.register(TestQuestion)
class TestQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'photo', 'category', 'speciality')
    list_per_page = 20
    readonly_fields = ('id',)


@admin.register(TestResult)
class TestResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'type', 'category', 'started_at', 'finished_at', )
    inlines = [QuestionsInline, TestQuestionAnswerInline]
    exclude = ('questions',)
    list_per_page = 20
    readonly_fields = ('id',)


@admin.register(TestQuestionAnswer)
class TestQuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'test_result', 'questions', 'answer', 'correct', 'created_at')
    list_per_page = 20
    list_editable = ('correct', )
    readonly_fields = ('id',)
