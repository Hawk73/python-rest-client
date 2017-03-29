class AbstractModel:
    def __init__(self, api_client):
        # TODO: convert to class variable
        self.api_client = api_client

    # TODO: convert to static
    def get_lists(self):
        # TODO: return CollectionClass
        return self.api_client.get_lists(self._resources_name())

    # TODO: convert to static
    def get(self, resource_id):
        # TODO: return instance of model
        return self.api_client.get(self._resources_name(), resource_id)

    # TODO: convert to static
    def create(self, attributes):
        self._validate_presence_of_required_attributes(attributes)
        response = self.api_client.post(self._resources_name(), attributes)
        # TODO: return instance of model
        return response['id']

    # TODO: create two methods static and for instance
    def update(self, resource_id, data):
        response = self.api_client.put(self._resources_name(), resource_id, data)
        return response['id'] == resource_id

    # TODO: create two methods static and for instance
    def delete(self, resource_id):
        response = self.api_client.delete(self._resources_name(), resource_id)
        return response == {}

    def _resources_name(self):
        raise NotImplementedError("AbstractModel does not have _resources_name!")

    # TODO: implement _validate_presence_of_required_params
    def _validate_presence_of_required_attributes(self, attributes):
        pass
