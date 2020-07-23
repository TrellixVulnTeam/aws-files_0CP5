{"filter":false,"title":"test_invalid_password.py","tooltip":"/ib_miniprojects_backend/resource_management/tests/presenters/test_invalid_password.py","undoManager":{"mark":41,"position":41,"stack":[[{"start":{"row":0,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["import pytest","from resource_management.exceptions.exceptions import (","    UserDoesNotExist,","    InvalidPassword",")","from resource_management.presenters.presenter_implementation import \\","    PresenterImplementation","","def test_username_not_exists():","","    #Arrange","    presenter = PresenterImplementation()","","    #Act","    with pytest.raises(UserDoesNotExist):","        presenter.username_not_exists()",""],"id":1}],[{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"remove","lines":[","],"id":2},{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"remove","lines":["t"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"remove","lines":["s"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"remove","lines":["i"]},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["x"]},{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["E"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":["t"]},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":["o"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":["N"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":["s"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["e"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["o"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["D"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["r"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["e"],"id":3},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":["s"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"remove","lines":["U"]},{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"remove","lines":["    "]},{"start":{"row":1,"column":55},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"remove","lines":[")"],"id":4},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"remove","lines":["("]},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"remove","lines":["s"]},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"remove","lines":["t"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["s"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["i"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["x"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["e"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["_"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["t"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["o"]},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"remove","lines":["n"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["_"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["e"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["m"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["a"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":["n"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"remove","lines":["r"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["e"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":["s"]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["u"]}],[{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"insert","lines":["i"],"id":5},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"insert","lines":["n"]}],[{"start":{"row":14,"column":18},"end":{"row":14,"column":20},"action":"remove","lines":["in"],"id":6},{"start":{"row":14,"column":18},"end":{"row":14,"column":34},"action":"insert","lines":["invalid_password"]}],[{"start":{"row":14,"column":34},"end":{"row":14,"column":36},"action":"insert","lines":["()"],"id":7}],[{"start":{"row":13,"column":38},"end":{"row":13,"column":39},"action":"remove","lines":["t"],"id":8},{"start":{"row":13,"column":37},"end":{"row":13,"column":38},"action":"remove","lines":["s"]},{"start":{"row":13,"column":36},"end":{"row":13,"column":37},"action":"remove","lines":["i"]},{"start":{"row":13,"column":35},"end":{"row":13,"column":36},"action":"remove","lines":["x"]},{"start":{"row":13,"column":34},"end":{"row":13,"column":35},"action":"remove","lines":["E"]},{"start":{"row":13,"column":33},"end":{"row":13,"column":34},"action":"remove","lines":["t"]},{"start":{"row":13,"column":32},"end":{"row":13,"column":33},"action":"remove","lines":["o"]},{"start":{"row":13,"column":31},"end":{"row":13,"column":32},"action":"remove","lines":["N"]},{"start":{"row":13,"column":30},"end":{"row":13,"column":31},"action":"remove","lines":["s"]},{"start":{"row":13,"column":29},"end":{"row":13,"column":30},"action":"remove","lines":["e"]},{"start":{"row":13,"column":28},"end":{"row":13,"column":29},"action":"remove","lines":["o"]},{"start":{"row":13,"column":27},"end":{"row":13,"column":28},"action":"remove","lines":["D"]},{"start":{"row":13,"column":26},"end":{"row":13,"column":27},"action":"remove","lines":["r"]},{"start":{"row":13,"column":25},"end":{"row":13,"column":26},"action":"remove","lines":["e"]},{"start":{"row":13,"column":24},"end":{"row":13,"column":25},"action":"remove","lines":["s"]},{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["U"]}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["i"],"id":9}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["i"],"id":10}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"insert","lines":["I"],"id":11}],[{"start":{"row":13,"column":23},"end":{"row":13,"column":24},"action":"remove","lines":["I"],"id":12},{"start":{"row":13,"column":23},"end":{"row":13,"column":38},"action":"insert","lines":["InvalidPassword"]}],[{"start":{"row":5,"column":27},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "],"id":14}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":15},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":24},"action":"insert","lines":["from resource_management.constants.exception_message import \\","    USER_DOES_NOT_EXISTS"],"id":16}],[{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"remove","lines":["s"],"id":17},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"remove","lines":["t"]},{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"remove","lines":["s"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"remove","lines":["i"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"remove","lines":["x"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"remove","lines":["e"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"remove","lines":["_"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"remove","lines":["t"]},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"remove","lines":["o"]},{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"remove","lines":["n"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"remove","lines":["_"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"remove","lines":["e"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"remove","lines":["m"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"remove","lines":["a"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["n"]}],[{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["r"],"id":18},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["e"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["s"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"remove","lines":["u"]}],[{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["i"],"id":19},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["n"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["v"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["a"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["l"]},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["i"]},{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"insert","lines":["d"]},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["_"]},{"start":{"row":11,"column":17},"end":{"row":11,"column":18},"action":"insert","lines":["p"]}],[{"start":{"row":11,"column":18},"end":{"row":11,"column":19},"action":"insert","lines":["a"],"id":20},{"start":{"row":11,"column":19},"end":{"row":11,"column":20},"action":"insert","lines":["s"]},{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["s"]},{"start":{"row":11,"column":21},"end":{"row":11,"column":22},"action":"insert","lines":["w"]},{"start":{"row":11,"column":22},"end":{"row":11,"column":23},"action":"insert","lines":["o"]},{"start":{"row":11,"column":23},"end":{"row":11,"column":24},"action":"insert","lines":["r"]},{"start":{"row":11,"column":24},"end":{"row":11,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":[" "],"id":21}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"remove","lines":[" "],"id":22}],[{"start":{"row":11,"column":25},"end":{"row":11,"column":26},"action":"insert","lines":["_"],"id":23},{"start":{"row":11,"column":26},"end":{"row":11,"column":27},"action":"insert","lines":["r"]},{"start":{"row":11,"column":27},"end":{"row":11,"column":28},"action":"insert","lines":["a"]},{"start":{"row":11,"column":28},"end":{"row":11,"column":29},"action":"insert","lines":["i"]},{"start":{"row":11,"column":29},"end":{"row":11,"column":30},"action":"insert","lines":["s"]},{"start":{"row":11,"column":30},"end":{"row":11,"column":31},"action":"insert","lines":["e"]},{"start":{"row":11,"column":31},"end":{"row":11,"column":32},"action":"insert","lines":["_"]},{"start":{"row":11,"column":32},"end":{"row":11,"column":33},"action":"insert","lines":["e"]},{"start":{"row":11,"column":33},"end":{"row":11,"column":34},"action":"insert","lines":["x"]}],[{"start":{"row":11,"column":34},"end":{"row":11,"column":35},"action":"insert","lines":["c"],"id":24},{"start":{"row":11,"column":35},"end":{"row":11,"column":36},"action":"insert","lines":["e"]},{"start":{"row":11,"column":36},"end":{"row":11,"column":37},"action":"insert","lines":["p"]},{"start":{"row":11,"column":37},"end":{"row":11,"column":38},"action":"insert","lines":["t"]},{"start":{"row":11,"column":38},"end":{"row":11,"column":39},"action":"insert","lines":["i"]},{"start":{"row":11,"column":39},"end":{"row":11,"column":40},"action":"insert","lines":["o"]},{"start":{"row":11,"column":40},"end":{"row":11,"column":41},"action":"insert","lines":["n"]}],[{"start":{"row":7,"column":4},"end":{"row":7,"column":24},"action":"remove","lines":["USER_DOES_NOT_EXISTS"],"id":25},{"start":{"row":7,"column":4},"end":{"row":7,"column":20},"action":"insert","lines":["INVALID_PASSWORD"]}],[{"start":{"row":13,"column":12},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":26},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":55},"action":"insert","lines":["exception_message = USER_DOES_NOT_EXISTS[0]","    exception_response_status = USER_DOES_NOT_EXISTS[1]"],"id":27}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":44},"action":"remove","lines":["USER_DOES_NOT_EXISTS"],"id":28},{"start":{"row":14,"column":24},"end":{"row":14,"column":40},"action":"insert","lines":["INVALID_PASSWORD"]}],[{"start":{"row":15,"column":32},"end":{"row":15,"column":52},"action":"remove","lines":["USER_DOES_NOT_EXISTS"],"id":29},{"start":{"row":15,"column":32},"end":{"row":15,"column":48},"action":"insert","lines":["INVALID_PASSWORD"]}],[{"start":{"row":20,"column":36},"end":{"row":21,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":21,"column":0},"end":{"row":21,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["    "],"id":31},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":21,"column":0},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":32}],[{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "],"id":33}],[{"start":{"row":22,"column":4},"end":{"row":24,"column":66},"action":"insert","lines":["#Assert","    assert exception.value.message == exception_message","    assert exception.value.res_status == exception_response_status"],"id":34}],[{"start":{"row":1,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":["from resource_management.exceptions.exceptions import (","    InvalidPassword",")"],"id":35},{"start":{"row":1,"column":0},"end":{"row":1,"column":63},"action":"insert","lines":["from django_swagger_utils.drf_server.exceptions import NotFound"]}],[{"start":{"row":1,"column":62},"end":{"row":1,"column":63},"action":"remove","lines":["d"],"id":36},{"start":{"row":1,"column":61},"end":{"row":1,"column":62},"action":"remove","lines":["n"]},{"start":{"row":1,"column":60},"end":{"row":1,"column":61},"action":"remove","lines":["u"]},{"start":{"row":1,"column":59},"end":{"row":1,"column":60},"action":"remove","lines":["o"]},{"start":{"row":1,"column":58},"end":{"row":1,"column":59},"action":"remove","lines":["F"]},{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"remove","lines":["t"]},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"remove","lines":["o"]},{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"remove","lines":["N"]}],[{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"insert","lines":["B"],"id":37},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"insert","lines":["a"]},{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"insert","lines":["d"]}],[{"start":{"row":1,"column":55},"end":{"row":1,"column":58},"action":"remove","lines":["Bad"],"id":38},{"start":{"row":1,"column":55},"end":{"row":1,"column":65},"action":"insert","lines":["BadRequest"]}],[{"start":{"row":17,"column":23},"end":{"row":17,"column":38},"action":"remove","lines":["InvalidPassword"],"id":39},{"start":{"row":17,"column":23},"end":{"row":17,"column":33},"action":"insert","lines":["BadRequest"]}],[{"start":{"row":17,"column":34},"end":{"row":17,"column":35},"action":"insert","lines":[" "],"id":40},{"start":{"row":17,"column":35},"end":{"row":17,"column":36},"action":"insert","lines":["a"]},{"start":{"row":17,"column":36},"end":{"row":17,"column":37},"action":"insert","lines":["s"]}],[{"start":{"row":17,"column":37},"end":{"row":17,"column":38},"action":"insert","lines":[" "],"id":41},{"start":{"row":17,"column":38},"end":{"row":17,"column":39},"action":"insert","lines":["e"]},{"start":{"row":17,"column":39},"end":{"row":17,"column":40},"action":"insert","lines":["x"]},{"start":{"row":17,"column":40},"end":{"row":17,"column":41},"action":"insert","lines":["c"]},{"start":{"row":17,"column":41},"end":{"row":17,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":17,"column":38},"end":{"row":17,"column":42},"action":"remove","lines":["exce"],"id":42},{"start":{"row":17,"column":38},"end":{"row":17,"column":47},"action":"insert","lines":["exception"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":47},"end":{"row":17,"column":47},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591158936411,"hash":"c43d08284043642b1dffb0bc3b32e12d885e4087"}