from behave import *
from features.support import *
import pythonrestclient
import requests_mock


@given('init post model')
def step_init_post_model(context):
    context.subject = pythonrestclient.PostModel(JSON_RESPONSE_FOR_GET_RESOURCE)
    context.subject_class = pythonrestclient.PostModel


@when('make get all request for posts')
def step_make_get_all_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_get_resources_request(mocker, context.status_code)
            context.result = context.subject_class.all()
    except pythonrestclient.api.errors.ApiError, e:
        context.exc = e


@when('make get resource request for posts')
def step_make_get_resource_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_get_resource_request(mocker, TEST_ID, context.status_code)
            context.result = context.subject_class.get(TEST_ID)
    except pythonrestclient.api.errors.ApiError, e:
        context.exc = e


@when('make create resource request for posts')
def step_make_create_resource_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_create_resource_request(mocker, context.status_code)
            context.result = context.subject_class.create(NEW_RESOURCE_DATA)
    except pythonrestclient.api.errors.ApiError, e:
        context.exc = e


@when('make update resource request for posts')
def step_make_update_resource_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_update_resource_request(mocker, TEST_ID, context.status_code)
            context.result = context.subject.update(TEST_ID, NEW_RESOURCE_DATA)
    except pythonrestclient.api.errors.ApiError, e:
        context.exc = e


@when('make delete resource by ID request for posts')
def step_make_get_resource_by_id_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_delete_resource_request(mocker, TEST_ID, context.status_code)
            context.result = context.subject_class.delete_by_id(TEST_ID)
    except pythonrestclient.api.errors.ApiError, e:
        context.exc = e


@when('make delete resource request for posts')
def step_make_get_resource_request_for_posts(context):
    try:
        context.exc = None
        with requests_mock.Mocker() as mocker:
            stub_delete_resource_request(mocker, TEST_ID, context.status_code)
            context.result = context.subject.delete()
    except pythonrestclient.api.errors.ApiError, e:
        context.exc = e
