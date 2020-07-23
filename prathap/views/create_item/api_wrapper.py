from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.create_item_interactor import \
    CreateItemInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

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
