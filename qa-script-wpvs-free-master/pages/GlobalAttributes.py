from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config import TestData
from pages.BasePage import BasePage
from pages.CommonFunctions import CommonFunctions
from utilities.case_id import CaseID
from utilities.helper import get_id_property


class GlobalAttributes(BasePage):
    attribute_heading = (By.XPATH, "//div[@class='wrap woocommerce']/h1[text()='Attributes']")
    attribute_name = (By.ID, "attribute_label")
    attribute_type = (By.ID, "attribute_type")
    add_new_attribute = (By.XPATH, "//button[@name='add_new_attribute']")
    term_name = (By.ID, "tag-name")
    submit_button = (By.ID, "submit")
    container = (By.ID, "col-container")
    product_color = (By.XPATH, "//input[@name='product_pa_color']")
    product_label = (By.XPATH, "//input[@name='product_pa_label']")
    delete_button = (By.XPATH, "//tr//a[text()='Delete']")
    attribute_row = (By.XPATH, "//td//strong/a")
    test_case_ids = CaseID.GLOBAL_ATTRIBUTES

    def __init__(self, driver):
        super().__init__(driver)
        self.commonFunctions = CommonFunctions(self.driver, self.test_case_ids)

    def delete_all_attributes(self):
        self.commonFunctions.launch_edit_product_attributes_page()
        attribute_rows = self.get_elements(self.attribute_row)
        delete_buttons = self.get_elements(self.delete_button)
        # print(len(attribute_rows), ' ', len(delete_buttons))
        self.sleep(3)
        if len(attribute_rows) == 0:
            pass
        for i in range(len(attribute_rows)):
            for j in range(len(delete_buttons)):
                i, j = 0, 0
                self.sleep(3)
                self.move_to_element(attribute_rows[i])
                print('Deleting', attribute_rows[i].text, 'attribute')
                self.sleep(3)
                delete_buttons[j].click()
                self.sleep(3)
                self.alert_accept()
                self.sleep(5)
                if len(attribute_rows) == 1:
                    break
                attribute_rows = self.get_elements(self.attribute_row)
                delete_buttons = self.get_elements(self.delete_button)
                # print(len(attribute_rows), ' ', len(delete_buttons))
                break
            self.sleep(5)
        print('Deleted all attributes successfully')

    def create_attribute_name(self, swatch_type, attribute_name):
        self.commonFunctions.launch_edit_product_attributes_page()
        self.do_sendkeys(self.attribute_name, attribute_name)
        self.scroll_window_to_height()
        self.sleep(2)
        self.select_element_from_dropdown_by_value(self.attribute_type, swatch_type)
        self.do_click(self.add_new_attribute)
        self.sleep(2)
        self.scroll_element_into_view(self.attribute_heading)
        self.sleep(2)
        print('Swatch type selected for attribute ', attribute_name)
        self.do_click((By.XPATH,
                          "//td[contains(text(),'" + attribute_name + "')]/following-sibling::td/a[@class='configure-terms']"))

    def create_new_term(self, swatch_type, term_name, additional_property):
        if swatch_type == 'image_1' or swatch_type == 'image_2':
            self.page_refresh()
            self.sleep(2)
        self.scroll_window_to_height()
        self.sleep(2)
        self.do_sendkeys(self.term_name, term_name)
        if swatch_type == 'color':
            self.do_sendkeys(self.product_color, additional_property)
            self.do_click(self.container)
        elif swatch_type == 'image_1':
            self.scroll_window_to_height()
            self.sleep(2)
            self.do_click(self.commonFunctions.image_upload_button)
            self.sleep(10)
            self.move_to_element(self.get_element(self.commonFunctions.first_image))
            self.sleep(2)
            self.do_click(self.commonFunctions.first_image)
            self.sleep(3)
            self.do_click(self.commonFunctions.choose_image_button)
        elif swatch_type == 'image_2':
            self.scroll_window_to_height()
            self.sleep(2)
            self.do_click(self.commonFunctions.image_upload_button)
            self.sleep(10)
            self.move_to_element(self.get_element(self.commonFunctions.second_image))
            self.sleep(2)
            self.do_click(self.commonFunctions.second_image)
            self.sleep(3)
            self.do_click(self.commonFunctions.choose_image_button)
        elif swatch_type == 'label':
            self.do_sendkeys(self.product_label, additional_property)
        else:
            pass
        print('\nAttribute with term name ' + term_name + ' is created')
        self.do_click(self.submit_button)
        self.sleep(10)

    def is_attribute_created(self, attribute_name):
        self.commonFunctions.launch_edit_product_attributes_page()
        try:
            self.check_element_presence((By.XPATH, "//td//strong/a[text()='"+attribute_name+"']"))
            return True
        except NoSuchElementException:
            return False

