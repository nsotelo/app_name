import hypothesis
from {{ app_name }} import views
from django import test
from django.contrib.auth import models as auth_models
from hypothesis.extra import django


class TestAdminView(django.TestCase):
    def test_anonymous(self):
        req = test.RequestFactory().get("/")
        req.user = auth_models.AnonymousUser()
        resp = views.AdminView.as_view()(req)
        self.assertIn("login", resp.url, "Should be redirected.")

    @hypothesis.given(django.from_model(auth_models.User))
    def test_superuser(self, user):
        user.is_superuser = True
        req = test.RequestFactory().get("/")
        req.user = user
        resp = views.AdminView.as_view()(req)
        self.assertEqual(resp.status_code, 200, "Authenticated user can access")
