from django.test import TestCase

from users.models import User


def is_exist(cls, field):
    return bool(getattr(cls, field))


def is_type_of(cls, field, field_type):
    return cls._meta.get_field(field).get_internal_type() == field_type


class UserRequestTest(TestCase):

    def test_email(self):
        self.assertTrue(is_exist(User, 'email'))
        self.assertTrue(is_type_of(User, 'email', 'CharField'))

    def test_first_name(self):
        self.assertTrue(is_exist(User, 'first_name'))
        self.assertTrue(is_type_of(User, 'first_name', 'CharField'))

    def test_last_name(self):
        self.assertTrue(is_exist(User, 'last_name'))
        self.assertTrue(is_type_of(User, 'last_name', 'CharField'))

    def test_is_staff(self):
        self.assertTrue(is_exist(User, 'is_staff'))
        self.assertTrue(is_type_of(User, 'is_staff', 'BooleanField'))

    def test_is_active(self):
        self.assertTrue(is_exist(User, 'is_active'))
        self.assertTrue(is_type_of(User, 'is_active', 'BooleanField'))

    def test_timestamp_created(self):
        self.assertTrue(is_exist(User, 'timestamp_created'))
        self.assertTrue(is_type_of(User, 'timestamp_created', 'DateTimeField'))

    def test_last_updated(self):
        self.assertTrue(is_exist(User, 'last_updated'))
        self.assertTrue(is_type_of(User, 'last_updated', 'DateTimeField'))