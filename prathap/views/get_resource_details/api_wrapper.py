from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_resource_details_interactor import \
    GetResourceDetailsInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass
from resource_management.constants.exception_message import INVALID_RESOURCE
from resource_management.exceptions.exceptions import InvalidResource
from django_swagger_utils.drf_server.exceptions import NotFound


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    resource_id = kwargs['resource_id']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetResourceDetailsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    try:
        resource_dict = interactor.get_resource_details(
            resource_id=resource_id
        )
    except InvalidResource:
        raise NotFound(*INVALID_RESOURCE)

    data = json.dumps(resource_dict)
    response = HttpResponse(data, status=200)
    return response
