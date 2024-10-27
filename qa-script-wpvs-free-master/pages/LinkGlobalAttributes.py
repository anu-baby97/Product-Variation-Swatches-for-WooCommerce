from selenium.webdriver.common.by import By

from config import TestData
from pages.BasePage import BasePage
from pages.CommonFunctions import CommonFunctions
from pages.GlobalAttributes import GlobalAttributes


class LinkGlobalAttributes(BasePage):
    select_all_button = (By.XPATH, "//button[text()='Select all']")
    select_attribute_field = (By.XPATH, "//span[@class='select2-selection__placeholder' and text()='Add existing']")
    product_attributes = (By.XPATH, "//div[contains(@class,'product_attributes')]")
    test_case_ids = GlobalAttributes.test_case_ids

    def __init__(self, driver):
        super().__init__(driver)
        self.commonFunctions = CommonFunctions(self.driver, self.test_case_ids)

    def select_global_attributes(self, global_attribute):
        self.do_click(self.select_attribute_field)
        self.commonFunctions.check_visibility_of_element(self.product_attributes)
        self.sleep(5)
        self.do_click((By.XPATH, "//ul[@class='select2-results__options']//li[text()='" + global_attribute + "']"))
        self.sleep(5)
        self.do_click((By.XPATH,
                                   "//strong[text()='" + global_attribute + "']/parent::td[@class='attribute_name']/following-sibling::td//button[text()='Select all']"))
        self.commonFunctions.check_visibility_of_element(self.product_attributes)
        self.sleep(5)
        self.do_click(self.commonFunctions.save_attributes_button)
        self.commonFunctions.check_visibility_of_element(self.product_attributes)
        self.sleep(10)
        print('Selected', global_attribute, 'attribute for the product')
        self.scroll_element_into_view(self.commonFunctions.product_data)
        self.sleep(4)
