from django.test import TestCase

from sites.models import UserRequest, BlockedSites


def is_exist(cls, field):
    return bool(getattr(cls, field))


def is_type_of(cls, field, field_type):
    return cls._meta.get_field(field).get_internal_type() == field_type


class UserRequestTest(TestCase):

    def test_domain_name(self):
        self.assertTrue(is_exist(UserRequest, 'domain_name'))
        self.assertTrue(is_type_of(UserRequest, 'domain_name', 'CharField'))

    def test_description(self):
        self.assertTrue(is_exist(UserRequest, 'description'))
        self.assertTrue(is_type_of(UserRequest, 'description', 'CharField'))

    def test_user_email(self):
        self.assertTrue(is_exist(UserRequest, 'user_email'))
        self.assertTrue(is_type_of(UserRequest, 'user_email', 'CharField'))

    def test_ip_address(self):
        self.assertTrue(is_exist(UserRequest, 'ip_address'))
        self.assertTrue(is_type_of(UserRequest, 'ip_address', 'GenericIPAddressField'))

    def test_additional_info(self):
        self.assertTrue(is_exist(UserRequest, 'additional_info'))
        self.assertTrue(is_type_of(UserRequest, 'additional_info', 'CharField'))

    def test_created(self):
        self.assertTrue(is_exist(UserRequest, 'created'))
        self.assertTrue(is_type_of(UserRequest, 'created', 'DateTimeField'))


class BlockedSitesTest(TestCase):

    def test_is_blocked(self):
        self.assertTrue(is_exist(BlockedSites, 'is_blocked'))
        self.assertTrue(is_type_of(BlockedSites, 'is_blocked', 'BooleanField'))

    def test_site(self):
        self.assertTrue(is_exist(BlockedSites, 'site'))
        self.assertTrue(is_type_of(BlockedSites, 'site', 'ForeignKey'))

    def test_email_was_sent(self):
        self.assertTrue(is_exist(BlockedSites, 'email_was_sent'))
        self.assertTrue(is_type_of(BlockedSites, 'email_was_sent', 'BooleanField'))