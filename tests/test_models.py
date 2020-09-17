import hypothesis
from {{ app_name }} import models
from hypothesis import strategies
from hypothesis.extra import django


class TestModel(django.TestCase):
    @hypothesis.given(django.from_model(models.Model))
    def test_model(self, my_model):
        self.assertEqual(my_model, my_model)
