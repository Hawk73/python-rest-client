import requests
import json
import errors
from requests.auth import HTTPBasicAuth


class ClientClass:
    def __init__(self, base_url, username=None, password=None, verify=True, custom_headers=None, wo_trailing=False):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify = verify
        self.custom_headers = custom_headers
        self.wo_trailing = wo_trailing

    def get_resources(self, resources_name, params=None, url_format='/{:s}/'):
        url = self._make_url(url_format.format(resources_name))
        response = self._make_get_request(url, params)
        self._log_response(response)
        return self.decoded_response(response)

    def get(self, resources_name, resource_id, url_format='/{:s}/{:d}/'):
        url = self._make_url(url_format.format(resources_name, int(resource_id)))
        response = self._make_get_request(url)
        self._log_response(response)
        return self.decoded_response(response)

    def post(self, resources_name, params=None, data=None, url_format='/{:s}/'):
        url = self._make_url(url_format.format(resources_name))
        response = self._make_post_request(url, params, data)
        self._log_response(response)
        return self.decoded_response(response)

    def put(self, resources_name, resource_id, params=None, data=None, url_format='/{:s}/{:d}/'):
        url = self._make_url(url_format.format(resources_name, int(resource_id)))
        response = self._make_put_request(url, params)
        self._log_response(response)
        return self.decoded_response(response)

    def delete(self, resources_name, resource_id, url_format='/{:s}/{:d}/'):
        url = self._make_url(url_format.format(resources_name, int(resource_id)))
        response = self._make_delete_request(url)
        self._log_response(response)
        return self.decoded_response(response)

    def _make_url(self, path):
        url = self.base_url + path
        if self.wo_trailing and url[-1] == '/':
            return url[:-1]
        return url

    def _make_get_request(self, url, params=None):
        return self._make_request('get', url, params)

    def _make_post_request(self, url, params=None, data=None):
        return self._make_request('post', url, params, data)

    def _make_put_request(self, url, params=None, data=None):
        return self._make_request('put', url, params, data)

    def _make_delete_request(self, url):
        return self._make_request('delete', url, None)

    def _make_request(self, method, url, params=None, data=None):
        kwargs = {}
        if self.username is not None:
            kwargs['auth'] = HTTPBasicAuth(self.username, self.password)
        self._log_request(method, url, params, data, self.custom_headers)
        if data:
            response = requests.request(method, url, headers=self.custom_headers, params=params, data=json.dumps(data), verify=verify, **kwargs)
        else:
            response = requests.request(method, url, headers=self.custom_headers, params=params, verify=verify, **kwargs)
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
    def _log_request(method, url, params, data, headers):
        print('\nMaking {:s} request to url="{:s}" with headers:'.format(method, url))
        print(headers)
        print(' and params:')
        print(params)
        print(' and data:')
        print(data)

    @staticmethod
    def _log_response(response):
        print('\nReceived response: status_code="{:d}" content="{:s}"'.format(response.status_code, response.content))
