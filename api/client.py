import requests
import json
import errors
from requests.auth import HTTPBasicAuth


class Client:
    def __init__(self, base_url, username = None, password = None):
        self.base_url = base_url
        self.username = username
        self.password = password

    def get_lists(self, resources_name):
        url = self._make_url('/{:s}/'.format(resources_name))
        self._log_request(url)
        response = self._make_get_request(url)
        self._log_response(response)
        return self.decoded_response(response)

    def get(self, resources_name, resource_id):
        url = self._make_url('/{:s}/{:d}/'.format(resources_name, resource_id))
        self._log_request(url)
        response = self._make_get_request(url)
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

    def _make_get_request(self, url):
        kwargs = {}
        if self.username is not None:
            kwargs['auth'] = HTTPBasicAuth(self.username, self.password)
        response = requests.get(url, None, **kwargs)
        self._check_response(response)
        return response

    def _check_response(self, response):
        if response.status_code == 403 :
            raise errors.UnauthorizedError()

    @staticmethod
    def decoded_response(response):
        return json.loads(response.text)

    @staticmethod
    def _log_request(url):
        print('Making request to url="{:s}"'.format(url))

    @staticmethod
    def _log_response(response):
        print('Received response: status_code="{:d}" content="{:s}"'.format(response.status_code, response.content))
