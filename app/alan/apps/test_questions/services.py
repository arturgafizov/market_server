from apps.test_questions.models import TestResult, TestQuestionAnswer


class TestQuestions:

    @staticmethod
    def get_test_result(data):
        test_result = TestResult.objects.get(id=data['test_result'])
        test_result.finished_at = data['created_at']
        test_result.save(update_fields=['finished_at'])
        return test_result

    @staticmethod
    def get_user_test_result(test_result_id: int):
        total_questions = TestQuestionAnswer.objects.filter(test_result=test_result_id).count()
        true_questions = TestQuestionAnswer.objects.filter(test_result=test_result_id, correct=True).count()
        false_questions = TestQuestionAnswer.objects.filter(test_result=test_result_id, correct=False).count()
        if false_questions != 0:
            result = f'Тест не пройден, {false_questions} ответов из  {total_questions} неправильные'
            return result
        result = f'Тест пройден успешно, колличество правильных/неправильных ответов {true_questions}/{false_questions}'
        return result
