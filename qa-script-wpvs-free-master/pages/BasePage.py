import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException, \
    TimeoutException, ElementNotInteractableException, NoSuchElementException, NoAlertPresentException

from tests.BaseClass import BaseClass
from utilities.helper import get_id_property, update_test_run

"""This class is the parent of all pages"""
"""It contains all generic methods and utilities for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def check_element_presence(self, by_locator):
        element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(by_locator))
        return element

    def check_element_staleness(self, element):
        staleness = WebDriverWait(self.driver, 40).until(EC.staleness_of(element))
        return staleness

    def do_click(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(by_locator))
            element.click()
        except ElementClickInterceptedException:
            element = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(by_locator))
            element.click()

    def do_sendkeys(self, by_locator, text):
        element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(by_locator))
        element.send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(by_locator))
        return element.text

    def is_element_selected(self, by_locator):
        # return self.driver.find_element(*by_locator).is_selected()
        try:
            element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(by_locator))
            # time.sleep(1)
            selected = element.is_selected()
            return selected
        except TimeoutException:
            element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(by_locator))
            # time.sleep(1)
            selected = element.is_selected()
            return selected

    def text_clear(self, by_locator):
        element = WebDriverWait(self.driver, 40).until(EC.presence_of_element_located(by_locator))
        # time.sleep(1)
        element.clear()

    def select_element_from_dropdown_by_value(self, by_locator_dropdown, value_select):
        element = self.driver.find_element(*by_locator_dropdown)
        select = Select(element)
        select.select_by_value(value_select)

    def select_element_from_dropdown_by_value_with_element(self, element, value_select):
        select = Select(element)
        select.select_by_value(value_select)

    def multiselect_element_from_dropdown_by_value(self, by_locator_dropdown, value_select):
        element = self.driver.find_element(*by_locator_dropdown)
        select = Select(element)
        select.deselect_all()
        select.select_by_value(value_select)

    def deselect_all_options(self, by_locator_dropdown):
        element = self.driver.find_element(*by_locator_dropdown)
        select = Select(element)
        select.deselect_all()

    def select_element_from_dropdown_by_visible_text(self, by_locator_dropdown, value_select):
        element = self.driver.find_element(*by_locator_dropdown)
        select = Select(element)
        select.select_by_visible_text(value_select)

    # def select_element_from_dropdown_by_index(self, by_locator_dropdown, text):
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(by_locator_dropdown))
    #     select = Select(element)
    #     select.select_by_visible_text(text)

    def get_attribute_by_locator(self, by_locator, property):
        property_value = self.driver.find_element(*by_locator).get_attribute(property)
        return property_value

    def get_attribute_by_element(self, element, property):
        property_value = element.get_attribute(property)
        return property_value

    def is_element_enabled(self, by_locator):
        return self.driver.find_element(*by_locator).is_enabled()

    def get_css_property(self, by_locator, property_name):
        return self.get_element(by_locator).value_of_css_property(property_name)

    def get_hex(self, rgb):
        return Color.from_string(rgb).hex

    def get_attribute_class(self, by_locator):
        className = self.driver.find_element(*by_locator).get_attribute("class")
        return className

    def get_attribute_style(self, by_locator):
        style = self.driver.find_element(*by_locator).get_attribute("style")
        return style

    def get_display_property(self, by_locator):
        return self.get_css_property(by_locator, "display")

    def actions_mouse_hover(self, by_locator):
        action = ActionChains(self.driver)
        action.move_to_element(by_locator).perform()

    def get_background_color_hex(self, by_locator):
        rgb = self.driver.find_element(*by_locator).value_of_css_property("background-color")
        return Color.from_string(rgb).hex

    def get_text_color_hex(self, by_locator):
        rgb = self.driver.find_element(*by_locator).value_of_css_property("color")
        return Color.from_string(rgb).hex

    def get_border_color_hex(self, by_locator):
        rgb = self.driver.find_element(*by_locator).value_of_css_property("border-top")
        return Color.from_string(rgb[10:]).hex

    def get_list_of_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def get_float_position(self, by_locator):
        return self.get_css_property(by_locator, "float")

    def get_element(self, by_locator):
        return self.driver.find_element(*by_locator)

    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)

    def select2_dropdown_using_text(self, dropdown_locator, option_locator, option_text):
        self.driver.execute_script("window.scrollBy(0, 600);")
        try:
            self.do_click(dropdown_locator)
            options = self.driver.find_elements(*option_locator)
            for option in options:
                if option.text == option_text:
                    option.click()
        except StaleElementReferenceException:
            pass
        except ElementClickInterceptedException:
            pass
        # time.sleep(3)

    def scroll_window_to_height(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_window_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_element_into_view(self, by_locator):
        element = self.get_element(by_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def double_click_element(self, by_locator):
        action = ActionChains(self.driver)
        action.double_click(self.get_element(by_locator)).perform()

    def click_element(self, by_locator):
        action = ActionChains(self.driver)
        action.click(self.get_element(by_locator)).perform()

    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def action_clear_text(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE)
        action.perform()

    def click_javascript(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    def action_send_keys(self, text):
        action = ActionChains(self.driver)
        action.key_down(Keys.SHIFT).send_keys(text)
        action.perform()

    def alert_accept(self):
        try:
            alert = Alert(self.driver)
            self.sleep(1)
            alert.accept()
        except NoAlertPresentException:
            pass

    def alert_enter_text(self, text):
        alert = Alert(self.driver)
        self.sleep(1)
        alert.send_keys(text)
        self.sleep(1)
        self.alert_accept()

    def update_test_run_pass(self, section, test_case):
        update_test_run(section[test_case], BaseClass.run_id, True)

    def update_test_run_fail(self, section, test_case):
        update_test_run(section[test_case], BaseClass.run_id, False)

    def sleep(self, secs):
        time.sleep(secs)

    def is_element_displayed(self, by_locator):
        try:
            self.check_element_presence(by_locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_present(self, by_locator):
        try:
            self.get_element(by_locator)
            return True
        except NoSuchElementException:
            return False

    def check_visibility_of_element(self, by_locator):
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(by_locator))
        # self.driver.execute_script("return arguments[0].scrollIntoView(true);", self.get_element(by_locator))

    def check_element_displayed(self, by_locator):
        try:
            return self.get_element(by_locator).is_displayed()
        except NoSuchElementException:
            return False

    def page_refresh(self):
        self.driver.refresh()
        self.sleep(3)

    def launch_page(self, url):
        self.driver.get(url)
        self.sleep(2)
        self.driver.refresh()
        self.sleep(3)
        # retry_count = 5
        # for _ in range(retry_count):
        #     if self.check_database_error():
        #         print("Database connection error detected. Retrying in 5 seconds...")
        #         self.sleep(5)  # Wait before retrying
        #         self.page_refresh()  # Refresh the page
        #     else:
        #         print("Page loaded successfully.")
        #         break
        # else:
        #     print("Max retries reached. Exiting...")

    def check_database_error(self):
        try:
            # Check for the presence of the error message on the page
            error_message = self.get_element(
                (By.XPATH, "//*[contains(text(), 'Error Establishing a Connection with the Database')]"))
            return True if error_message else False
        except NoSuchElementException:
            return False
