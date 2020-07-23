# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "update_resource"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/resources/{resource_id}/update/"

from .test_case_01 import TestCase01UpdateResourceAPITestCase

__all__ = [
    "TestCase01UpdateResourceAPITestCase"
]
