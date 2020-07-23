# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_users"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/users/v1/"

from .test_case_01 import TestCase01GetUsersAPITestCase

__all__ = [
    "TestCase01GetUsersAPITestCase"
]
