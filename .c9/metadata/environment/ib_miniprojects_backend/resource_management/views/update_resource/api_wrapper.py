{"filter":false,"title":"api_wrapper.py","tooltip":"/ib_miniprojects_backend/resource_management/views/update_resource/api_wrapper.py","undoManager":{"mark":58,"position":58,"stack":[[{"start":{"row":0,"column":0},"end":{"row":28,"column":28},"action":"remove","lines":["from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    try:","        from resource_management.views.update_resource.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from resource_management.views.update_resource.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from resource_management.views.update_resource.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"resource_management\", test_case=test_case,","        operation_name=\"update_resource\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]"],"id":5},{"start":{"row":0,"column":0},"end":{"row":68,"column":0},"action":"insert","lines":["from django.http import HttpResponse","from django_swagger_utils.drf_server.utils.decorator.interface_decorator \\","    import validate_decorator","from .validator_class import ValidatorClass","from raven.utils import json","from resource_management.interactors.update_resource_interactor import \\","    UpdateResourceInteractor","from resource_management.storages.storage_implementation import \\","    StorageImplementation","from resource_management.presenters.presenter_implementation import \\","    PresenterImplementation","","@validate_decorator(validator_class=ValidatorClass)","def api_wrapper(*args, **kwargs):","    # ---------MOCK IMPLEMENTATION---------","","    user = kwargs['user']","    user_id = user.id","    resource_id = kwargs['resource_id']","    requested_data = kwargs['request_data']","    resource_name = requested_data['resource_name']","    description = requested_data['description']","    link = requested_data['link']","    thumbnail = requested_data['thumbnail']","","    user_storage = StorageImplementation()","    presenter = PresenterImplementation()","","    interactor = UpdateResourceInteractor(","        user_storage=user_storage,","        presenter=presenter","    )","","    resource_dict = interactor.update_resources(","        user_id=user_id,","        resource_id=resource_id,","        resource_name=resource_name,","        description=description,","        link=link,","        thumbnail=thumbnail","    )","","    data = json.dumps(resource_dict)","    response = HttpResponse(data, status=200)","    return response","","    \"\"\"","    try:","        from resource_management.views.update_resource.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from resource_management.views.update_resource.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from resource_management.views.update_resource.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"resource_management\", test_case=test_case,","        operation_name=\"update_resource\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]","    \"\"\"",""]}],[{"start":{"row":45,"column":0},"end":{"row":68,"column":0},"action":"remove","lines":["","    \"\"\"","    try:","        from resource_management.views.update_resource.tests.test_case_01 \\","            import TEST_CASE as test_case","    except ImportError:","        from resource_management.views.update_resource.tests.test_case_01 \\","            import test_case","","    from django_swagger_utils.drf_server.utils.server_gen.mock_response \\","        import mock_response","    try:","        from resource_management.views.update_resource.request_response_mocks \\","            import RESPONSE_200_JSON","    except ImportError:","        RESPONSE_200_JSON = ''","    response_tuple = mock_response(","        app_name=\"resource_management\", test_case=test_case,","        operation_name=\"update_resource\",","        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,","        group_name=\"\")","    return response_tuple[1]","    \"\"\"",""],"id":6}],[{"start":{"row":14,"column":42},"end":{"row":14,"column":43},"action":"remove","lines":["-"],"id":7},{"start":{"row":14,"column":41},"end":{"row":14,"column":42},"action":"remove","lines":["-"]},{"start":{"row":14,"column":40},"end":{"row":14,"column":41},"action":"remove","lines":["-"]},{"start":{"row":14,"column":39},"end":{"row":14,"column":40},"action":"remove","lines":["-"]},{"start":{"row":14,"column":38},"end":{"row":14,"column":39},"action":"remove","lines":["-"]},{"start":{"row":14,"column":37},"end":{"row":14,"column":38},"action":"remove","lines":["-"]},{"start":{"row":14,"column":36},"end":{"row":14,"column":37},"action":"remove","lines":["-"]},{"start":{"row":14,"column":35},"end":{"row":14,"column":36},"action":"remove","lines":["-"]},{"start":{"row":14,"column":34},"end":{"row":14,"column":35},"action":"remove","lines":["-"]},{"start":{"row":14,"column":33},"end":{"row":14,"column":34},"action":"remove","lines":["N"]},{"start":{"row":14,"column":32},"end":{"row":14,"column":33},"action":"remove","lines":["O"]},{"start":{"row":14,"column":31},"end":{"row":14,"column":32},"action":"remove","lines":["I"]},{"start":{"row":14,"column":30},"end":{"row":14,"column":31},"action":"remove","lines":["T"]},{"start":{"row":14,"column":29},"end":{"row":14,"column":30},"action":"remove","lines":["A"]},{"start":{"row":14,"column":28},"end":{"row":14,"column":29},"action":"remove","lines":["T"]},{"start":{"row":14,"column":27},"end":{"row":14,"column":28},"action":"remove","lines":["N"]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"remove","lines":["E"]},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"remove","lines":["M"]},{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"remove","lines":["E"]},{"start":{"row":14,"column":23},"end":{"row":14,"column":24},"action":"remove","lines":["L"]},{"start":{"row":14,"column":22},"end":{"row":14,"column":23},"action":"remove","lines":["P"]},{"start":{"row":14,"column":21},"end":{"row":14,"column":22},"action":"remove","lines":["M"]},{"start":{"row":14,"column":20},"end":{"row":14,"column":21},"action":"remove","lines":["I"]},{"start":{"row":14,"column":19},"end":{"row":14,"column":20},"action":"remove","lines":[" "]},{"start":{"row":14,"column":18},"end":{"row":14,"column":19},"action":"remove","lines":["K"]},{"start":{"row":14,"column":17},"end":{"row":14,"column":18},"action":"remove","lines":["C"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["O"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"remove","lines":["M"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["-"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["-"]},{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"remove","lines":["-"]},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"remove","lines":["-"]},{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"remove","lines":["-"]},{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["-"]},{"start":{"row":14,"column":8},"end":{"row":14,"column":9},"action":"remove","lines":["-"]},{"start":{"row":14,"column":7},"end":{"row":14,"column":8},"action":"remove","lines":["-"]},{"start":{"row":14,"column":6},"end":{"row":14,"column":7},"action":"remove","lines":["-"]}],[{"start":{"row":14,"column":5},"end":{"row":14,"column":6},"action":"remove","lines":[" "],"id":8},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["#"]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"remove","lines":["    "]},{"start":{"row":13,"column":33},"end":{"row":14,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":10},{"start":{"row":12,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":11,"column":0},"end":{"row":22,"column":1},"action":"insert","lines":["from resource_management.constants.exception_message import (","    USER_DOES_NOT_EXISTS,","    INVALID_PASSWORD",")","from resource_management.exceptions.exceptions import (","    UserDoesNotExist,","    InvalidPassword",")","from django_swagger_utils.drf_server.exceptions import (","    NotFound,","    BadRequest",")"],"id":11}],[{"start":{"row":20,"column":12},"end":{"row":20,"column":13},"action":"remove","lines":[","],"id":12},{"start":{"row":20,"column":11},"end":{"row":20,"column":12},"action":"remove","lines":["d"]},{"start":{"row":20,"column":10},"end":{"row":20,"column":11},"action":"remove","lines":["n"]},{"start":{"row":20,"column":9},"end":{"row":20,"column":10},"action":"remove","lines":["u"]},{"start":{"row":20,"column":8},"end":{"row":20,"column":9},"action":"remove","lines":["o"]},{"start":{"row":20,"column":7},"end":{"row":20,"column":8},"action":"remove","lines":["F"]},{"start":{"row":20,"column":6},"end":{"row":20,"column":7},"action":"remove","lines":["t"]},{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"remove","lines":["o"]},{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"remove","lines":["N"]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]},{"start":{"row":19,"column":56},"end":{"row":20,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":17,"column":18},"end":{"row":17,"column":19},"action":"remove","lines":["d"],"id":13},{"start":{"row":17,"column":17},"end":{"row":17,"column":18},"action":"remove","lines":["r"]},{"start":{"row":17,"column":16},"end":{"row":17,"column":17},"action":"remove","lines":["o"]},{"start":{"row":17,"column":15},"end":{"row":17,"column":16},"action":"remove","lines":["w"]},{"start":{"row":17,"column":14},"end":{"row":17,"column":15},"action":"remove","lines":["s"]},{"start":{"row":17,"column":13},"end":{"row":17,"column":14},"action":"remove","lines":["s"]},{"start":{"row":17,"column":12},"end":{"row":17,"column":13},"action":"remove","lines":["a"]},{"start":{"row":17,"column":11},"end":{"row":17,"column":12},"action":"remove","lines":["P"]},{"start":{"row":17,"column":10},"end":{"row":17,"column":11},"action":"remove","lines":["d"]},{"start":{"row":17,"column":9},"end":{"row":17,"column":10},"action":"remove","lines":["i"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"remove","lines":["l"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"remove","lines":["a"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"remove","lines":["v"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"remove","lines":["n"]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"remove","lines":["I"]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]},{"start":{"row":16,"column":21},"end":{"row":17,"column":0},"action":"remove","lines":["",""]},{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"remove","lines":[","]},{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"remove","lines":["t"]},{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"remove","lines":["s"]},{"start":{"row":16,"column":17},"end":{"row":16,"column":18},"action":"remove","lines":["i"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"remove","lines":["x"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"remove","lines":["E"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"remove","lines":["t"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"remove","lines":["o"]}],[{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"remove","lines":["N"],"id":14},{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"remove","lines":["s"]},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"remove","lines":["e"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"remove","lines":["o"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"remove","lines":["D"]}],[{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["N"],"id":15},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["o"]},{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":4},"end":{"row":16,"column":11},"action":"remove","lines":["UserNot"],"id":16},{"start":{"row":16,"column":4},"end":{"row":16,"column":26},"action":"insert","lines":["UserNotAllowedToUpdate"]}],[{"start":{"row":13,"column":19},"end":{"row":13,"column":20},"action":"remove","lines":["D"],"id":17},{"start":{"row":13,"column":18},"end":{"row":13,"column":19},"action":"remove","lines":["R"]},{"start":{"row":13,"column":17},"end":{"row":13,"column":18},"action":"remove","lines":["O"]},{"start":{"row":13,"column":16},"end":{"row":13,"column":17},"action":"remove","lines":["W"]},{"start":{"row":13,"column":15},"end":{"row":13,"column":16},"action":"remove","lines":["S"]},{"start":{"row":13,"column":14},"end":{"row":13,"column":15},"action":"remove","lines":["S"]},{"start":{"row":13,"column":13},"end":{"row":13,"column":14},"action":"remove","lines":["A"]},{"start":{"row":13,"column":12},"end":{"row":13,"column":13},"action":"remove","lines":["P"]},{"start":{"row":13,"column":11},"end":{"row":13,"column":12},"action":"remove","lines":["_"]},{"start":{"row":13,"column":10},"end":{"row":13,"column":11},"action":"remove","lines":["D"]},{"start":{"row":13,"column":9},"end":{"row":13,"column":10},"action":"remove","lines":["I"]},{"start":{"row":13,"column":8},"end":{"row":13,"column":9},"action":"remove","lines":["L"]},{"start":{"row":13,"column":7},"end":{"row":13,"column":8},"action":"remove","lines":["A"]},{"start":{"row":13,"column":6},"end":{"row":13,"column":7},"action":"remove","lines":["V"]},{"start":{"row":13,"column":5},"end":{"row":13,"column":6},"action":"remove","lines":["N"]},{"start":{"row":13,"column":4},"end":{"row":13,"column":5},"action":"remove","lines":["I"]},{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]},{"start":{"row":12,"column":25},"end":{"row":13,"column":0},"action":"remove","lines":["",""]},{"start":{"row":12,"column":24},"end":{"row":12,"column":25},"action":"remove","lines":[","]},{"start":{"row":12,"column":23},"end":{"row":12,"column":24},"action":"remove","lines":["S"]},{"start":{"row":12,"column":22},"end":{"row":12,"column":23},"action":"remove","lines":["T"]}],[{"start":{"row":12,"column":21},"end":{"row":12,"column":22},"action":"remove","lines":["S"],"id":18},{"start":{"row":12,"column":20},"end":{"row":12,"column":21},"action":"remove","lines":["I"]},{"start":{"row":12,"column":19},"end":{"row":12,"column":20},"action":"remove","lines":["X"]},{"start":{"row":12,"column":18},"end":{"row":12,"column":19},"action":"remove","lines":["E"]},{"start":{"row":12,"column":17},"end":{"row":12,"column":18},"action":"remove","lines":["_"]},{"start":{"row":12,"column":16},"end":{"row":12,"column":17},"action":"remove","lines":["T"]},{"start":{"row":12,"column":15},"end":{"row":12,"column":16},"action":"remove","lines":["O"]},{"start":{"row":12,"column":14},"end":{"row":12,"column":15},"action":"remove","lines":["N"]},{"start":{"row":12,"column":13},"end":{"row":12,"column":14},"action":"remove","lines":["_"]},{"start":{"row":12,"column":12},"end":{"row":12,"column":13},"action":"remove","lines":["S"]},{"start":{"row":12,"column":11},"end":{"row":12,"column":12},"action":"remove","lines":["E"]},{"start":{"row":12,"column":10},"end":{"row":12,"column":11},"action":"remove","lines":["O"]},{"start":{"row":12,"column":9},"end":{"row":12,"column":10},"action":"remove","lines":["D"]},{"start":{"row":12,"column":8},"end":{"row":12,"column":9},"action":"remove","lines":["_"]},{"start":{"row":12,"column":7},"end":{"row":12,"column":8},"action":"remove","lines":["R"]},{"start":{"row":12,"column":6},"end":{"row":12,"column":7},"action":"remove","lines":["E"]},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"remove","lines":["S"]},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["U"]}],[{"start":{"row":12,"column":4},"end":{"row":12,"column":30},"action":"insert","lines":["USER_NOT_ALLOWED_TO_UPDATE"],"id":19}],[{"start":{"row":41,"column":0},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":20}],[{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"insert","lines":["    "],"id":21}],[{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["t"],"id":22},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["r"]},{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["y"]},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":[":"]}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "],"id":23},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]},{"start":{"row":50,"column":0},"end":{"row":50,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":50,"column":9},"end":{"row":51,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":51,"column":0},"end":{"row":51,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":8},"action":"remove","lines":["    "],"id":25}],[{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"insert","lines":["e"],"id":26},{"start":{"row":51,"column":5},"end":{"row":51,"column":6},"action":"insert","lines":["x"]},{"start":{"row":51,"column":6},"end":{"row":51,"column":7},"action":"insert","lines":["c"]},{"start":{"row":51,"column":7},"end":{"row":51,"column":8},"action":"insert","lines":["e"]},{"start":{"row":51,"column":8},"end":{"row":51,"column":9},"action":"insert","lines":["p"]},{"start":{"row":51,"column":9},"end":{"row":51,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":51,"column":10},"end":{"row":51,"column":11},"action":"insert","lines":[" "],"id":27}],[{"start":{"row":51,"column":11},"end":{"row":51,"column":33},"action":"insert","lines":["UserNotAllowedToUpdate"],"id":28}],[{"start":{"row":51,"column":33},"end":{"row":51,"column":34},"action":"insert","lines":[":"],"id":29}],[{"start":{"row":51,"column":34},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":30},{"start":{"row":52,"column":0},"end":{"row":52,"column":8},"action":"insert","lines":["        "]},{"start":{"row":52,"column":8},"end":{"row":52,"column":9},"action":"insert","lines":["r"]},{"start":{"row":52,"column":9},"end":{"row":52,"column":10},"action":"insert","lines":["a"]},{"start":{"row":52,"column":10},"end":{"row":52,"column":11},"action":"insert","lines":["i"]},{"start":{"row":52,"column":11},"end":{"row":52,"column":12},"action":"insert","lines":["s"]},{"start":{"row":52,"column":12},"end":{"row":52,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":52,"column":13},"end":{"row":52,"column":14},"action":"insert","lines":[" "],"id":31},{"start":{"row":52,"column":14},"end":{"row":52,"column":15},"action":"insert","lines":["B"]},{"start":{"row":52,"column":15},"end":{"row":52,"column":16},"action":"insert","lines":["a"]},{"start":{"row":52,"column":16},"end":{"row":52,"column":17},"action":"insert","lines":["d"]}],[{"start":{"row":52,"column":14},"end":{"row":52,"column":17},"action":"remove","lines":["Bad"],"id":32},{"start":{"row":52,"column":14},"end":{"row":52,"column":24},"action":"insert","lines":["BadRequest"]}],[{"start":{"row":52,"column":24},"end":{"row":52,"column":26},"action":"insert","lines":["()"],"id":33}],[{"start":{"row":52,"column":25},"end":{"row":52,"column":26},"action":"insert","lines":["*"],"id":34}],[{"start":{"row":52,"column":26},"end":{"row":52,"column":52},"action":"insert","lines":["USER_NOT_ALLOWED_TO_UPDATE"],"id":35}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":43},"action":"remove","lines":["from .validator_class import ValidatorClass"],"id":36}],[{"start":{"row":2,"column":29},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":37}],[{"start":{"row":9,"column":27},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":39}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":43},"action":"insert","lines":["from .validator_class import ValidatorClass"],"id":40}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":25},"action":"remove","lines":["from resource_management.storages.storage_implementation import \\","    StorageImplementation"],"id":41},{"start":{"row":6,"column":0},"end":{"row":9,"column":33},"action":"insert","lines":["from resource_management.storages.user_storage_implementation import \\","    UserStorageImplementation","from resource_management.storages.resource_storage_implementation import \\","    ResourceStorageImplementation"]}],[{"start":{"row":13,"column":0},"end":{"row":22,"column":0},"action":"remove","lines":["from resource_management.constants.exception_message import (","    USER_NOT_ALLOWED_TO_UPDATE",")","from resource_management.exceptions.exceptions import (","    UserNotAllowedToUpdate",")","from django_swagger_utils.drf_server.exceptions import (","    BadRequest",")",""],"id":42}],[{"start":{"row":27,"column":4},"end":{"row":28,"column":41},"action":"remove","lines":["user_storage = StorageImplementation()","    presenter = PresenterImplementation()"],"id":43},{"start":{"row":27,"column":4},"end":{"row":29,"column":41},"action":"insert","lines":["user_storage = UserStorageImplementation()","    resource_storage = ResourceStorageImplementation()","    presenter = PresenterImplementation()"]}],[{"start":{"row":32,"column":34},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":44},{"start":{"row":33,"column":0},"end":{"row":33,"column":8},"action":"insert","lines":["        "]},{"start":{"row":33,"column":8},"end":{"row":33,"column":9},"action":"insert","lines":["r"]},{"start":{"row":33,"column":9},"end":{"row":33,"column":10},"action":"insert","lines":["e"]},{"start":{"row":33,"column":10},"end":{"row":33,"column":11},"action":"insert","lines":["s"]},{"start":{"row":33,"column":11},"end":{"row":33,"column":12},"action":"insert","lines":["o"]},{"start":{"row":33,"column":12},"end":{"row":33,"column":13},"action":"insert","lines":["u"]},{"start":{"row":33,"column":13},"end":{"row":33,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":14},"action":"remove","lines":["resour"],"id":45},{"start":{"row":33,"column":8},"end":{"row":33,"column":24},"action":"insert","lines":["resource_storage"]}],[{"start":{"row":33,"column":24},"end":{"row":33,"column":25},"action":"insert","lines":["="],"id":46},{"start":{"row":33,"column":25},"end":{"row":33,"column":26},"action":"insert","lines":["r"]},{"start":{"row":33,"column":26},"end":{"row":33,"column":27},"action":"insert","lines":["e"]},{"start":{"row":33,"column":27},"end":{"row":33,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":33,"column":25},"end":{"row":33,"column":28},"action":"remove","lines":["res"],"id":47},{"start":{"row":33,"column":25},"end":{"row":33,"column":41},"action":"insert","lines":["resource_storage"]}],[{"start":{"row":33,"column":41},"end":{"row":33,"column":42},"action":"insert","lines":[","],"id":48}],[{"start":{"row":38,"column":50},"end":{"row":38,"column":51},"action":"remove","lines":["s"],"id":49}],[{"start":{"row":37,"column":7},"end":{"row":37,"column":8},"action":"remove","lines":[":"],"id":50},{"start":{"row":37,"column":6},"end":{"row":37,"column":7},"action":"remove","lines":["y"]},{"start":{"row":37,"column":5},"end":{"row":37,"column":6},"action":"remove","lines":["r"]},{"start":{"row":37,"column":4},"end":{"row":37,"column":5},"action":"remove","lines":["t"]},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":38,"column":23},"end":{"row":38,"column":24},"action":"remove","lines":[" "],"id":51},{"start":{"row":38,"column":22},"end":{"row":38,"column":23},"action":"remove","lines":["="]},{"start":{"row":38,"column":21},"end":{"row":38,"column":22},"action":"remove","lines":[" "]},{"start":{"row":38,"column":20},"end":{"row":38,"column":21},"action":"remove","lines":["t"]},{"start":{"row":38,"column":19},"end":{"row":38,"column":20},"action":"remove","lines":["c"]},{"start":{"row":38,"column":18},"end":{"row":38,"column":19},"action":"remove","lines":["i"]},{"start":{"row":38,"column":17},"end":{"row":38,"column":18},"action":"remove","lines":["d"]},{"start":{"row":38,"column":16},"end":{"row":38,"column":17},"action":"remove","lines":["_"]},{"start":{"row":38,"column":15},"end":{"row":38,"column":16},"action":"remove","lines":["e"]},{"start":{"row":38,"column":14},"end":{"row":38,"column":15},"action":"remove","lines":["c"]},{"start":{"row":38,"column":13},"end":{"row":38,"column":14},"action":"remove","lines":["r"]},{"start":{"row":38,"column":12},"end":{"row":38,"column":13},"action":"remove","lines":["u"]},{"start":{"row":38,"column":11},"end":{"row":38,"column":12},"action":"remove","lines":["o"]},{"start":{"row":38,"column":10},"end":{"row":38,"column":11},"action":"remove","lines":["s"]},{"start":{"row":38,"column":9},"end":{"row":38,"column":10},"action":"remove","lines":["e"]},{"start":{"row":38,"column":8},"end":{"row":38,"column":9},"action":"remove","lines":["r"]}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"remove","lines":["    "],"id":52},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"remove","lines":["    "]},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"remove","lines":["    "]},{"start":{"row":41,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "]},{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "]},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"remove","lines":["    "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":46,"column":4},"end":{"row":47,"column":53},"action":"remove","lines":["except UserNotAllowedToUpdate:","        raise BadRequest(*USER_NOT_ALLOWED_TO_UPDATE)"],"id":53},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"remove","lines":["    "]},{"start":{"row":45,"column":5},"end":{"row":46,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":47,"column":34},"end":{"row":47,"column":35},"action":"remove","lines":["t"],"id":54},{"start":{"row":47,"column":33},"end":{"row":47,"column":34},"action":"remove","lines":["c"]},{"start":{"row":47,"column":32},"end":{"row":47,"column":33},"action":"remove","lines":["i"]},{"start":{"row":47,"column":31},"end":{"row":47,"column":32},"action":"remove","lines":["d"]},{"start":{"row":47,"column":30},"end":{"row":47,"column":31},"action":"remove","lines":["_"]},{"start":{"row":47,"column":29},"end":{"row":47,"column":30},"action":"remove","lines":["e"]},{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"remove","lines":["c"]},{"start":{"row":47,"column":27},"end":{"row":47,"column":28},"action":"remove","lines":["r"]},{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"remove","lines":["u"]},{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"remove","lines":["o"]},{"start":{"row":47,"column":24},"end":{"row":47,"column":25},"action":"remove","lines":["s"]},{"start":{"row":47,"column":23},"end":{"row":47,"column":24},"action":"remove","lines":["e"]}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"remove","lines":["r"],"id":55}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":24},"action":"insert","lines":["{}"],"id":56}],[{"start":{"row":47,"column":23},"end":{"row":47,"column":25},"action":"insert","lines":["\"\""],"id":57}],[{"start":{"row":47,"column":24},"end":{"row":47,"column":25},"action":"insert","lines":["r"],"id":58},{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"insert","lines":["e"]},{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"insert","lines":["s"]},{"start":{"row":47,"column":27},"end":{"row":47,"column":28},"action":"insert","lines":["p"]},{"start":{"row":47,"column":28},"end":{"row":47,"column":29},"action":"insert","lines":["o"]},{"start":{"row":47,"column":29},"end":{"row":47,"column":30},"action":"insert","lines":["n"]},{"start":{"row":47,"column":30},"end":{"row":47,"column":31},"action":"insert","lines":["s"]},{"start":{"row":47,"column":31},"end":{"row":47,"column":32},"action":"insert","lines":["e"]}],[{"start":{"row":47,"column":33},"end":{"row":47,"column":34},"action":"insert","lines":[":"],"id":59}],[{"start":{"row":47,"column":34},"end":{"row":47,"column":35},"action":"insert","lines":[" "],"id":60}],[{"start":{"row":47,"column":35},"end":{"row":47,"column":37},"action":"insert","lines":["\"\""],"id":61}],[{"start":{"row":47,"column":36},"end":{"row":47,"column":37},"action":"insert","lines":["u"],"id":62},{"start":{"row":47,"column":37},"end":{"row":47,"column":38},"action":"insert","lines":["p"]},{"start":{"row":47,"column":38},"end":{"row":47,"column":39},"action":"insert","lines":["d"]},{"start":{"row":47,"column":39},"end":{"row":47,"column":40},"action":"insert","lines":["a"]},{"start":{"row":47,"column":40},"end":{"row":47,"column":41},"action":"insert","lines":["t"]},{"start":{"row":47,"column":41},"end":{"row":47,"column":42},"action":"insert","lines":["e"]},{"start":{"row":47,"column":42},"end":{"row":47,"column":43},"action":"insert","lines":["d"]}],[{"start":{"row":47,"column":43},"end":{"row":47,"column":44},"action":"insert","lines":[" "],"id":63},{"start":{"row":47,"column":44},"end":{"row":47,"column":45},"action":"insert","lines":["s"]},{"start":{"row":47,"column":45},"end":{"row":47,"column":46},"action":"insert","lines":["u"]},{"start":{"row":47,"column":46},"end":{"row":47,"column":47},"action":"insert","lines":["c"]},{"start":{"row":47,"column":47},"end":{"row":47,"column":48},"action":"insert","lines":["c"]},{"start":{"row":47,"column":48},"end":{"row":47,"column":49},"action":"insert","lines":["e"]},{"start":{"row":47,"column":49},"end":{"row":47,"column":50},"action":"insert","lines":["s"]},{"start":{"row":47,"column":50},"end":{"row":47,"column":51},"action":"insert","lines":["s"]}],[{"start":{"row":47,"column":51},"end":{"row":47,"column":52},"action":"insert","lines":["f"],"id":64},{"start":{"row":47,"column":52},"end":{"row":47,"column":53},"action":"insert","lines":["u"]},{"start":{"row":47,"column":53},"end":{"row":47,"column":54},"action":"insert","lines":["l"]},{"start":{"row":47,"column":54},"end":{"row":47,"column":55},"action":"insert","lines":["l"]},{"start":{"row":47,"column":55},"end":{"row":47,"column":56},"action":"insert","lines":["y"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":17,"column":0},"end":{"row":17,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1591182705045,"hash":"4a40e8f0a05a4f0650c3cd1f7b2d93bc9911695f"}