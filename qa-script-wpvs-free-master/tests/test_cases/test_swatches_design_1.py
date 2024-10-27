import pytest

from pages.ProductAttributes import ProductAttributes
from pages.SwatchesDesign import SwatchesDesign
from tests.BaseClass import BaseClass
from pages.LocalAttributes import LocalAttributes
from utilities.case_id import CaseID


# @pytest.mark.skip
@pytest.mark.order(7)
class TestSwatchDesign1(BaseClass):
    swatch_type, section, design_property, displayed_property = '', '', '', ''
    testrail_properties, design_properties, testrail_fields = [], [], []
    design_type = 'design_1'
    swatch_type_list = ['Color', 'Image', 'Label', 'Radio', 'Select']
    test_case_ids = CaseID.SWATCH_DESIGN_1

    # Common Attribute Styling Test Cases

    def test_valid_design_name(self):
        self.section = 'design_name'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
        swatchesDesign.reset_design_settings(1)
        productAttributes = ProductAttributes(self.driver)
        for i in range(0, len(self.swatch_type_list)):
            productAttributes.select_swatch_design(self.swatch_type_list[i], self.design_type)
        swatchesDesign.enter_common_attribute_styling(self.section, self.design_property)
        swatchesDesign.save_design_settings()
        swatchesDesign.commonFunctions.launch_variable_product_page(0)
        if swatchesDesign.check_design_styling(self.section, self.design_type, 'color'):
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_icon_height(self):
        self.section = 'icon_height'
        self.design_properties = ['icon_height', 'icon_width', 'icon_shape']
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
        for i in range(0, len(self.design_properties)):
            self.testrail_properties.append(swatchesDesign.commonFunctions.get_test_case_property(self.design_properties[i], self.design_properties[i]))
            swatchesDesign.enter_common_attribute_styling(self.design_properties[i], self.testrail_properties[i])
            print(self.testrail_properties[i], " ", self.design_properties[i])
        swatchesDesign.save_design_settings()
        swatchesDesign.commonFunctions.launch_variable_product_page(0)
        self.displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_icon_width(self):
        self.section = 'icon_width'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
        self.displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_icon_shape(self):
        self.section = 'icon_shape'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        if self.displayed_property == '50px':
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    # Hover and Border Styling Test Cases

    def test_border_color(self):
        self.section = 'border_color'
        self.design_properties = ['border_color', 'border_color_on_hover', 'border_color_on_selected',
                                  'color_image_selection_style_tick_color', 'color_image_selection_style_tick_size',
                                  'button_label_selection_style_tick_color', 'button_label_selection_style_tick_size']
        self.testrail_fields = ['border_color', 'border_color_on_hover', 'border_color_on_selected', 'tick_color',
                                'tick_size', 'tick_color', 'tick_size']
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
        self.testrail_properties.clear()
        for i in range(0, len(self.design_properties)):
            self.testrail_properties.append(
                swatchesDesign.commonFunctions.get_test_case_property(self.design_properties[i],
                                                                      self.testrail_fields[i]))
            swatchesDesign.enter_hover_and_border_styling(self.design_properties[i], self.testrail_properties[i])
            print(self.testrail_properties[i], " ", self.design_properties[i])
        swatchesDesign.save_design_settings()
        swatchesDesign.commonFunctions.launch_variable_product_page(0)
        self.displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_hover_border_color(self):
        self.section = 'border_color_on_hover'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
        self.displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_selected_border_color(self):
        self.section = 'border_color_on_selected'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
        self.displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_color_image_swatches_selection_style_tick_color(self):
        self.section = 'color_image_selection_style_tick_color'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'tick_color')
        displayed_property_1 = swatchesDesign.check_design_styling('swatches_selection_style_checkmark_tick_color',
                                                                   self.design_type,
                                                                   'color')
        displayed_property_2 = swatchesDesign.check_design_styling('swatches_selection_style_checkmark_tick_color',
                                                                   self.design_type,
                                                                   'image')
        if displayed_property_1 and displayed_property_2:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_color_image_swatches_selection_style_tick_size(self):
        self.section = 'color_image_selection_style_tick_size'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'tick_size')
        displayed_property_1 = swatchesDesign.check_design_styling('swatches_selection_style_checkmark_tick_size',
                                                                   self.design_type,
                                                                   'color')
        displayed_property_2 = swatchesDesign.check_design_styling('swatches_selection_style_checkmark_tick_size',
                                                                   self.design_type,
                                                                   'image')
        if displayed_property_1 and displayed_property_2:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatches_selection_style_tick_color(self):
        self.section = 'button_label_selection_style_tick_color'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'tick_color')
        self.displayed_property = swatchesDesign.check_design_styling('swatches_selection_style_checkmark_tick_color',
                                                                      self.design_type,
                                                                      'label')
        if self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatches_selection_style_tick_size(self):
        self.section = 'button_label_selection_style_tick_size'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'tick_size')
        self.displayed_property = swatchesDesign.check_design_styling('swatches_selection_style_checkmark_tick_size',
                                                                      self.design_type,
                                                                      'label')
        if self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatches_selection_style_background_color_on_hover(self):
        self.section = 'button_label_background_color_on_hover'
        self.design_properties = ['button_label_background_color_on_hover', 'button_label_text_color_on_hover',
                                  'button_label_background_color_on_selection', 'button_label_text_color_on_selection']
        self.testrail_fields = ['background_color_on_hover', 'text_color_on_hover', 'background_color_on_selected', 'text_color_on_selection']
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.testrail_properties.clear()
        for i in range(0, len(self.design_properties)):
            self.testrail_properties.append(
                swatchesDesign.commonFunctions.get_test_case_property(self.design_properties[i],
                                                                      self.testrail_fields[i]))
            swatchesDesign.enter_hover_and_border_styling(self.design_properties[i], self.testrail_properties[i])
            print(self.testrail_properties[i], " ", self.design_properties[i])
        swatchesDesign.save_design_settings()
        swatchesDesign.commonFunctions.launch_variable_product_page(0)
        self.displayed_property = swatchesDesign.check_design_styling('button_label_background_color_on_hover',
                                                                      self.design_type,
                                                                      'label')
        if self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatches_selection_style_text_color_on_hover(self):
        self.section = 'button_label_text_color_on_hover'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section,
                                                                                     'text_color_on_hover')
        self.displayed_property = swatchesDesign.check_design_styling(self.section,
                                                                      self.design_type,
                                                                      'label')
        if self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatches_selection_style_background_color_on_selection(self):
        self.section = 'button_label_background_color_on_selection'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section,
                                                                                     'background_color_on_selected')
        self.displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type,
                                                                      'label')
        if self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatches_selection_style_text_color_on_selection(self):
        self.section = 'button_label_text_color_on_selection'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section,
                                                                                     'text_color_on_selection')
        self.displayed_property = swatchesDesign.check_design_styling(self.section,
                                                                      self.design_type,
                                                                      'label')
        if self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    # # Tooltip styling

    def test_term_name_text_color(self):
        self.section = 'term_name_text_color'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        term_name_text_color = swatchesDesign.commonFunctions.get_test_case_property('term_name_text_color',
                                                                                     'text_color')
        term_name_background_color = swatchesDesign.commonFunctions.get_test_case_property('term_name_background_color',
                                                                                           'background_color')
        swatchesDesign.enter_tooltip_styling(self.section, term_name_text_color)
        swatchesDesign.enter_tooltip_styling('term_name_background_color', term_name_background_color)
        swatchesDesign.save_design_settings()
        swatchesDesign.commonFunctions.launch_variable_product_page(0)
        displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        if displayed_property == term_name_text_color:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_term_name_background_color(self):
        self.section = 'term_name_background_color'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        term_name_background_color = swatchesDesign.commonFunctions.get_test_case_property('term_name_background_color',
                                                                                           'background_color')
        displayed_property = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        if displayed_property == term_name_background_color:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    # # Swatch Type Specific Styling Test Cases

    def test_button_label_swatch_icon_height(self):
        self.section = 'button_label_icon_height'
        self.design_properties = ['button_label_icon_height', 'button_label_icon_width', 'button_label_font_size',
                                  'button_label_background_color', 'button_label_font_color']
        self.testrail_fields = ['icon_height', 'icon_width', 'font_size', 'background_color', 'text_color']
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'icon_height')
        self.testrail_properties.clear()
        for i in range(0, len(self.design_properties)):
            self.testrail_properties.append(swatchesDesign.commonFunctions.get_test_case_property(self.design_properties[i], self.testrail_fields[i]))
            swatchesDesign.enter_swatch_type_specific_styling(self.design_properties[i], self.testrail_properties[i])
            print(self.testrail_properties[i], " ", self.design_properties[i])
        swatchesDesign.save_design_settings()
        swatchesDesign.commonFunctions.launch_variable_product_page(0)
        self.displayed_property = swatchesDesign.check_design_styling('icon_height', self.design_type, 'label')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatch_icon_width(self):
        self.section = 'button_label_icon_width'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'icon_width')
        self.displayed_property = swatchesDesign.check_design_styling('icon_width', self.design_type, 'label')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatch_font_size(self):
        self.section = 'button_label_font_size'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'font_size')
        self.displayed_property = swatchesDesign.check_design_styling('font_size', self.design_type, 'label')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatch_background_color(self):
        self.section = 'button_label_background_color'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'background_color')
        self.displayed_property = swatchesDesign.check_design_styling('background_color', self.design_type, 'label')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_button_label_swatch_font_color(self):
        self.section = 'button_label_font_color'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'text_color')
        self.displayed_property = swatchesDesign.check_design_styling('font_color', self.design_type, 'label')
        if self.design_property == self.displayed_property:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_color_image_swatches_enable_swatch_dropdown(self):
        self.section = 'color_image_swatch_dropdown'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        swatchesDesign.enter_swatch_type_specific_styling(self.section, 'on')
        swatchesDesign.save_design_settings()
        swatchesDesign.commonFunctions.launch_variable_product_page(0)
        displayed_property_1 = swatchesDesign.check_design_styling(self.section, self.design_type, 'color')
        displayed_property_2 = swatchesDesign.check_design_styling(self.section, self.design_type, 'image')
        if displayed_property_1 and displayed_property_2:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)
        swatchesDesign.enter_swatch_type_specific_styling(self.section, 'off')
        swatchesDesign.save_design_settings()


