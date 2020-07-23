# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_items"
REQUEST_METHOD = "get"
URL_SUFFIX = "resources/{resource_id}/items/v1/"

from .test_case_01 import TestCase01GetItemsAPITestCase

__all__ = [
    "TestCase01GetItemsAPITestCase"
]
