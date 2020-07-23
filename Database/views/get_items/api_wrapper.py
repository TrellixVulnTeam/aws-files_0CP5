from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from resource_management.interactors.get_items_interactor import \
    GetItemsInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    resource_id = kwargs['resource_id']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetItemsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    items_list = interactor.get_items(
        resource_id=resource_id
    )
    data = json.dumps(items_list)
    response = HttpResponse(data, status=200)
    return response

    """
    try:
        from resource_management.views.get_items.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from resource_management.views.get_items.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from resource_management.views.get_items.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="resource_management", test_case=test_case,
        operation_name="get_items",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """
