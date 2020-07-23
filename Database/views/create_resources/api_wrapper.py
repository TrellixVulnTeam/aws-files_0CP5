from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from resource_name.interactors.create_resource_interactor import \
    CreateResourcesInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    user = kwargs['user']
    user_id = user.id
    requested_data = kwargs['request_data']
    resource_name = requested_data['resource_name']
    description = requested_data['description']
    link = requested_data['link']
    thumbnail = requested_data['thumbnail']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = CreateResourcesInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    resource_dict = interactor.create_resources(
        user_id=user_id,
        resource_name=resource_name,
        description=description,
        link=link,
        thumbnail=thumbnail
    )

    data = json.dumps(resource_dict)
    response = HttpResponse(data, status=201)
    return response

    """
    try:
        from resource_management.views.create_resources.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from resource_management.views.create_resources.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from resource_management.views.create_resources.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="resource_management", test_case=test_case,
        operation_name="create_resources",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """
