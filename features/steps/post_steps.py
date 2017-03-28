from behave import *
from hamcrest import *
import api.client
import api.errors
import models.post
import requests_mock


BASE_URL = 'http://localhost'
# TODO: create factory
RESOURCES_JSON = [
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
RESOURCE_JSON = {
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


def stub_get_resources_request(mocker, status_code=200):
    kwargs = {
        'status_code': status_code,
    }
    if status_code == 200:
        kwargs['json'] = RESOURCES_JSON
    mocker.get('{:s}/posts/'.format(BASE_URL), **kwargs)


def stub_get_resource_request(mocker, resource_id, status_code=200):
    kwargs = {
        'status_code': status_code,
    }
    if status_code == 200:
        kwargs['json'] = RESOURCE_JSON
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


@given('client has valid credentials')
def step_client_has_valid_credentials(context):
    api_client = api.client.Client(BASE_URL, 'username', 'password')
    context.subject = models.post.Post(api_client)
    context.status_code = 200


@given('client has invalid credentials')
def step_client_has_invalid_credentials(context):
    api_client = api.client.Client(BASE_URL, 'username', 'password')
    context.subject = models.post.Post(api_client)
    context.status_code = 403


@given('resource does not exist')
def step_client_has_invalid_credentials(context):
    context.status_code = 404


@when('make get list request for posts')
def step_make_get_list_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_get_resources_request(mocker, context.status_code)
            context.result = context.subject.get_lists()
    except api.errors.ApiError, e:
        context.exc = e


@when('make get resource request for posts')
def step_make_get_resource_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_get_resource_request(mocker, TEST_ID, context.status_code)
            context.result = context.subject.get(TEST_ID)
    except api.errors.ApiError, e:
        context.exc = e


@when('make create resource request for posts')
def step_make_create_resource_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_create_resource_request(mocker, context.status_code)
            context.result = context.subject.create(NEW_RESOURCE_DATA)
    except api.errors.ApiError, e:
        context.exc = e


@when('make update resource request for posts')
def step_make_update_resource_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_update_resource_request(mocker, TEST_ID, context.status_code)
            context.result = context.subject.update(TEST_ID, NEW_RESOURCE_DATA)
    except api.errors.ApiError, e:
        context.exc = e


@then('it does not have error')
def step_it_does_not_have_error(context):
    assert_that(context.exc, equal_to(None))


@then('it returns not empty list')
def step_it_returns_not_empty_list(context):
    assert_that(context.result, equal_to(RESOURCES_JSON))
    assert_that(len(context.result), equal_to(2))


@then('it returns resource')
def step_it_returns_resource(context):
    assert_that(context.result, equal_to(RESOURCE_JSON))
    assert_that(context.result['id'], equal_to(TEST_ID))


@then('it returns ID')
def step_it_returns_id(context):
    assert_that(context.result, equal_to(TEST_ID))


@then('it returns True')
def step_it_returns_true(context):
    assert_that(context.result, equal_to(True))


@then('it throws unauthorized error')
def step_it_throws_403_error(context):
    assert_that(context.exc.__class__, equal_to(api.errors.UnauthorizedError))


@then('it throws not found error')
def step_it_throws_404_error(context):
    assert_that(context.exc.__class__, equal_to(api.errors.NotFoundError))
