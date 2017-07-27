import requests
import json
import sys
import errors
import logging
from requests.auth import HTTPBasicAuth


class ClientClass:
    def __init__(self, base_url, username=None, password=None, verify=True, client_cert=None, custom_headers=None, wo_trailing=False, log_level=logging.CRITICAL, log_loc=sys.stdout):
        self.base_url = base_url
        self.username = username
        self.password = password
        self.verify = verify
        self.client_cert = client_cert
        self.custom_headers = custom_headers
        self.wo_trailing = wo_trailing

        # Set up logging
        # Set up the global logger to stdout
        self.logger = logging.getLogger(__name__)
        ch = logging.StreamHandler(log_loc)
        self.logger.setLevel(log_level)
        ch.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

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
        if data is not None:
            kwargs['data'] = json.dumps(data)
        if self.client_cert is not None:
            kwargs['cert'] = self.client_cert
        if self.verify:
            kwargs['verify'] = self.verify
   
        self._log_request(method, url, params, data)
        response = requests.request(method, url, headers=self.custom_headers, params=params, **kwargs)

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

    def _log_request(self, method, url, params, data):
        self.logger.debug('\nMaking {:s} request to url="{:s}"'.format(method, url))
        self.logger.debug('-Client Cert: ')
        self.logger.debug(self.client_cert)
        self.logger.debug('-Headers: ')
        self.logger.debug(self.custom_headers)
        self.logger.debug('-Params: ')
        self.logger.debug(params)
        self.logger.debug('-Data:')
        self.logger.debug(data)

    def _log_response(self, response):
        self.logger.debug('\nReceived response: status_code="{:d}" content="{:s}"'.format(response.status_code, response.content))
