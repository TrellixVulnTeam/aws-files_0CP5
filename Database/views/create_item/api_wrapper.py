from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from resource_management.interactors.create_item_interactor import \
    CreateItemInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    resource_id = kwargs['resource_id']
    requested_data = kwargs['request_data']
    title = requested_data['title']
    description = requested_data['description']
    link = requested_data['link']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = CreateItemInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    item_dict = interactor.create_item(
        resource_id=resource_id,
        title=title,
        description=description,
        link=link
    )
    data = json.dumps(item_dict)
    response = HttpResponse(data, status=200)
    return response

    """
    try:
        from resource_management.views.create_item.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from resource_management.views.create_item.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from resource_management.views.create_item.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="resource_management", test_case=test_case,
        operation_name="create_item",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """
