from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.get_admin_resources_interactor import \
    GetAdminResourcesInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from resource_management.presenters.presenter_implementation import \
    PresenterImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    user_storage = StorageImplementation()
    presenter = PresenterImplementation()

    interactor = GetAdminResourcesInteractor(
        user_storage=user_storage,
        presenter=presenter
    )

    resource_dict_list = interactor.get_admin_resources()

    data = json.dumps(resource_dict_list)
    response = HttpResponse(data, status=200)
    return response
