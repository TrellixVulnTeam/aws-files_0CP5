from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_item_details_interactor import \
    GetItemDetailsInteractor
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

    item_id = kwargs['item_id']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetItemDetailsInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    try:
        item_dict = interactor.get_item_details(
            item_id=item_id
        )
    except InvalidItem:
        raise NotFound(*INVALID_ITEM)

    data = json.dumps(item_dict)
    response = HttpResponse(data, status=200)
    return response
