from behave import *
from features.support import *
from hamcrest import *
import pythonrestclient
import requests_mock


@given('init collection')
def step_init_collection(context):
    with requests_mock.Mocker() as mocker:
        stub_get_resources_request(mocker)
        context.subject = pythonrestclient.PostModel.get_lists()


@when('delete all items')
def step_delete_all_items(context):
    context.exc = None
    try:
        with requests_mock.Mocker() as mocker:
            stub_delete_resource_request(mocker, 1, context.status_code)
            stub_delete_resource_request(mocker, 2, context.status_code)
            context.result = context.subject.delete_all()
    except pythonrestclient.api.errors.ApiError, e:
        context.exc = e



@then('it has no items')
def step_it_has_no_items(context):
    assert_that(context.subject.items, equal_to([]))
