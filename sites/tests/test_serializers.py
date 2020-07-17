from django.test import TestCase

from sites.models import UserRequest, BlockedSites
from sites.api.v1.serializers import UserRequestSerializer,\
    UserRequestInfoSerializer, BlockedSitesSerializer


class UserRequestSerializerTest(TestCase):
    def setUp(self):
        self.user_request_attributes = \
            {
                'domain_name': 'roskomnadzor.com',
                'description': 'check it',
                'user_email': 'info.no-reply@roskomnadzor.com',
            }

        self.user_request = UserRequest.objects.create(
            **self.user_request_attributes)
        self.serializer = UserRequestSerializer(self.user_request)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()),
                         {
                             'id',
                             'domain_name',
                             'description',
                             'user_email',
                             'created'
                         })


class UserRequestInfoSerializerTest(TestCase):

    def setUp(self):
        self.user_request_attributes = \
            {
                'domain_name': 'roskomnadzor.com',
                'description': 'check it',
                'user_email': 'info.no-reply@roskomnadzor.com',
                'ip_address': '127.0.0.1',
                'additional_info': 'some browser',

            }

        self.user_request = UserRequest.objects.create(
            **self.user_request_attributes)
        self.serializer = UserRequestInfoSerializer(self.user_request)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()),
                         {
                             'domain_name',
                             'description',
                             'user_email',
                             'ip_address',
                             'additional_info',
                             'created'
                         })


class BlockedSitesSerializerTest(TestCase):

    def setUp(self):
        self.site = UserRequest.objects.create(
            domain_name='roskomnadzor.com')

        self.blocked_sites_attributes = \
            {
                'is_blocked': True,
                'email_was_sent': True,
                'site': self.site,

            }

        self.block_sites = BlockedSites.objects.create(
            **self.blocked_sites_attributes)
        self.serializer = BlockedSitesSerializer(self.block_sites)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(set(data.keys()),
                         {
                             'id',
                             'is_blocked',
                             'email_was_sent',
                             'site',
                         })
