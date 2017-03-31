from collection_class import CollectionClass
from pythonrestclient.service_factory import ServiceFactory


class AbstractModel:
    def __init__(self):
        pass

    # TODO: convert to static
    def get_lists(self):
        items = ServiceFactory.api_client.get_lists(self._resources_name())
        return CollectionClass(items)

    # TODO: convert to static
    def get(self, resource_id):
        # TODO: return instance of model
        return ServiceFactory.api_client.get(self._resources_name(), resource_id)

    # TODO: convert to static
    def create(self, attributes):
        self._validate_presence_of_required_attributes(attributes)
        response = ServiceFactory.api_client.post(self._resources_name(), attributes)
        # TODO: return instance of model
        return response['id']

    # TODO: create two methods static and for instance
    def update(self, resource_id, attributes):
        response = ServiceFactory.api_client.put(self._resources_name(), resource_id, attributes)
        return response['id'] == resource_id

    # TODO: create two methods static and for instance
    def delete(self, resource_id):
        response = ServiceFactory.api_client.delete(self._resources_name(), resource_id)
        return response == {}

    def _resources_name(self):
        raise NotImplementedError("AbstractModel does not have _resources_name!")

    # TODO: implement _validate_presence_of_required_params
    def _validate_presence_of_required_attributes(self, attributes):
        pass
