import requests

class ApiClient:
    def __init__(self, base_url, user, login):
        self.base_url = base_url
        self.user = user
        self.login = login

    def get_lists(self, resources_name):
        url = self._make_url('/{:s}/'.format(resources_name))
        return requests.get(url)

    def get_lists(self, resources_name, resource_id):
        url = self._make_url('/{:s}/{:d}/'.format(resources_name, resource_id))
        return requests.get(url)

    def post(self, resources_name, data):
        pass

    def put(self, resources_name, data):
        pass

    def delete(self, resources_name, id):
        pass

    def _make_url(self, path):
        return self.base_url + path
