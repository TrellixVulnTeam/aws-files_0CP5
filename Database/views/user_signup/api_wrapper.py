from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from resource_management.interactors.signup_interactor import \
    SignupInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    requested_data = kwargs['request_data']
    username = requested_data['username']
    password = requested_data['password']

    user_storage = StorageImplementation()
    oauth2_storage = OAuth2SQLStorage()
    presenter = PresenterImplementation()

    interactor = SignupInteractor(
        user_storage=user_storage,
        oauth2_storage=oauth2_storage,
        presenter=presenter
    )
    access_token = interactor.signup(
        username=username,
        password=password
    )
    data = json.dumps(access_token)
    response = HttpResponse(data, status=201)
    return response



    """
    try:
        from resource_management.views.user_signup.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from resource_management.views.user_signup.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from resource_management.views.user_signup.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="resource_management", test_case=test_case,
        operation_name="user_signup",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """
