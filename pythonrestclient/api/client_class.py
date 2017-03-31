import requests
import json
import errors
from requests.auth import HTTPBasicAuth


class ClientClass:
    def __init__(self, base_url, username=None, password=None):
        self.base_url = base_url
        self.username = username
        self.password = password

    def get_lists(self, resources_name):
        url = self._make_url('/{:s}/'.format(resources_name))
        response = self._make_get_request(url)
        self._log_response(response)
        return self.decoded_response(response)

    def get(self, resources_name, resource_id):
        url = self._make_url('/{:s}/{:d}/'.format(resources_name, int(resource_id)))
        response = self._make_get_request(url)
        self._log_response(response)
        return self.decoded_response(response)

    def post(self, resources_name, params):
        url = self._make_url('/{:s}/'.format(resources_name))
        response = self._make_post_request(url, params)
        self._log_response(response)
        return self.decoded_response(response)

    def put(self, resources_name, resource_id, params):
        url = self._make_url('/{:s}/{:d}/'.format(resources_name, int(resource_id)))
        response = self._make_put_request(url, params)
        self._log_response(response)
        return self.decoded_response(response)

    def delete(self, resources_name, resource_id):
        url = self._make_url('/{:s}/{:d}/'.format(resources_name, int(resource_id)))
        response = self._make_delete_request(url)
        self._log_response(response)
        return self.decoded_response(response)

    def _make_url(self, path):
        return self.base_url + path

    def _make_get_request(self, url):
        return self._make_request('get', url, None)

    def _make_post_request(self, url, params):
        return self._make_request('post', url, params)

    def _make_put_request(self, url, params):
        return self._make_request('put', url, params)

    def _make_delete_request(self, url):
        return self._make_request('delete', url, None)

    def _make_request(self, method, url, params):
        kwargs = {}
        if self.username is not None:
            kwargs['auth'] = HTTPBasicAuth(self.username, self.password)
        self._log_request(method, url, params)
        response = requests.request(method, url, params=params, **kwargs)
        self._check_response(response)
        return response

    @staticmethod
    def _check_response(response):
        if response.status_code == 403:
            raise errors.UnauthorizedError()
        if response.status_code == 404:
            raise errors.NotFoundError()

    @staticmethod
    def decoded_response(response):
        return json.loads(response.text)

    # TODO: print log to file

    @staticmethod
    def _log_request(method, url, params):
        print('\nMaking {:s} request to url="{:s}" with data:'.format(method, url))
        print(params)

    @staticmethod
    def _log_response(response):
        print('\nReceived response: status_code="{:d}" content="{:s}"'.format(response.status_code, response.content))
