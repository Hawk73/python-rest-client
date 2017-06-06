from api.client_class import ClientClass


class ServiceFactory(object):
    api_client = None

    @classmethod
    def init_api_client(cls, base_url, username=None, password=None, custom_headers=None, wo_trailing=False):
        cls.api_client = ClientClass(base_url, username, password, custom_headers, wo_trailing)
