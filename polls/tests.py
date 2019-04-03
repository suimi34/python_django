from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        for testCase in [
            [(timezone.now() + datetime.timedelta(days=30)), False],
            [(timezone.now() - datetime.timedelta(days=1, seconds=1)), False],
            [(timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)), True],
        ]:
            future_question = Question(pub_date=testCase[0])
            self.assertIs(future_question.was_published_recently(), testCase[1])
