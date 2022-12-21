import time

from selenium.common.exceptions import TimeoutException, \
    StaleElementReferenceException, NoAlertPresentException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
import config.base_config as config


class BasePage(object):

    def __init__(self, context):
        self.browser = context.driver
        self.timeout = config.default_wait

    def visit(self, url):
        self.browser.get(url)
        print("Visiting url: {}".format(url))
        return self

    def find_element(self, locator, visibility=True, timeout=config.default_wait):
        try:
            if visibility:
                return WebDriverWait(self.browser, timeout=timeout).until(ec.visibility_of_element_located(locator),
                                                                          'ELEMENT IS NOT FOUND OR VISIBLE! => {}'.format(
                                                                              locator))
            else:
                return WebDriverWait(self.browser, timeout=timeout).until(ec.presence_of_element_located(locator),
                                                                          'ELEMENT IS NOT FOUND! => {}'.format(locator))
        except TimeoutException as e:
            error = e.args[0]
            raise TimeoutException(error) from e.__cause__
        except StaleElementReferenceException as e:
            error = e.args[0]
            raise StaleElementReferenceException(error) from e.__cause__

    def click_element(self, locator, timeout=config.default_wait):
        try:
            WebDriverWait(self.browser, timeout=timeout).until(ec.element_to_be_clickable(locator),
                                                                   'UNABLE TO LOCATE ELEMENT! => {}'.format(
                                                                       locator)).click()
        except TimeoutException as e:
            error = e.args[0]
            raise TimeoutException(error) from e.__cause__
        except StaleElementReferenceException as e:
            error = e.args[0]
            raise StaleElementReferenceException(error) from e.__cause__
        return self

    def fill_input(self, locator, value, timeout=config.default_wait):
        element = self.find_element(locator, timeout=timeout)
        try:
            element.send_keys(value)
        except StaleElementReferenceException as e:
            print(f"Failed to fill {value} input on {locator} with {e}")
        return self

    def select_from_dropdown_by_text(self, dropdown_locator, option_text):
        element = WebDriverWait(self.browser, self.timeout).until(ec.presence_of_element_located(dropdown_locator))
        Select(element).select_by_visible_text(option_text)
        return self

    def accept_alert(self, expected_text_in_alert: str = None):
        try:
            alert = self.browser.switch_to.alert
            text = alert.text
            if expected_text_in_alert is not None and text is not None:
                assert expected_text_in_alert in text, f"Expected {expected_text_in_alert} in popup window but found {text}!"
            alert.accept()
        except NoAlertPresentException as e:
            error = e.args[0]
            raise NoAlertPresentException(error) from e.__cause__
        return self

    def get_current_url(self):
        return self.browser.current_url
