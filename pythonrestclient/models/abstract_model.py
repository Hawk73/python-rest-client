from collection_class import CollectionClass
from pythonrestclient.service_factory import ServiceFactory


class AbstractModel:
    def __init__(self, attributes = None):
        self.attributes = attributes

    def attributes(self):
        return self.attributes

    @classmethod
    def all(cls):
        return cls.filter(None)

    # TODO: add tests
    @classmethod
    def filter(cls, params):
        response = ServiceFactory.api_client.get_resources(cls.resources_name(), params)
        items = list(map(lambda attributes: cls(attributes), response))
        return CollectionClass(items, params)

    @classmethod
    def get(cls, resource_id):
        response = ServiceFactory.api_client.get(cls.resources_name(), resource_id)
        return cls(response)

    @classmethod
    def create(cls, attributes):
        cls._validate_presence_of_required_attributes(attributes)
        response = ServiceFactory.api_client.post(cls.resources_name(), attributes)
        if response['id']:
            merged_attributes = cls.merge_two_dicts(attributes, response)
            return cls(merged_attributes)
        else:
            return None

    # TODO: add tests
    def update(self, new_attributes):
        if self.__class__.update_by_id(self.attributes['id'], new_attributes):
            self.attributes = self.merge_two_dicts(self.attributes, new_attributes)
            return True
        else:
            return False

    @classmethod
    def update_by_id(cls, resource_id, new_attributes):
        response = ServiceFactory.api_client.put(cls.resources_name(), resource_id, new_attributes)
        return response['id'] == resource_id

    def delete(self):
        # TODO: check ID
        return self.__class__.delete_by_id(self.attributes['id'])

    @classmethod
    def delete_by_id(cls, resource_id):
        response = ServiceFactory.api_client.delete(cls.resources_name(), resource_id)
        return response == {}

    @classmethod
    def resources_name(cls):
        raise NotImplementedError("AbstractModel does not have _resources_name!")

    @classmethod
    def _validate_presence_of_required_attributes(cls, attributes):
        # TODO: implement _validate_presence_of_required_params
        pass

    @staticmethod
    def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z
