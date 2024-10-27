import time

import pytest

from pages.GlobalSettings import GlobalSettings
from pages.LocalAttributes import LocalAttributes
from tests.BaseClass import BaseClass
from utilities.case_id import CaseID
from pages.GlobalAttributes import GlobalAttributes

# @pytest.mark.skip
@pytest.mark.order(2)
class TestCreateGlobalAttributes(BaseClass):
    attribute_name, swatch_type = '', ''

    def test_create_select_swatch_type_global_attribute(self):
        self.swatch_type = 'select'
        globalAttribute = GlobalAttributes(self.driver)
        globalSettings = GlobalSettings(self.driver)
        globalSettings.click_reset_global_settings()
        globalSettings.select_global_settings('lazy_load', 'on')
        globalSettings.enter_ajax_threshold('60')
        localAttributes = LocalAttributes(self.driver)
        localAttributes.commonFunctions.launch_variable_product_edit_page(0)
        localAttributes.commonFunctions.navigate_to_attributes_tab()
        localAttributes.commonFunctions.delete_attributes()
        globalAttribute.delete_all_attributes()
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type)
        globalAttribute.create_attribute_name(self.swatch_type, globalAttribute.commonFunctions.get_attribute_name(self.swatch_type))
        globalAttribute.create_new_term(self.swatch_type, globalAttribute.commonFunctions.get_term_name_one(self.swatch_type), '')
        globalAttribute.create_new_term(self.swatch_type, globalAttribute.commonFunctions.get_term_name_two(self.swatch_type), '')
        if globalAttribute.is_attribute_created(self.attribute_name):
            globalAttribute.update_test_run_pass(globalAttribute.test_case_ids, self.swatch_type)
        else:
            globalAttribute.update_test_run_fail(globalAttribute.test_case_ids, self.swatch_type)

    def test_create_color_swatch_type_global_attribute(self):
        self.swatch_type = 'color'
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type)
        globalAttribute.create_attribute_name(self.swatch_type, globalAttribute.commonFunctions.get_attribute_name(self.swatch_type))
        globalAttribute.create_new_term(self.swatch_type, globalAttribute.commonFunctions.get_term_name_one(self.swatch_type),
                                        globalAttribute.commonFunctions.get_term_color_one(self.swatch_type))
        globalAttribute.create_new_term(self.swatch_type, globalAttribute.commonFunctions.get_term_name_two(self.swatch_type),
                                        globalAttribute.commonFunctions.get_term_color_two(self.swatch_type))
        if globalAttribute.is_attribute_created(self.attribute_name):
            globalAttribute.update_test_run_pass(globalAttribute.test_case_ids, self.swatch_type)
        else:
            globalAttribute.update_test_run_fail(globalAttribute.test_case_ids, self.swatch_type)

    def test_create_image_swatch_type_global_attribute(self):
        self.swatch_type = 'image'
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type)
        globalAttribute.create_attribute_name(self.swatch_type, globalAttribute.commonFunctions.get_attribute_name(self.swatch_type))
        globalAttribute.create_new_term('image_1', globalAttribute.commonFunctions.get_term_name_one(self.swatch_type), '')
        globalAttribute.create_new_term('image_2', globalAttribute.commonFunctions.get_term_name_two(self.swatch_type), '')
        if globalAttribute.is_attribute_created(self.attribute_name):
            globalAttribute.update_test_run_pass(globalAttribute.test_case_ids, self.swatch_type)
        else:
            globalAttribute.update_test_run_fail(globalAttribute.test_case_ids, self.swatch_type)

    def test_create_label_swatch_type_global_attribute(self):
        self.swatch_type = 'label'
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type)
        globalAttribute.commonFunctions.launch_edit_product_attributes_page()
        globalAttribute.create_attribute_name(self.swatch_type, globalAttribute.commonFunctions.get_attribute_name(self.swatch_type))
        globalAttribute.create_new_term(self.swatch_type, globalAttribute.commonFunctions.get_term_name_one(self.swatch_type),
                                        globalAttribute.commonFunctions.get_term_label_one(self.swatch_type))
        globalAttribute.create_new_term(self.swatch_type, globalAttribute.commonFunctions.get_term_name_two(self.swatch_type),
                                        globalAttribute.commonFunctions.get_term_label_two(self.swatch_type))
        if globalAttribute.is_attribute_created(self.attribute_name):
            globalAttribute.update_test_run_pass(globalAttribute.test_case_ids, self.swatch_type)
        else:
            globalAttribute.update_test_run_fail(globalAttribute.test_case_ids, self.swatch_type)

    def test_create_radio_swatch_type_global_attribute(self):
        self.swatch_type = 'radio'
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type)
        globalAttribute.create_attribute_name(self.swatch_type, globalAttribute.commonFunctions.get_attribute_name(self.swatch_type))
        globalAttribute.create_new_term(self.swatch_type, globalAttribute.commonFunctions.get_term_name_one(self.swatch_type), '')
        globalAttribute.create_new_term(self.swatch_type, globalAttribute.commonFunctions.get_term_name_two(self.swatch_type), '')
        if globalAttribute.is_attribute_created(self.attribute_name):
            globalAttribute.update_test_run_pass(globalAttribute.test_case_ids, self.swatch_type)
        else:
            globalAttribute.update_test_run_fail(globalAttribute.test_case_ids, self.swatch_type)
