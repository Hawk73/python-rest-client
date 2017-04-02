from behave import *
from features.support import *
from hamcrest import *
import pythonrestclient


@given('init API client')
def step_init_api_client(context):
    pythonrestclient.ServiceFactory.init_api_client(BASE_URL, 'username', 'password')


@given('client has valid credentials')
def step_client_has_valid_credentials(context):
    context.status_code = 200


@given('client has invalid credentials')
def step_client_has_invalid_credentials(context):
    context.status_code = 403


@given('resource does not exist')
def step_client_has_invalid_credentials(context):
    context.status_code = 404


@then('it does not have error')
def step_it_does_not_have_error(context):
    assert_that(context.exc, equal_to(None))


@then('it returns collection of posts')
def step_it_returns_not_empty_list(context):
    assert_that(context.result.__class__, equal_to(pythonrestclient.CollectionClass))
    for item in context.result.items:
        assert_that(item.__class__, equal_to(pythonrestclient.PostModel))
    assert_that(len(context.result.items), equal_to(2))


@then('it returns resource of post')
def step_it_returns_resource(context):
    assert_that(context.result.__class__, equal_to(pythonrestclient.PostModel))
    assert_that(context.result.attributes, equal_to(JSON_RESPONSE_FOR_GET_RESOURCE))
    assert_that(context.result.attributes['id'], equal_to(TEST_ID))


@then('it returns ID')
def step_it_returns_id(context):
    assert_that(context.result, equal_to(TEST_ID))


@then('it returns True')
def step_it_returns_true(context):
    assert_that(context.result, equal_to(True))


@then('it throws unauthorized error')
def step_it_throws_403_error(context):
    assert_that(context.exc.__class__, equal_to(pythonrestclient.api.errors.UnauthorizedError))


@then('it throws not found error')
def step_it_throws_404_error(context):
    assert_that(context.exc.__class__, equal_to(pythonrestclient.api.errors.NotFoundError))
