{"filter":false,"title":"test_case_03.py","tooltip":"/ib_miniprojects_backend/resource_management/views/delete_item/tests/test_case_03.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":49,"column":0},"action":"insert","lines":["\"\"\"","# TODO: Update test case description","\"\"\"","","from django_swagger_utils.utils.test import CustomAPITestCase","from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX","from resource_management.factories.factories import (","    ResourceFactory,","    ItemFactory",")","","","REQUEST_BODY = \"\"\"","{","    \"item_ids\": [","        2","    ]","}","\"\"\"","","TEST_CASE = {","    \"request\": {","        \"path_params\": {},","        \"query_params\": {},","        \"header_params\": {},","        \"securities\": {\"oauth\": {\"tokenUrl\": \"http://auth.ibtspl.com/oauth2/\", \"flow\": \"password\", \"scopes\": [\"read\", \"write\"], \"type\": \"oauth2\"}},","        \"body\": REQUEST_BODY,","    },","}","","","class TestCase02DeleteItemAPITestCase(CustomAPITestCase):","    app_name = APP_NAME","    operation_name = OPERATION_NAME","    request_method = REQUEST_METHOD","    url_suffix = URL_SUFFIX","    test_case_dict = TEST_CASE","","    def setupUser(self, username, password):","        super(TestCase02DeleteItemAPITestCase, self).setupUser(","            username=username, password=password","        )","        self.foo_user.is_admin = True","        self.foo_user.save()","        resource = ResourceFactory.create()","        ItemFactory.create(resource=resource)","","    def test_case(self):","        self.default_test_case()",""],"id":1}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"remove","lines":["2"],"id":2}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":9},"action":"insert","lines":["1"],"id":3}],[{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"remove","lines":["2"],"id":4}],[{"start":{"row":31,"column":15},"end":{"row":31,"column":16},"action":"insert","lines":["3"],"id":5}],[{"start":{"row":39,"column":23},"end":{"row":39,"column":24},"action":"remove","lines":["2"],"id":6}],[{"start":{"row":39,"column":23},"end":{"row":39,"column":24},"action":"insert","lines":["3"],"id":7}]]},"ace":{"folds":[],"scrolltop":59.5,"scrollleft":0,"selection":{"start":{"row":39,"column":24},"end":{"row":39,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":50,"mode":"ace/mode/python"}},"timestamp":1593172634802,"hash":"f2d2aace1c78901be84b1a7c00c0e485788b8d20"}