from behave import given, when, then
from dotenv import load_dotenv
import os
from pages.login_page import LoginPage
from utils.data_loader import load_json


load_dotenv("credsdata.env")
    

@given("User is on the registration page")
def step_open_register(context):
    context.login_page = LoginPage(context.page)
    context.login_page.open_registration_page()

@when("User clicks on register")
def step_enter_valid_registration(context):
    context.login_page = LoginPage(context.page)
    LoginPage.open_registration_page()


@when("User enters valid registration details")
def step_enter_valid_registration(context):
    context.login_page = LoginPage(context.page)
    data = load_json("login_data.json")["valid_user"]
    context.login_page.fill_registration_form(data)

@when("User clicks on register submit")
def step_enter_valid_registration(context):
    context.login_page = LoginPage(context.page)
    LoginPage.click_register_submit()

@then("User should be able to see the balance afer clicking on overview")
def get_balance(context):
    context.login_page = LoginPage(context.page)
    LoginPage.click_account_overview()
    LoginPage.get_account_balance()