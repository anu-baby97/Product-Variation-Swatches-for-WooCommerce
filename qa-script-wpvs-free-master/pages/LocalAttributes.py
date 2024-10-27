from selenium.common import NoSuchElementException, NoAlertPresentException
from selenium.webdriver.common.by import By

from config import TestData
from pages.BasePage import BasePage
from pages.CommonFunctions import CommonFunctions
from utilities.case_id import CaseID


class LocalAttributes(BasePage):
    test_case_ids = CaseID.LOCAL_ATTRIBUTES
    add_new_attribute = (By.XPATH, "//div[@class='actions']/button[text()='Add new']")
    local_attribute_name_input_fields = (
        By.XPATH, "//td[contains(@class, 'attribute_name')]/input[contains(@name,'attribute_names')]")
    local_attribute_terms = (By.XPATH,
                             "//td[contains(@class, 'attribute_name')]/following-sibling::*//textarea[contains(@name, 'attribute_values')]")
    swatches_settings_tab = (By.XPATH, "//span[text()='Swatches Settings']/parent::a")
    local_attributes_list = (By.XPATH, "//*[@id='custom_variations_inner']/div/h3/strong")
    local_attribute_type_select = (By.XPATH, "//select[contains(@name, 'th_attribute_type')]")
    close_attributes = (By.XPATH, "//div[@id='product_attributes']//a[text()='Close'][1]")

    def __init__(self, driver):
        super().__init__(driver)
        self.commonFunctions = CommonFunctions(self.driver, self.test_case_ids)

    def create_local_attribute(self, attribute_order, attribute_name, term_values, swatch_type, term_property_1,
                               term_property_2):
        self.do_click(self.add_new_attribute)
        self.do_sendkeys((By.XPATH, "//td[contains(@class, 'attribute_name')]/following-sibling::*/textarea["
                                    "@name='attribute_values[" + attribute_order + "]']"), term_values)
        self.do_sendkeys((By.XPATH,
                          "//td[contains(@class, 'attribute_name')]/input[@name='attribute_names[" + attribute_order + "]']"),
                         attribute_name)
        self.scroll_element_into_view(self.commonFunctions.product_image)
        self.sleep(2)
        self.do_click(self.commonFunctions.attributes_tab)
        self.sleep(3)
        self.do_click(self.close_attributes)
        self.sleep(2)
        self.do_click(self.commonFunctions.save_attributes_button)
        self.sleep(10)
        print('Local attribute with name ' + attribute_name + ' and term values ' + term_values + ' is created')
        # self.sleep(10)
        self.commonFunctions.check_product_update_success_message()
        self.page_refresh()
        self.scroll_element_into_view(self.commonFunctions.product_data)
        self.sleep(5)
        self.do_click(self.swatches_settings_tab)
        self.sleep(10)
        local_attributes_list = self.get_elements(self.local_attributes_list)
        self.sleep(5)
        self.do_click(local_attributes_list[len(local_attributes_list) - 1])
        self.sleep(5)
        local_attribute_type_select_boxes = self.get_elements(self.local_attribute_type_select)
        self.sleep(5)
        self.select_element_from_dropdown_by_value_with_element(
            local_attribute_type_select_boxes[len(local_attribute_type_select_boxes) - 1], swatch_type)
        self.sleep(3)
        print('Swatch type ' + swatch_type + ' assigned to the attribute created')
        self.sleep(3)
        term_values = term_values.split('|')
        if swatch_type == 'color':
            self.do_sendkeys((By.XPATH, "//td[text()='" + term_values[
                0] + "']/parent::tr/following-sibling::tr//input[@class='thpladmin-colorpick']"), term_property_1)
            self.sleep(2)
            self.do_click((By.XPATH,
                           "//table[@class='thwvsf-custom-table thwvsf-custom-table-color']//h3[@data-term_name='" +
                           term_values[1] + "']"))
            self.sleep(2)
            self.do_sendkeys((By.XPATH, "//td[text()='" + term_values[
                1] + "']/parent::tr/following-sibling::tr//input[@class='thpladmin-colorpick']"), term_property_2)
            self.sleep(2)
        elif swatch_type == 'image':
            for i in range(0, 2):
                if i == 1:
                    self.scroll_element_into_view(self.commonFunctions.product_data)
                    self.sleep(5)
                    self.do_click(self.swatches_settings_tab)
                    self.sleep(15)
                    local_attributes_list = self.get_elements(self.local_attributes_list)
                    self.sleep(5)
                    self.do_click(local_attributes_list[len(local_attributes_list) - 1])
                    self.sleep(5)
                    self.do_click((By.XPATH,
                                   "//table[@class='thwvsf-custom-table thwvsf-custom-table-image']//h3[@data-term_name='" +
                                   term_values[i] + "']"))
                    self.sleep(2)
                self.do_click((By.XPATH, "//td[text()='" + term_values[
                    i] + "']/parent::tr/following-sibling::tr//button[@class='thwvsf-upload-image-button button ']/img"))
                self.sleep(15)
                if i == 0:
                    self.move_to_element(self.get_element(self.commonFunctions.first_image))
                    self.sleep(2)
                    self.do_click(self.commonFunctions.first_image)
                else:
                    self.move_to_element(self.get_element(self.commonFunctions.second_image))
                    self.sleep(2)
                    self.do_click(self.commonFunctions.second_image)
                self.sleep(3)
                self.do_click(self.commonFunctions.choose_image_button)
                self.sleep(3)
                self.commonFunctions.check_product_update_success_message()
                self.sleep(2)
        elif swatch_type == 'label':
            self.do_sendkeys((By.XPATH, "//td[text()='" + term_values[
                0] + "']/parent::tr/following-sibling::tr//input[@class='i_label']"), term_property_1)
            self.sleep(2)
            self.do_click((By.XPATH,
                           "//table[@class='thwvsf-custom-table thwvsf-custom-table-label']//h3[@data-term_name='" +
                           term_values[1] + "']"))
            self.sleep(2)
            self.do_sendkeys((By.XPATH, "//td[text()='" + term_values[
                1] + "']/parent::tr/following-sibling::tr//input[@class='i_label']"), term_property_2)
            self.sleep(2)
        if not swatch_type == 'image':
            self.commonFunctions.check_product_update_success_message()
            self.sleep(2)
        if swatch_type == 'color' or swatch_type == 'label':
            print('Term properties ' + term_property_1 + ', ' + term_property_2 + ' assigned to term names')

    def is_local_attribute_created(self, attribute_name):
        self.commonFunctions.navigate_to_attributes_tab()
        return self.is_element_displayed(
            (By.XPATH, "//div[contains(@class,'product_attributes')]//strong[text()='"+attribute_name+"']"))
