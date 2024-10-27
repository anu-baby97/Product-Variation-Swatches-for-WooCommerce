from selenium.webdriver.common.by import By

from config import TestData
from pages.BasePage import BasePage


class ProductAttributes(BasePage):
    design_type = (By.XPATH, "//select[@name='i_swatch_design_style']")
    default_design_type_option = (By.XPATH, "//select[@name='i_swatch_design_style']/option[1]")
    second_option_of_design_type = (By.XPATH, "//select[@name='i_swatch_design_style']/option[2]")
    save_attribute_settings = (By.XPATH, "//input[@name='attribute_save_settings']")

    def __init__(self, driver):
        super().__init__(driver)

    def launch_global_attributes(self):
        self.launch_page(TestData.GLOBAL_ATTRIBUTES_URL)

    def select_swatch_design(self, swatch_type, design_name):
        self.launch_global_attributes()
        self.sleep(3)
        edit_design_icon_for_swatch_type = (By.XPATH, "//p[@class='attr-type-label' and contains(text(), '"+swatch_type+"')]/preceding-sibling::div/span[@class='icon icon-edit']")
        self.sleep(3)
        edit_design_icon = self.get_element(edit_design_icon_for_swatch_type)
        self.sleep(3)
        self.move_to_element(edit_design_icon)
        self.sleep(3)
        self.do_click(edit_design_icon)
        self.sleep(3)
        self.move_to_element(self.get_element(self.design_type))
        self.sleep(3)
        if design_name == 'default_design':
            self.select_element_from_dropdown_by_visible_text(self.design_type, 'Default Design')
        elif design_name == 'design_1':
            self.select_element_from_dropdown_by_value(self.design_type, 'swatch_design_1')
        self.click_save_attribute_settings()
        print('Design selected for', swatch_type)
        self.sleep(3)

    def click_save_attribute_settings(self):
        self.do_click(self.save_attribute_settings)

