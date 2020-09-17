import hypothesis
import pytest
from {{ app_name }} import admin, models
from django.contrib.admin.sites import AdminSite
from hypothesis.extra import django


@pytest.mark.django_db
class TestModelAdmin(django.TestCase):
    @hypothesis.given(django.from_model(models.Model),)
    def test_admin(self, model):
        site = AdminSite()
        model_admin = admin.ModelAdmin(models.Model, site)
        self.assertEqual(
            model_admin.something(model),
            model.something(),
            "Should do something.",
        )
