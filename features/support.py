BASE_URL = 'http://localhost'
# TODO: create factory
JSON_RESPONSE_FOR_GET_RESOURCES = [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis"
  }
]
TEST_ID = 1
JSON_RESPONSE_FOR_GET_RESOURCE = {
    "userId": 1,
    "id": TEST_ID,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas"
}
NEW_RESOURCE_DATA = {
    "userId": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas"
}
ID_JSON = {
    "id": TEST_ID
}
JSON_RESPONSE_FOR_DELETE_RESOURCE = { }


def stub_get_resources_request(mocker, status_code=200):
    kwargs = {
        'status_code': status_code,
    }
    if status_code == 200:
        kwargs['json'] = JSON_RESPONSE_FOR_GET_RESOURCES
    mocker.get('{:s}/posts/'.format(BASE_URL), **kwargs)


def stub_get_resource_request(mocker, resource_id, status_code=200):
    kwargs = {
        'status_code': status_code,
    }
    if status_code == 200:
        kwargs['json'] = JSON_RESPONSE_FOR_GET_RESOURCE
    mocker.get('{:s}/posts/{:d}/'.format(BASE_URL, resource_id), **kwargs)


def stub_create_resource_request(mocker, status_code=200):
    kwargs = {
        'status_code': status_code,
    }
    if status_code == 200:
        kwargs['json'] = ID_JSON
    mocker.post('{:s}/posts/'.format(BASE_URL), **kwargs)


def stub_update_resource_request(mocker, resource_id, status_code=200):
    kwargs = {
        'status_code': status_code,
    }
    if status_code == 200:
        kwargs['json'] = ID_JSON
    mocker.put('{:s}/posts/{:d}/'.format(BASE_URL, resource_id), **kwargs)


def stub_delete_resource_request(mocker, resource_id, status_code=200):
    kwargs = {
        'status_code': status_code,
    }
    if status_code == 200:
        kwargs['json'] = JSON_RESPONSE_FOR_DELETE_RESOURCE
    mocker.delete('{:s}/posts/{:d}/'.format(BASE_URL, resource_id), **kwargs)
