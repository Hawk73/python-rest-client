from behave import *
import api.client
import models.post

# TODO: stub api responses

@given('client has valid credentials')
def step_impl(context):
    api_client = api.client.Client('https://jsonplaceholder.typicode.com', 'user', 'pass')
    context.model = models.post.Post(api_client)

@given('client has invalid credentials')
def step_impl(context):
    api_client = api.client.Client('https://jsonplaceholder.typicode.com', 'user', 'invalid password')
    context.model = models.post.Post(api_client)

@when('made get list request for posts')
def step_impl(context):
    try:
        context.lists = context.model.get_lists()
    except Exception, e:
        context.exc = e

@then('it returns not empty list')
def step_impl(context):
    assert len(context.lists) is not 0

@then('it throws 403 error')
def step(context):
    assert context.exc.message == 'Invalid credentials'

