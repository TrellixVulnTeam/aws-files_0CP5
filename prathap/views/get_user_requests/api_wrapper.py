from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_user_requests_interactor import \
    GetUserRequestsInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    offset = kwargs['request_query_params']['offset']
    limit = kwargs['request_query_params']['limit']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetUserRequestsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    requests_dict = interactor.get_user_requests(
        offset=offset,
        limit=limit
    )
    data = json.dumps(requests_dict)
    response = HttpResponse(data, status=200)
    return response
