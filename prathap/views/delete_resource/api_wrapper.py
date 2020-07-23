from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from raven.utils import json
from resource_management.interactors.delete_resource_interactor import \
    DeleteResourceInteractor
from resource_management.storages.storage_implementation import \
    StorageImplementation
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    resource_id = kwargs['resource_id']

    user_storage = StorageImplementation()

    interactors = DeleteResourceInteractor(
        user_storage=user_storage
    )

    interactors.delete_resource(
        resource_id=resource_id
    )
    data = json.dumps({'response': 'deleted successfully'})
    return HttpResponse(data, status=200)
