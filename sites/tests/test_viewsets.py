from django.test import RequestFactory, TestCase
from sites.api.v1.viewsets import RequestView
from sites.models import UserRequest


class TestUserRequest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

        self.url = "/api/v1/request/"

        self.data_request = {
            'domain_name': 'test_roskomnadzor.com',
            'description': 'check it',
            'user_email': 'info.no-reply@roskomnadzor.com',
            'ip_address': '127.0.0.1',
        }

    def test_for_method_post(self):
        request = self.factory.post(self.url, self.data_request)
        view = RequestView.as_view({'post': 'create'})
        response = view(request).render()

        test_user_request = UserRequest.objects.last()

        self.assertEqual(
            response.status_code, 201)
        self.assertEqual(
            test_user_request.domain_name, self.data_request["domain_name"])
        self.assertEqual(
            test_user_request.description, self.data_request["description"])
        self.assertEqual(
            test_user_request.user_email, self.data_request["user_email"])
        self.assertEqual(
            test_user_request.ip_address, self.data_request["ip_address"])





