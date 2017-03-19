class AbstractModel:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_lists(self):
        return self.api_client.get_lists(self.resources_name)

    def get(self, resource_id):
        return self.api_client.get(self.resources_name, resource_id)

    def post(self, data):
        return self.api_client.post(self.resources_name, data)

    def put(self, data):
        return self.api_client.post(self.resources_name, data)

    def delete(self, id):
        return self.api_client.delete(self.resources_name, id)

    def resources_name(self):
        raise NotImplementedError("AbstractModel does not have resources_name!")
