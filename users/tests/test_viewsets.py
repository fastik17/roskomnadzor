import json

from django.test import RequestFactory, TestCase
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.test import force_authenticate
from users.models import User


class TestloginViews(TestCase):
    def setUp(self):

        self.url_login = "/api/v1/signin/"
        self.factory = RequestFactory()

        user = User.objects.create(email='testuser@gmail.com')
        user.set_password('password')
        user.save()

    def test_login(self):
        data_login = {
                      "email": "testuser@gmail.com",
                      "password": "password"
                     }

        request = self.factory.post(
            self.url_login,
            data_login,
            content_type='application/json'
        )

        force_authenticate(request)
        view = TokenObtainPairView.as_view()

        response = view(request).render()
        data = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(set(data.keys()),
                         {
                             "refresh",
                             "access",
                         })