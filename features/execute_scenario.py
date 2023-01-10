from behave import *
from ..main import Scenario


@given('the driver started')
def init_driver(context):
    Scenario.__init__()


@when('driver login')
def login(context):
    Scenario.login()


@when('new grade added')
def add(context):
    Scenario.add()


@then('new row created')
def check(context):
    Scenario.check()


@then('row removed')
def remove(context):
    Scenario.remove()