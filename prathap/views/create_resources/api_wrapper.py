from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.create_resource_interactor import \
    CreateResourcesInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass
from resource_management.exceptions.exceptions import UserNotAllowedToCreate
from resource_management.constants.exception_message import (
    USER_NOT_ALLOWED_TO_CREATE
)
from django_swagger_utils.drf_server.exceptions import (
    BadRequest
)


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

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

    try:
        resource_dict = interactor.create_resources(
            user_id=user_id,
            resource_name=resource_name,
            description=description,
            link=link,
            thumbnail=thumbnail
        )
    except UserNotAllowedToCreate:
        raise BadRequest(*USER_NOT_ALLOWED_TO_CREATE)

    data = json.dumps(resource_dict)
    response = HttpResponse(data, status=201)
    return response
