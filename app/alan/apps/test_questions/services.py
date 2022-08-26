from apps.test_questions.models import TestResult


class TestQuestions:

    @staticmethod
    def get_test_result(data):
        test_result = TestResult.objects.get(id=data['test_result'])
        test_result.finished_at = data['created_at']
        test_result.save(update_fields=['finished_at'])
        return test_result
