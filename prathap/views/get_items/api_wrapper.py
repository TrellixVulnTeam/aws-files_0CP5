from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_items_interactor import \
    GetItemsInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

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
