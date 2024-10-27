import pytest

from pages.GlobalAttributes import GlobalAttributes
from pages.LinkGlobalAttributes import LinkGlobalAttributes
from tests.BaseClass import BaseClass
from utilities.case_id import CaseID
from pages.LocalAttributes import LocalAttributes


# @pytest.mark.skip
@pytest.mark.order(3)
class TestLinkGlobalAttributes(BaseClass):
    attribute_name, term_name_one, term_name_two = '', '', ''
    swatch_type = ['select', 'color', 'image', 'label', 'radio']
    swatches_displayed = True

    def test_link_select_swatch_attribute_with_product(self):
        linkAttributes = LinkGlobalAttributes(self.driver)
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type[0])
        linkAttributes.commonFunctions.launch_variable_product_edit_page(0)
        linkAttributes.commonFunctions.navigate_to_attributes_tab()
        linkAttributes.commonFunctions.delete_attributes()
        linkAttributes.select_global_attributes(self.attribute_name)

    def test_link_color_swatch_attribute_with_product(self):
        linkAttributes = LinkGlobalAttributes(self.driver)
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type[1])
        linkAttributes.select_global_attributes(self.attribute_name)

    def test_link_image_swatch_attribute_with_product(self):
        linkAttributes = LinkGlobalAttributes(self.driver)
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type[2])
        linkAttributes.select_global_attributes(self.attribute_name)

    def test_link_label_swatch_attribute_with_product(self):
        linkAttributes = LinkGlobalAttributes(self.driver)
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type[3])
        linkAttributes.select_global_attributes(self.attribute_name)

    def test_link_radio_swatch_attribute_with_product(self):
        linkAttributes = LinkGlobalAttributes(self.driver)
        globalAttribute = GlobalAttributes(self.driver)
        self.attribute_name = globalAttribute.commonFunctions.get_attribute_name(self.swatch_type[4])
        linkAttributes.select_global_attributes(self.attribute_name)

    def test_create_variations_for_selected_attributes(self):
        linkAttributes = LinkGlobalAttributes(self.driver)
        linkAttributes.commonFunctions.launch_variable_product_edit_page(0)
        linkAttributes.commonFunctions.navigate_to_attributes_tab()
        linkAttributes.commonFunctions.generate_variations()
        linkAttributes.commonFunctions.assign_general_regular_price('500')
        linkAttributes.commonFunctions.assign_different_regular_prices('350')

    def test_check_product_page_for_global_attributes(self):
        global swatches_displayed
        linkAttributes = LinkGlobalAttributes(self.driver)
        linkAttributes.commonFunctions.remove_all_products_in_cart()
        linkAttributes.commonFunctions.launch_variable_product_page(0)
        for i in range(0, len(self.swatch_type)):
            self.attribute_name = linkAttributes.commonFunctions.get_attribute_name(self.swatch_type[i])
            self.term_name_one = linkAttributes.commonFunctions.get_term_name_one(self.swatch_type[i])
            self.term_name_two = linkAttributes.commonFunctions.get_term_name_two(self.swatch_type[i])
            linkAttributes.commonFunctions.choose_option_using_swatch_type(self.swatch_type[i], self.attribute_name,
                                                                           self.term_name_one)
        linkAttributes.commonFunctions.place_order()
        print('Order placed after selecting global attributes swatches options')
        print('Checking for global attributes swatches options in order details page')
        for i in range(0, len(self.swatch_type)):
            self.attribute_name = linkAttributes.commonFunctions.get_attribute_name(self.swatch_type[i]) + ':'
            self.term_name_one = linkAttributes.commonFunctions.get_term_name_one(self.swatch_type[i])
            self.term_name_two = linkAttributes.commonFunctions.get_term_name_two(self.swatch_type[i])
            swatches_displayed = linkAttributes.commonFunctions.check_swatches_in_order_details_page(self.swatch_type[i],
                                                                                self.attribute_name,
                                                                                self.term_name_one)
            swatches_displayed = swatches_displayed and self.swatches_displayed

        linkAttributes.commonFunctions.launch_orders_in_my_account_page()
        print('Checking for global attributes swatches options in my account orders page')
        for i in range(0, len(self.swatch_type)):
            self.attribute_name = linkAttributes.commonFunctions.get_attribute_name(self.swatch_type[i]) + ':'
            self.term_name_one = linkAttributes.commonFunctions.get_term_name_one(self.swatch_type[i])
            self.term_name_two = linkAttributes.commonFunctions.get_term_name_two(self.swatch_type[i])
            swatches_displayed = linkAttributes.commonFunctions.check_swatches_in_order_details_page(self.swatch_type[i],
                                                                                self.attribute_name, self.term_name_one)
            swatches_displayed = swatches_displayed and self.swatches_displayed
        if swatches_displayed:
            linkAttributes.update_test_run_pass(linkAttributes.commonFunctions.test_case_ids, 'link_attributes')
        else:
            linkAttributes.update_test_run_fail(linkAttributes.commonFunctions.test_case_ids, 'link_attributes')
