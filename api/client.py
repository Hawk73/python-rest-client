import requests
import json


class Client:
    def __init__(self, base_url, user, login):
        self.base_url = base_url
        self.user = user
        self.login = login

    def get_lists(self, resources_name):
        url = self._make_url('/{:s}/'.format(resources_name))
        self._log_request(url)
        response = requests.get(url)
        self._log_response(response)
        return self.decoded_response(response)

    def get(self, resources_name, resource_id):
        url = self._make_url('/{:s}/{:d}/'.format(resources_name, resource_id))
        self._log_request(url)
        response = requests.get(url)
        self._log_response(response)
        return self.decoded_response(response)

    def post(self, resources_name, data):
        pass

    def put(self, resources_name, data):
        pass

    def delete(self, resources_name, id):
        pass

    def _make_url(self, path):
        return self.base_url + path

    @staticmethod
    def decoded_response(response):
        return json.loads(response.text)

    @staticmethod
    def _log_request(url):
        print('Making request to url="{:s}"'.format(url))

    @staticmethod
    def _log_response(response):
        print('Received response: status_code="{:d}" content="{:s}"'.format(response.status_code, response.content))
