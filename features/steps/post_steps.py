from behave import *
from hamcrest import *
import api.client
import api.errors
import models.post
import requests_mock


BASE_URL = 'http://localhost'
# TODO: create factory
POSTS_JSON = [
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


def stub_get_list_request(mocker, is_valid_auth = True):
    if is_valid_auth:
        kwargs = {
            'json': POSTS_JSON,
        }
    else:
        kwargs = {
            'status_code': 403,
        }
    mocker.get(BASE_URL + '/posts/', **kwargs)


@given('client has valid credentials')
def step_client_has_valid_credentials(context):
    api_client = api.client.Client(BASE_URL, 'username', 'password')
    context.subject = models.post.Post(api_client)
    context.is_valid_auth = True


@given('client has invalid credentials')
def step_client_has_invalid_credentials(context):
    api_client = api.client.Client(BASE_URL, 'username', 'password')
    context.subject = models.post.Post(api_client)
    context.is_valid_auth = False


@when('make get list request for posts')
def step_make_get_list_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_get_list_request(mocker, context.is_valid_auth)
            context.result = context.subject.get_lists()
    except api.errors.ApiError, e:
        context.exc = e


@then('it returns not empty list')
def step_it_returns_not_empty_list(context):
    assert_that(context.exc, equal_to(None))
    assert_that(context.result, equal_to(POSTS_JSON))
    assert_that(len(context.result), equal_to(2))


@then('it throws unauthorized error')
def step_it_throws_403_error(context):
    assert_that(context.exc.__class__, equal_to(api.errors.UnauthorizedError))
