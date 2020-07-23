from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from raven.utils import json
from resource_management.interactors.user_profile_update_interactor import \
    UserProfileUpdateInteractor
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
    username = requested_data['username']
    email = requested_data['email']
    job_role = requested_data['job_role']
    department = requested_data['department']
    gender = requested_data['gender']
    profile_pic = requested_data['profile_pic']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = UserProfileUpdateInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    user_dict = interactor.user_profile_update(
        user_id=user_id,
        username=username,
        email=email,
        job_role=job_role,
        department=department,
        gender=gender,
        profile_pic=profile_pic
    )

    data = json.dumps(user_dict)
    response = HttpResponse(data, status=200)
    return response

    """
    try:
        from resource_management.views.user_profile_update.tests.test_case_01 \
            import TEST_CASE as test_case
    except ImportError:
        from resource_management.views.user_profile_update.tests.test_case_01 \
            import test_case

    from django_swagger_utils.drf_server.utils.server_gen.mock_response \
        import mock_response
    try:
        from resource_management.views.user_profile_update.request_response_mocks \
            import RESPONSE_200_JSON
    except ImportError:
        RESPONSE_200_JSON = ''
    response_tuple = mock_response(
        app_name="resource_management", test_case=test_case,
        operation_name="user_profile_update",
        kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
        group_name="")
    return response_tuple[1]
    """
