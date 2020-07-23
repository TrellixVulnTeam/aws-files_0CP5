from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.delete_items_interactor import \
    DeleteItemsInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass
from resource_management.constants.exception_message import INVALID_ITEM
from resource_management.exceptions.exceptions import InvalidItem
from django_swagger_utils.drf_server.exceptions import NotFound


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    requested_data = kwargs['request_data']
    item_ids = requested_data['item_ids']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = DeleteItemsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    try:
        interactor.delete_items(
            item_ids=item_ids
        )
    except InvalidItem:
        raise NotFound(*INVALID_ITEM)

    data = json.dumps({'response': 'deleted successfully'})
    return HttpResponse(data, status=200)
