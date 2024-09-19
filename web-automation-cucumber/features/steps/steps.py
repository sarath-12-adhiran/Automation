from behave import given, when, then
from selenium import webdriver

@given('I have Behave installed')
def step_impl(context):
    context.browser = webdriver.Chrome()

@when('I run behave')
def step_impl(context):
    context.browser.get('http://google.com')

@then('I should see the test run successfully')
def step_impl(context):
    assert "Google" in context.browser.title
    context.browser.quit()
