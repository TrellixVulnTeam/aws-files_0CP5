{"filter":false,"title":"test_case_01.py","tooltip":"/ib_miniprojects_backend/resource_management/views/delete_item/tests/test_case_01.py","undoManager":{"mark":61,"position":61,"stack":[[{"start":{"row":34,"column":32},"end":{"row":36,"column":41},"action":"remove","lines":[" # Returns response object.","        # Which can be used for further response object checks.","        # Add database state checks here."],"id":2}],[{"start":{"row":34,"column":32},"end":{"row":35,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":35,"column":0},"end":{"row":35,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":35,"column":4},"end":{"row":35,"column":8},"action":"remove","lines":["    "],"id":4},{"start":{"row":35,"column":0},"end":{"row":35,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":32,"column":0},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "],"id":6}],[{"start":{"row":33,"column":4},"end":{"row":36,"column":9},"action":"insert","lines":["def setupUser(self, username, password):","        super(TestCase01CreateResourcesAPITestCase, self).setupUser(","            username=username, password=password","        )"],"id":7}],[{"start":{"row":34,"column":14},"end":{"row":34,"column":50},"action":"remove","lines":["TestCase01CreateResourcesAPITestCase"],"id":8},{"start":{"row":34,"column":14},"end":{"row":34,"column":45},"action":"insert","lines":["TestCase01DeleteItemAPITestCase"]}],[{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "],"id":10}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":97},"action":"insert","lines":["@patch('resource_management_auth.interfaces.service_interface.ServiceInterface.get_user_dto')"],"id":11}],[{"start":{"row":39,"column":24},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":12},{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":40,"column":8},"end":{"row":46,"column":48},"action":"insert","lines":["from resource_management.dtos.dtos import UserDto","        userdto = UserDto(","            user_id=1,","            username='Nav',","            is_admin=True","        )","        get_user_dto_mock.return_value = userdto"],"id":13}],[{"start":{"row":39,"column":22},"end":{"row":39,"column":23},"action":"insert","lines":[","],"id":14}],[{"start":{"row":39,"column":23},"end":{"row":39,"column":24},"action":"insert","lines":[" "],"id":15}],[{"start":{"row":39,"column":24},"end":{"row":39,"column":41},"action":"insert","lines":["get_user_dto_mock"],"id":16}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":["f"],"id":17},{"start":{"row":3,"column":1},"end":{"row":3,"column":2},"action":"insert","lines":["r"]},{"start":{"row":3,"column":2},"end":{"row":3,"column":3},"action":"insert","lines":["o"]},{"start":{"row":3,"column":3},"end":{"row":3,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":[" "],"id":18},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["u"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["n"]},{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":["i"]}],[{"start":{"row":3,"column":5},"end":{"row":3,"column":8},"action":"remove","lines":["uni"],"id":19},{"start":{"row":3,"column":5},"end":{"row":3,"column":13},"action":"insert","lines":["unittest"]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["."],"id":20},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["m"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["o"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["c"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["k"]}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":[" "],"id":21},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["i"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["m"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["p"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["o"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["r"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":[" "],"id":22},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["p"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["a"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["t"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["c"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["h"]}],[{"start":{"row":36,"column":9},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":37,"column":0},"end":{"row":37,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["f"],"id":25},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["r"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["o"]},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":[" "],"id":26},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["e"],"id":27},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["s"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["o"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["u"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":5},"end":{"row":6,"column":11},"action":"remove","lines":["resour"],"id":28},{"start":{"row":6,"column":5},"end":{"row":6,"column":24},"action":"insert","lines":["resource_management"]}],[{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["."],"id":29},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["f"]},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["a"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["c"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["t"]},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["o"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":31},"end":{"row":6,"column":32},"action":"insert","lines":["i"],"id":30},{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":["e"]},{"start":{"row":6,"column":33},"end":{"row":6,"column":34},"action":"insert","lines":["s"]},{"start":{"row":6,"column":34},"end":{"row":6,"column":35},"action":"insert","lines":["."]},{"start":{"row":6,"column":35},"end":{"row":6,"column":36},"action":"insert","lines":["f"]},{"start":{"row":6,"column":36},"end":{"row":6,"column":37},"action":"insert","lines":["a"]},{"start":{"row":6,"column":37},"end":{"row":6,"column":38},"action":"insert","lines":["c"]}],[{"start":{"row":6,"column":35},"end":{"row":6,"column":38},"action":"remove","lines":["fac"],"id":31},{"start":{"row":6,"column":35},"end":{"row":6,"column":44},"action":"insert","lines":["factories"]}],[{"start":{"row":6,"column":44},"end":{"row":6,"column":45},"action":"insert","lines":[" "],"id":32},{"start":{"row":6,"column":45},"end":{"row":6,"column":46},"action":"insert","lines":["i"]},{"start":{"row":6,"column":46},"end":{"row":6,"column":47},"action":"insert","lines":["m"]},{"start":{"row":6,"column":47},"end":{"row":6,"column":48},"action":"insert","lines":["p"]},{"start":{"row":6,"column":48},"end":{"row":6,"column":49},"action":"insert","lines":["o"]},{"start":{"row":6,"column":49},"end":{"row":6,"column":50},"action":"insert","lines":["r"]},{"start":{"row":6,"column":50},"end":{"row":6,"column":51},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":51},"end":{"row":6,"column":52},"action":"insert","lines":[" "],"id":33}],[{"start":{"row":6,"column":52},"end":{"row":6,"column":53},"action":"insert","lines":["R"],"id":34},{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"insert","lines":["e"]},{"start":{"row":6,"column":54},"end":{"row":6,"column":55},"action":"insert","lines":["s"]},{"start":{"row":6,"column":55},"end":{"row":6,"column":56},"action":"insert","lines":["o"]},{"start":{"row":6,"column":56},"end":{"row":6,"column":57},"action":"insert","lines":["u"]}],[{"start":{"row":6,"column":52},"end":{"row":6,"column":57},"action":"remove","lines":["Resou"],"id":35},{"start":{"row":6,"column":52},"end":{"row":6,"column":67},"action":"insert","lines":["ResourceFactory"]}],[{"start":{"row":6,"column":52},"end":{"row":6,"column":53},"action":"insert","lines":["("],"id":36}],[{"start":{"row":6,"column":53},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":19},"end":{"row":7,"column":20},"action":"insert","lines":[","],"id":38}],[{"start":{"row":7,"column":20},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["I"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["t"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["e"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["m"]}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"remove","lines":["Item"],"id":40},{"start":{"row":8,"column":4},"end":{"row":8,"column":15},"action":"insert","lines":["ItemFactory"]}],[{"start":{"row":8,"column":15},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":41},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":42}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"insert","lines":[")"],"id":43}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["r"],"id":44},{"start":{"row":42,"column":9},"end":{"row":42,"column":10},"action":"insert","lines":["e"]},{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["s"]},{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":["o"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["u"]},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["e"]},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["c"]},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"remove","lines":["e"],"id":45},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"remove","lines":["c"]},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"remove","lines":["e"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"remove","lines":["u"]}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["u"],"id":46},{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":["r"]},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["c"]},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"insert","lines":[" "],"id":47},{"start":{"row":42,"column":17},"end":{"row":42,"column":18},"action":"insert","lines":["="]}],[{"start":{"row":42,"column":18},"end":{"row":42,"column":19},"action":"insert","lines":[" "],"id":48},{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":["R"]},{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"insert","lines":["e"]},{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"insert","lines":["s"]},{"start":{"row":42,"column":22},"end":{"row":42,"column":23},"action":"insert","lines":["o"]},{"start":{"row":42,"column":23},"end":{"row":42,"column":24},"action":"insert","lines":["u"]},{"start":{"row":42,"column":24},"end":{"row":42,"column":25},"action":"insert","lines":["r"]}],[{"start":{"row":42,"column":19},"end":{"row":42,"column":25},"action":"remove","lines":["Resour"],"id":49},{"start":{"row":42,"column":19},"end":{"row":42,"column":34},"action":"insert","lines":["ResourceFactory"]}],[{"start":{"row":42,"column":34},"end":{"row":42,"column":35},"action":"insert","lines":["."],"id":50},{"start":{"row":42,"column":35},"end":{"row":42,"column":36},"action":"insert","lines":["c"]},{"start":{"row":42,"column":36},"end":{"row":42,"column":37},"action":"insert","lines":["r"]},{"start":{"row":42,"column":37},"end":{"row":42,"column":38},"action":"insert","lines":["e"]},{"start":{"row":42,"column":38},"end":{"row":42,"column":39},"action":"insert","lines":["a"]},{"start":{"row":42,"column":39},"end":{"row":42,"column":40},"action":"insert","lines":["t"]},{"start":{"row":42,"column":40},"end":{"row":42,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":42,"column":41},"end":{"row":42,"column":43},"action":"insert","lines":["()"],"id":51}],[{"start":{"row":42,"column":43},"end":{"row":43,"column":0},"action":"insert","lines":["",""],"id":52},{"start":{"row":43,"column":0},"end":{"row":43,"column":8},"action":"insert","lines":["        "]},{"start":{"row":43,"column":8},"end":{"row":43,"column":9},"action":"insert","lines":["I"]},{"start":{"row":43,"column":9},"end":{"row":43,"column":10},"action":"insert","lines":["t"]},{"start":{"row":43,"column":10},"end":{"row":43,"column":11},"action":"insert","lines":["e"]},{"start":{"row":43,"column":11},"end":{"row":43,"column":12},"action":"insert","lines":["m"]}],[{"start":{"row":43,"column":8},"end":{"row":43,"column":12},"action":"remove","lines":["Item"],"id":53},{"start":{"row":43,"column":8},"end":{"row":43,"column":19},"action":"insert","lines":["ItemFactory"]}],[{"start":{"row":43,"column":19},"end":{"row":43,"column":20},"action":"insert","lines":["."],"id":54},{"start":{"row":43,"column":20},"end":{"row":43,"column":21},"action":"insert","lines":["c"]},{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["e"]}],[{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"remove","lines":["e"],"id":55}],[{"start":{"row":43,"column":21},"end":{"row":43,"column":22},"action":"insert","lines":["r"],"id":56},{"start":{"row":43,"column":22},"end":{"row":43,"column":23},"action":"insert","lines":["e"]},{"start":{"row":43,"column":23},"end":{"row":43,"column":24},"action":"insert","lines":["a"]},{"start":{"row":43,"column":24},"end":{"row":43,"column":25},"action":"insert","lines":["t"]},{"start":{"row":43,"column":25},"end":{"row":43,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":43,"column":26},"end":{"row":43,"column":28},"action":"insert","lines":["()"],"id":57}],[{"start":{"row":43,"column":27},"end":{"row":43,"column":28},"action":"insert","lines":["r"],"id":58},{"start":{"row":43,"column":28},"end":{"row":43,"column":29},"action":"insert","lines":["e"]},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["s"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["o"]},{"start":{"row":43,"column":31},"end":{"row":43,"column":32},"action":"insert","lines":["u"]}],[{"start":{"row":43,"column":27},"end":{"row":43,"column":32},"action":"remove","lines":["resou"],"id":59},{"start":{"row":43,"column":27},"end":{"row":43,"column":35},"action":"insert","lines":["resource"]}],[{"start":{"row":43,"column":35},"end":{"row":43,"column":36},"action":"insert","lines":["="],"id":60},{"start":{"row":43,"column":36},"end":{"row":43,"column":37},"action":"insert","lines":["r"]},{"start":{"row":43,"column":37},"end":{"row":43,"column":38},"action":"insert","lines":["e"]},{"start":{"row":43,"column":38},"end":{"row":43,"column":39},"action":"insert","lines":["s"]},{"start":{"row":43,"column":39},"end":{"row":43,"column":40},"action":"insert","lines":["o"]},{"start":{"row":43,"column":40},"end":{"row":43,"column":41},"action":"insert","lines":["u"]},{"start":{"row":43,"column":41},"end":{"row":43,"column":42},"action":"insert","lines":["r"]},{"start":{"row":43,"column":42},"end":{"row":43,"column":43},"action":"insert","lines":["c"]}],[{"start":{"row":43,"column":43},"end":{"row":43,"column":44},"action":"insert","lines":["e"],"id":61}],[{"start":{"row":25,"column":144},"end":{"row":25,"column":145},"action":"remove","lines":["\""],"id":62},{"start":{"row":25,"column":143},"end":{"row":25,"column":144},"action":"remove","lines":["e"]},{"start":{"row":25,"column":142},"end":{"row":25,"column":143},"action":"remove","lines":["t"]},{"start":{"row":25,"column":141},"end":{"row":25,"column":142},"action":"remove","lines":["e"]},{"start":{"row":25,"column":140},"end":{"row":25,"column":141},"action":"remove","lines":["l"]},{"start":{"row":25,"column":139},"end":{"row":25,"column":140},"action":"remove","lines":["e"]},{"start":{"row":25,"column":138},"end":{"row":25,"column":139},"action":"remove","lines":["d"]},{"start":{"row":25,"column":137},"end":{"row":25,"column":138},"action":"remove","lines":["\""]},{"start":{"row":25,"column":136},"end":{"row":25,"column":137},"action":"remove","lines":[" "]},{"start":{"row":25,"column":135},"end":{"row":25,"column":136},"action":"remove","lines":[","]},{"start":{"row":25,"column":134},"end":{"row":25,"column":135},"action":"remove","lines":["\""]},{"start":{"row":25,"column":133},"end":{"row":25,"column":134},"action":"remove","lines":["e"]},{"start":{"row":25,"column":132},"end":{"row":25,"column":133},"action":"remove","lines":["t"]},{"start":{"row":25,"column":131},"end":{"row":25,"column":132},"action":"remove","lines":["a"]},{"start":{"row":25,"column":130},"end":{"row":25,"column":131},"action":"remove","lines":["d"]},{"start":{"row":25,"column":129},"end":{"row":25,"column":130},"action":"remove","lines":["p"]},{"start":{"row":25,"column":128},"end":{"row":25,"column":129},"action":"remove","lines":["u"]},{"start":{"row":25,"column":127},"end":{"row":25,"column":128},"action":"remove","lines":["\""]}],[{"start":{"row":25,"column":126},"end":{"row":25,"column":127},"action":"remove","lines":[" "],"id":63},{"start":{"row":25,"column":125},"end":{"row":25,"column":126},"action":"remove","lines":[","]}]]},"ace":{"folds":[],"scrolltop":634.5,"scrollleft":0,"selection":{"start":{"row":45,"column":4},"end":{"row":54,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":30,"state":"start","mode":"ace/mode/python"}},"timestamp":1593702010331,"hash":"253dd66a0490c5275f1f15fdefc6c5e5ce8bc8d3"}