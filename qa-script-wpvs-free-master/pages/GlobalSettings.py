from selenium.webdriver.common.by import By

from config import TestData
from pages.BasePage import BasePage
from pages.CommonFunctions import CommonFunctions
from utilities.case_id import CaseID


class GlobalSettings(BasePage):
    displayed_property = ''
    save_global_settings_button = (
        By.XPATH, "//*[@id='thwvsf_global_settings']/div/input[@name='global_save_settings']")
    reset_global_settings_button = (By.NAME, "global_reset_settings")
    lazy_load_toggle = (By.XPATH, "//label[@for='i_enable_lazy_load']")
    lazy_load_checkbox = (By.ID, "i_enable_lazy_load")
    convert_to_label_swatches_toggle = (By.XPATH, "//label[@for='i_auto_convert']")
    convert_to_label_swatches_checkbox = (By.ID, "i_auto_convert")
    behaviour_for_out_of_stock = (By.NAME, "i_behavior_of_out_of_stock")
    behaviour_for_unavailable_variation = (By.NAME, "i_behavior_for_unavailable_variation")
    clear_on_reselect_toggle = (By.XPATH, "//label[@for='i_clear_select']")
    clear_on_reselect_checkbox = (By.NAME, "i_clear_select")
    disable_swatches_plugin_stylesheet_toggle = (By.XPATH, "//label[@for='i_disable_style_sheet']")
    disable_swatches_plugin_stylesheet_checkbox = (By.NAME, "i_disable_style_sheet")
    show_selected_variation_name_beside_attribute_label_toggle = (
    By.XPATH, "//label[@for='i_show_selected_variation_name']")
    show_selected_variation_name_beside_attribute_label_checkbox = (By.NAME, "i_show_selected_variation_name")
    enable_swatches_on_additional_info_toggle = (By.XPATH, "//label[@for='i_swatches_on_additional_info']")
    enable_swatches_on_additional_info_checkbox = (By.NAME, "i_swatches_on_additional_info")
    ajax_threshold = (By.NAME, "i_ajax_variation_threshold")
    test_case_ids = CaseID.GLOBAL_SETTINGS

    def __init__(self, driver):
        super().__init__(driver)
        self.commonFunctions = CommonFunctions(self.driver, self.test_case_ids)

    def launch_global_settings_page(self):
        self.launch_page(TestData.GLOBAL_SETTINGS_URL)

    def click_reset_global_settings(self):
        self.do_click(self.reset_global_settings_button)
        self.sleep(3)
        self.alert_accept()
        self.sleep(3)

    def select_global_settings(self, setting, option):
        self.launch_global_settings_page()
        match setting:
            case 'lazy_load':
                self.scroll_element_into_view(self.lazy_load_checkbox)
                if option == 'off':
                    if self.is_element_selected(self.lazy_load_checkbox):
                        self.do_click(self.lazy_load_toggle)
                else:
                    if not self.is_element_selected(self.lazy_load_checkbox):
                        self.do_click(self.lazy_load_toggle)
            case 'convert_to_label_swatches':
                if option == 'off':
                    self.scroll_element_into_view(self.convert_to_label_swatches_checkbox)
                    if self.is_element_selected(self.convert_to_label_swatches_checkbox):
                        self.do_click(self.convert_to_label_swatches_toggle)
                else:
                    self.scroll_element_into_view(self.convert_to_label_swatches_checkbox)
                    if not self.is_element_selected(self.convert_to_label_swatches_checkbox):
                        self.do_click(self.convert_to_label_swatches_toggle)
            case 'behaviour_for_out_of_stock_variation':
                self.select_element_from_dropdown_by_value(self.behaviour_for_out_of_stock, option)
            case 'behaviour_for_unavailable_variation':
                self.select_element_from_dropdown_by_value(self.behaviour_for_unavailable_variation, option)
            case 'clear_on_reselect':
                self.scroll_element_into_view(self.clear_on_reselect_checkbox)
                if option == 'off':
                    if self.is_element_selected(self.clear_on_reselect_checkbox):
                        self.do_click(self.clear_on_reselect_toggle)
                else:
                    if not self.is_element_selected(self.clear_on_reselect_checkbox):
                        self.do_click(self.clear_on_reselect_toggle)
            case 'disable_swatches_plugin_stylesheet':
                self.scroll_element_into_view(self.disable_swatches_plugin_stylesheet_checkbox)
                if option == 'off':
                    if self.is_element_selected(self.disable_swatches_plugin_stylesheet_checkbox):
                        self.do_click(self.disable_swatches_plugin_stylesheet_toggle)
                else:
                    if not self.is_element_selected(self.disable_swatches_plugin_stylesheet_checkbox):
                        self.do_click(self.disable_swatches_plugin_stylesheet_toggle)
            case 'show_selected_variation_name_beside_attribute_label':
                self.scroll_element_into_view(self.show_selected_variation_name_beside_attribute_label_checkbox)
                if option == 'off':
                    if self.is_element_selected(self.show_selected_variation_name_beside_attribute_label_checkbox):
                        self.do_click(self.show_selected_variation_name_beside_attribute_label_toggle)
                else:
                    if not self.is_element_selected(self.show_selected_variation_name_beside_attribute_label_checkbox):
                        self.do_click(self.show_selected_variation_name_beside_attribute_label_toggle)
            case 'enable_swatches_on_additional_info':
                self.scroll_element_into_view(self.enable_swatches_on_additional_info_checkbox)
                if option == 'off':
                    if self.is_element_selected(self.enable_swatches_on_additional_info_checkbox):
                        self.do_click(self.enable_swatches_on_additional_info_toggle)
                else:
                    if not self.is_element_selected(self.enable_swatches_on_additional_info_checkbox):
                        self.do_click(self.enable_swatches_on_additional_info_toggle)
        self.do_click(self.save_global_settings_button)

    def enter_ajax_threshold(self, value):
        self.text_clear(self.ajax_threshold)
        self.do_sendkeys(self.ajax_threshold, value)
        self.do_click(self.save_global_settings_button)

    def check_global_settings(self, settings, option, swatch_type):
        attribute_name = self.commonFunctions.get_attribute_name(swatch_type).lower()
        swatch_element = (By.XPATH, "//li[contains(@class, 'attribute_pa_" + attribute_name + "')]")
        match settings:
            case 'convert_to_label_swatches':
                label_swatch_element = (
                By.XPATH, "//select[contains(@name,'" + attribute_name + "')]/following-sibling::ul/li")
                if option == 'off':
                    self.displayed_property = not self.is_element_present(label_swatch_element)
                else:
                    self.displayed_property = self.is_element_present(label_swatch_element)
            case 'clear_on_reselect':
                swatch_element_selected = (
                By.XPATH, "//li[contains(@class, '" + attribute_name + "') and contains(@class, 'thwvsf-selected')]")
                self.do_click(swatch_element)
                self.sleep(1)
                self.do_click(swatch_element)
                self.sleep(1)
                if option == 'off':
                    self.displayed_property = self.is_element_present(swatch_element_selected)
                else:
                    self.displayed_property = not self.is_element_present(swatch_element_selected)
            case 'disable_swatches_plugin_stylesheet':
                self.displayed_property = self.get_display_property(swatch_element)
                if option == 'off':
                    self.displayed_property = not self.displayed_property == 'list-item'
                else:
                    self.displayed_property = self.displayed_property == 'list-item'
            case 'show_selected_variation_name_beside_attribute_label':
                if swatch_type == 'radio':
                    self.do_click((By.XPATH,
                                   "//label[text()='" + attribute_name.capitalize() + "']/ancestor::tr//span[@class='variation-name']"))
                else:
                    self.do_click(swatch_element)
                self.sleep(2)
                variation_name_label = (
                By.XPATH, "//label[text()='" + attribute_name.capitalize() + "']/label[@class='variation_name_label']")
                if option == 'off':
                    self.displayed_property = not self.is_element_present(variation_name_label)
                else:
                    self.displayed_property = self.is_element_present(variation_name_label)
            case 'enable_swatches_on_additional_info':
                additional_info_swatches = (By.XPATH,
                                            "//th[text()='" + attribute_name.capitalize() + "']/parent::tr//div[@class='thwvsf_additional_wrapper']")
                self.sleep(1)
                if option == 'off':
                    self.displayed_property = not self.is_element_present(additional_info_swatches)
                else:
                    self.displayed_property = self.is_element_present(additional_info_swatches)
            case 'behaviour_for_out_of_stock_variation':
                variation_terms_name = self.get_variation_terms(0)
                self.commonFunctions.launch_variable_product_page(0)
                if option == 'default':
                    self.do_click((By.XPATH, "//span[@class='variation-name' and text()='" + variation_terms_name[len(variation_terms_name) - 1] + "']"))
                    for i in range(len(variation_terms_name) - 1):
                        self.do_click((By.XPATH, "//ul[@class='thwvsf-wrapper-ul']//li[@title='" + variation_terms_name[i] + "']"))
                        self.sleep(1)
                    return self.check_element_displayed((By.XPATH, "//div[@class='woocommerce-variation-availability']/p[text()='Out of stock']"))
                else:
                    self.do_click((By.XPATH, "//span[@class='variation-name' and text()='" + variation_terms_name[
                        len(variation_terms_name) - 1] + "']"))
                    for i in range(len(variation_terms_name) - 2):
                        self.do_click((By.XPATH, "//ul[@class='thwvsf-wrapper-ul']//li[@title='" + variation_terms_name[
                            i] + "']"))
                        self.sleep(1)
                    if option == 'blur':
                        return self.get_css_property(
                            (By.XPATH, "//ul[@class='thwvsf-wrapper-ul']//li[@title='"+variation_terms_name[len(variation_terms_name)-2]+"']"), 'opacity')
                    elif option == 'blur_with_cross':
                        return (self.driver.execute_script(
                    "return window.getComputedStyle(arguments[0], ':after').getPropertyValue('height');", self.get_element((By.XPATH, "//ul[@class='thwvsf-wrapper-ul']//li[@title='"+variation_terms_name[len(variation_terms_name)-2]+"']"))))
            case 'behaviour_for_unavailable_variation':
                variation_terms_name = self.get_variation_terms(1)
                self.commonFunctions.launch_variable_product_page(0)
                if option == 'hide':
                    self.do_click((By.XPATH, "//span[@class='variation-name' and text()='" + variation_terms_name[
                        len(variation_terms_name) - 1] + "']"))
                    for i in range(len(variation_terms_name) - 2):
                        self.do_click((By.XPATH, "//ul[@class='thwvsf-wrapper-ul']//li[@title='" + variation_terms_name[
                            i] + "']"))
                        self.sleep(1)
                    return not self.check_element_displayed(
                        (By.XPATH, "//ul[@class='thwvsf-wrapper-ul']//li[@title='" + variation_terms_name[len(variation_terms_name)-2] + "']"))
                else:
                    self.do_click((By.XPATH, "//span[@class='variation-name' and text()='" + variation_terms_name[
                        len(variation_terms_name) - 1] + "']"))
                    for i in range(len(variation_terms_name) - 2):
                        self.do_click((By.XPATH, "//ul[@class='thwvsf-wrapper-ul']//li[@title='" + variation_terms_name[
                            i] + "']"))
                        self.sleep(1)
                    if option == 'blur':
                        return self.get_css_property(
                            (By.XPATH, "//ul[@class='thwvsf-wrapper-ul']//li[@title='" + variation_terms_name[
                                len(variation_terms_name) - 2] + "']"), 'opacity')
                    elif option == 'blur_with_cross':
                        return (self.driver.execute_script(
                            "return window.getComputedStyle(arguments[0], ':after').getPropertyValue('height');",
                            self.get_element((By.XPATH,
                                              "//ul[@class='thwvsf-wrapper-ul']//li[@title='" + variation_terms_name[
                                                  len(variation_terms_name) - 2] + "']"))))

        print(self.displayed_property, 'for swatch type', swatch_type)
        return self.displayed_property

    def assign_variation_as_out_of_stock(self):
        self.commonFunctions.launch_variable_product_edit_page(0)
        self.check_visibility_of_element(self.commonFunctions.product_data)
        self.do_click(self.commonFunctions.variations_tab)
        self.check_visibility_of_element(self.commonFunctions.variations_table)
        variation_boxes = self.get_elements(
            (By.XPATH, "//div[contains(@class, 'woocommerce_variation')]/h3/a[text()='Edit']"))
        self.sleep(5)
        variation_boxes[0].click()
        self.sleep(2)
        stock_status_select = self.get_elements((By.XPATH, "//select[contains(@id, 'variable_stock_status')]"))
        self.select_element_from_dropdown_by_value_with_element(stock_status_select[0], 'outofstock')
        self.sleep(2)
        variation_boxes[0].click()
        self.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", variation_boxes[len(variation_boxes) - 4])
        if self.is_element_enabled(self.commonFunctions.save_changes):
            self.do_click(self.commonFunctions.save_changes)
            self.sleep(10)

    def assign_variation_as_unavailable(self):
        self.commonFunctions.launch_variable_product_edit_page(0)
        self.check_visibility_of_element(self.commonFunctions.product_data)
        self.do_click(self.commonFunctions.variations_tab)
        self.check_visibility_of_element(self.commonFunctions.variations_table)
        variation_boxes = self.get_elements(
            (By.XPATH, "//div[contains(@class, 'woocommerce_variation')]/h3/a[text()='Edit']"))
        self.sleep(3)
        variation_boxes[1].click()
        self.sleep(2)
        self.text_clear((By.XPATH, "//input[contains(@name, 'variable_regular_price[1]')]"))
        self.sleep(2)
        variation_boxes[1].click()
        self.sleep(2)
        self.driver.execute_script("arguments[0].scrollIntoView();", variation_boxes[len(variation_boxes) - 4])
        if self.is_element_enabled(self.commonFunctions.save_changes):
            self.do_click(self.commonFunctions.save_changes)
            self.sleep(10)

    def get_variation_terms(self, variation_order):
        self.commonFunctions.launch_variable_product_edit_page(0)
        self.check_visibility_of_element(self.commonFunctions.product_data)
        self.do_click(self.commonFunctions.variations_tab)
        self.check_visibility_of_element(self.commonFunctions.variations_table)
        variation_boxes = self.get_elements(
            (By.XPATH, "//div[contains(@class, 'woocommerce_variation')]/h3/a[text()='Edit']"))
        self.sleep(3)
        variation_boxes[variation_order].click()
        self.sleep(2)
        variation_boxes = self.get_elements(
            (By.XPATH, "//div[contains(@class, 'woocommerce_variation')]/h3/a[text()='Edit']"))
        self.sleep(2)
        variation_terms = self.get_elements((By.XPATH, "//div[@class='woocommerce_variation wc-metabox open']//select[contains(@name, 'attribute')]/option[@selected]"))
        variation_terms_name = []
        for i in range(len(variation_terms)):
            variation_terms_name.append(variation_terms[i].text)
        print(variation_terms_name)
        variation_boxes[variation_order].click()
        self.sleep(1)
        return variation_terms_name



