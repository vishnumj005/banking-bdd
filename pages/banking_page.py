import time

from selenium.webdriver.common.by import By

from config.constants.constants import Constants
from pages.base.base_page import BasePage
from faker import Faker

fake = Faker()


class BankingPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    bank_manager_login_button = (By.XPATH, "//button[text()='Bank Manager Login']")
    add_customer_button = (By.XPATH, "//button[contains(.,'Add Customer')]")
    first_name_input = (By.XPATH, "//input[@placeholder='First Name']")
    last_name_input = (By.XPATH, "//input[@placeholder='Last Name']")
    post_code_input = (By.XPATH, "//input[@placeholder='Post Code']")
    submit_customer_details_button = (By.XPATH, "(//button[contains(.,'Add Customer')])[2]")
    open_account_tab = (By.XPATH, "//button[contains(.,'Open Account')]")
    customer_name_dropdown = (By.ID, "userSelect")
    currency_dropdown = (By.ID, "currency")
    process_button = (By.XPATH, "//button[contains(.,'Process')]")

    def click_bank_manager_login_button(self):
        self.click_element(self.bank_manager_login_button)

    def verify_page_url(self):
        time.sleep(2)
        assert self.get_current_url() == Constants.BANK_MANAGER_HOME_PAGE_URL

    def click_add_customer_button(self):
        self.click_element(self.add_customer_button)

    def fill_customer_information(self, context):
        first_name = fake.first_name()
        last_name = fake.last_name()
        context.full_name = f"{first_name} {last_name}"

        self.fill_input(self.first_name_input, first_name) \
            .fill_input(self.last_name_input, last_name) \
            .fill_input(self.post_code_input, fake.postcode()) \
            .click_element(self.submit_customer_details_button)\
            .accept_alert("Customer added successfully with customer id")

    def click_open_account_tab(self):
        self.click_element(self.open_account_tab)

    def select_customer_name_and_currency(self, context):
        self.select_from_dropdown_by_text(self.customer_name_dropdown, context.full_name) \
            .select_from_dropdown_by_text(self.currency_dropdown, "Dollar")

    def click_proceed_button(self):
        self.click_element(self.process_button)

    def verify_account_created_pop_message(self):
        self.accept_alert("Account created successfully with account Number")
