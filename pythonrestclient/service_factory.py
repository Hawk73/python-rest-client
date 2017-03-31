from api.client_class import ClientClass


class ServiceFactory(object):
    api_client = None

    @classmethod
    def init_api_client(cls, base_url, username=None, password=None):
        cls.api_client = ClientClass(base_url, username, password)
