# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_admin_resources"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/resources/"

from .test_case_01 import TestCase01GetAdminResourcesAPITestCase

__all__ = [
    "TestCase01GetAdminResourcesAPITestCase"
]
