from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_item_users_interactor import \
    GetItemUsersInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    item_id = kwargs['item_id']

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetItemUsersInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    users_dict = interactor.get_item_users(
        item_id=item_id
    )
    data = json.dumps(users_dict)
    response = HttpResponse(data, status=200)
    return response
