from behave import step

from pages.banking_page import BankingPage


@step("I click on bank manager login button")
def step_impl(context):
    BankingPage(context).click_bank_manager_login_button()


@step("I verify the page url")
def step_impl(context):
    BankingPage(context).verify_page_url()


@step("I click on add customer button")
def step_impl(context):
    BankingPage(context).click_add_customer_button()


@step("I fill the customer information and click add customer button")
def step_impl(context):
    BankingPage(context).fill_customer_information(context)


@step("I click on open account tab")
def step_impl(context):
    BankingPage(context).click_open_account_tab()


@step("I select customer name and currency")
def step_impl(context):
    BankingPage(context).select_customer_name_and_currency(context)


@step("I click process button")
def step_impl(context):
    BankingPage(context).click_proceed_button()


@step("verify the account created pop up message")
def step_impl(context):
    BankingPage(context).verify_account_created_pop_message()
