import pytest

from pages.GlobalAttributes import GlobalAttributes
from tests.BaseClass import BaseClass
from utilities.case_id import CaseID
from pages.LocalAttributes import LocalAttributes

# @pytest.mark.skip
@pytest.mark.order(4)
class TestCreateLocalAttributes(BaseClass):
    attribute_name, term_values, swatch_type, term_property_1, term_property_2 = '', '', '', '', ''
    swatches_displayed = True
    swatch_type_list = ['select', 'color', 'image', 'label', 'radio']

    def test_create_local_select_swatch_attribute_with_product(self):
        self.swatch_type = 'select'
        localAttributes = LocalAttributes(self.driver)
        self.attribute_name = localAttributes.commonFunctions.get_attribute_name(self.swatch_type)
        self.term_values = localAttributes.commonFunctions.get_term_name_one(self.swatch_type) + '|' + localAttributes.commonFunctions.get_term_name_two(self.swatch_type)
        localAttributes.commonFunctions.launch_variable_product_edit_page(1)
        localAttributes.commonFunctions.navigate_to_attributes_tab()
        localAttributes.commonFunctions.delete_attributes()
        localAttributes.create_local_attribute('0', self.attribute_name, self.term_values, self.swatch_type, '', '')
        if localAttributes.is_local_attribute_created(self.attribute_name):
            localAttributes.update_test_run_pass(localAttributes.test_case_ids, self.swatch_type)
        else:
            localAttributes.update_test_run_fail(localAttributes.test_case_ids, self.swatch_type)

    def test_create_local_color_swatch_attribute_with_product(self):
        self.swatch_type = 'color'
        localAttributes = LocalAttributes(self.driver)
        self.attribute_name = localAttributes.commonFunctions.get_attribute_name(self.swatch_type)
        self.term_values = localAttributes.commonFunctions.get_term_name_one(self.swatch_type) + '|' + localAttributes.commonFunctions.get_term_name_two(self.swatch_type)
        self.term_property_1 = localAttributes.commonFunctions.get_term_color_one(self.swatch_type)
        self.term_property_2 = localAttributes.commonFunctions.get_term_color_two(self.swatch_type)
        localAttributes.create_local_attribute('1', self.attribute_name, self.term_values, self.swatch_type, self.term_property_1, self.term_property_2)
        if localAttributes.is_local_attribute_created(self.attribute_name):
            localAttributes.update_test_run_pass(localAttributes.test_case_ids, self.swatch_type)
        else:
            localAttributes.update_test_run_fail(localAttributes.test_case_ids, self.swatch_type)

    def test_create_local_image_swatch_attribute_with_product(self):
        self.swatch_type = 'image'
        localAttributes = LocalAttributes(self.driver)
        self.attribute_name = localAttributes.commonFunctions.get_attribute_name(self.swatch_type)
        self.term_values = localAttributes.commonFunctions.get_term_name_one(
            self.swatch_type) + '|' + localAttributes.commonFunctions.get_term_name_two(self.swatch_type)
        localAttributes.create_local_attribute('2', self.attribute_name, self.term_values, self.swatch_type, '', '')
        if localAttributes.is_local_attribute_created(self.attribute_name):
            localAttributes.update_test_run_pass(localAttributes.test_case_ids, self.swatch_type)
        else:
            localAttributes.update_test_run_fail(localAttributes.test_case_ids, self.swatch_type)

    def test_create_local_label_swatch_attribute_with_product(self):
        self.swatch_type = 'label'
        localAttributes = LocalAttributes(self.driver)
        self.attribute_name = localAttributes.commonFunctions.get_attribute_name(self.swatch_type)
        self.term_values = localAttributes.commonFunctions.get_term_name_one(self.swatch_type) + '|' + localAttributes.commonFunctions.get_term_name_two(self.swatch_type)
        self.term_property_1 = localAttributes.commonFunctions.get_term_label_one(self.swatch_type)
        self.term_property_2 = localAttributes.commonFunctions.get_term_label_two(self.swatch_type)
        localAttributes.create_local_attribute('3', self.attribute_name, self.term_values, self.swatch_type,  self.term_property_1, self.term_property_2)
        if localAttributes.is_local_attribute_created(self.attribute_name):
            localAttributes.update_test_run_pass(localAttributes.test_case_ids, self.swatch_type)
        else:
            localAttributes.update_test_run_fail(localAttributes.test_case_ids, self.swatch_type)

    def test_create_local_radio_swatch_attribute_with_product(self):
        self.swatch_type = 'radio'
        localAttributes = LocalAttributes(self.driver)
        self.attribute_name = localAttributes.commonFunctions.get_attribute_name(self.swatch_type)
        self.term_values = localAttributes.commonFunctions.get_term_name_one(self.swatch_type) + '|' + localAttributes.commonFunctions.get_term_name_two(self.swatch_type)
        localAttributes.create_local_attribute('4', self.attribute_name, self.term_values, self.swatch_type, '', '')
        if localAttributes.is_local_attribute_created(self.attribute_name):
            localAttributes.update_test_run_pass(localAttributes.test_case_ids, self.swatch_type)
        else:
            localAttributes.update_test_run_fail(localAttributes.test_case_ids, self.swatch_type)

    def test_create_variations_for_local_attributes(self):
        localAttributes = LocalAttributes(self.driver)
        localAttributes.commonFunctions.launch_variable_product_edit_page(1)
        localAttributes.commonFunctions.navigate_to_attributes_tab()
        localAttributes.commonFunctions.generate_variations()
        localAttributes.commonFunctions.assign_general_regular_price('350')
        localAttributes.commonFunctions.assign_different_regular_prices('300')
        localAttributes.commonFunctions.check_product_update_success_message()

    def test_check_product_page_for_local_attributes(self):
        global swatches_displayed
        localAttributes = LocalAttributes(self.driver)
        localAttributes.commonFunctions.remove_all_products_in_cart()
        localAttributes.commonFunctions.launch_variable_product_page(1)
        for i in range(0, len(self.swatch_type_list)):
            self.attribute_name = localAttributes.commonFunctions.get_attribute_name(self.swatch_type_list[i])
            self.term_name_one = localAttributes.commonFunctions.get_term_name_one(self.swatch_type_list[i])
            self.term_name_two = localAttributes.commonFunctions.get_term_name_two(self.swatch_type_list[i])
            localAttributes.commonFunctions.choose_option_using_swatch_type(self.swatch_type_list[i], self.attribute_name,
                                                                           self.term_name_one)
        localAttributes.commonFunctions.place_order()
        print('Order placed after selecting local attributes swatches options')
        print('Checking for local attributes swatches options in order details page')
        for i in range(0, len(self.swatch_type_list)):
            self.attribute_name = localAttributes.commonFunctions.get_attribute_name(self.swatch_type_list[i]) + ':'
            self.term_name_one = localAttributes.commonFunctions.get_term_name_one(self.swatch_type_list[i])
            self.term_name_two = localAttributes.commonFunctions.get_term_name_two(self.swatch_type_list[i])
            swatches_displayed = localAttributes.commonFunctions.check_swatches_in_order_details_page(self.swatch_type_list[i],
                                                                                self.attribute_name,
                                                                                self.term_name_one)
            swatches_displayed = swatches_displayed and self.swatches_displayed

        localAttributes.commonFunctions.launch_orders_in_my_account_page()
        print('Checking for local attributes swatches options in my account orders page')
        for i in range(0, len(self.swatch_type_list)):
            self.attribute_name = localAttributes.commonFunctions.get_attribute_name(self.swatch_type_list[i]) + ':'
            self.term_name_one = localAttributes.commonFunctions.get_term_name_one(self.swatch_type_list[i])
            self.term_name_two = localAttributes.commonFunctions.get_term_name_two(self.swatch_type_list[i])
            swatches_displayed = localAttributes.commonFunctions.check_swatches_in_order_details_page(self.swatch_type_list[i],
                                                                                self.attribute_name, self.term_name_one)
            swatches_displayed = swatches_displayed and self.swatches_displayed
        if swatches_displayed:
            localAttributes.update_test_run_pass(localAttributes.commonFunctions.test_case_ids, 'link_attributes')
        else:
            localAttributes.update_test_run_fail(localAttributes.commonFunctions.test_case_ids, 'link_attributes')
