from behave import given, when, then
from selenium import webdriver
import logging
import os
import stat

# Define the path to the log file


@given('I have second Behave installed')
def step_impl(context):
    context.browser = webdriver.Chrome()
    # logger.info("Browser initialized.")

@when('I run second behave')
def step_impl(context):
    context.browser.get('http://amazon.com')
    print("title1 -",context.browser.title)
    print("title2 -",context.browser.title)
    print("title3 -",context.browser.title)
    print("title4 -",context.browser.title)
    print("title5 -",context.browser.title)

    # logger.info("Navigated to Amazon.com")
    # logger.info(f"Title: {context.browser.title}")

@then('I should see the second test run successfully')
def step_impl(context):
    assert "Amazon" in context.browser.title
    # logger.info("Test assertion passed: 'Amazon' is in the title.")
    context.browser.quit()
    # logger.info("Browser closed.")

