import pytest

from pages.ProductAttributes import ProductAttributes
from pages.SwatchesDesign import SwatchesDesign
from tests.BaseClass import BaseClass
from pages.LocalAttributes import LocalAttributes
from utilities.case_id import CaseID


# @pytest.mark.skip
@pytest.mark.order(6)
class TestSwatchDefaultDesign(BaseClass):
    swatch_type, section, design_property, displayed_property = '', '', '', ''
    design_type = 'default'
    swatch_type_list = ['Color', 'Image', 'Label', 'Radio', 'Select']
    test_case_ids = CaseID.DEFAULT_DESIGN

    # Common Attribute Styling Test Cases

    def test_valid_design_name(self):
        self.section = 'design_name'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
        swatchesDesign.reset_design_settings(0)
        productAttributes = ProductAttributes(self.driver)
        for i in range(0, len(self.swatch_type_list)):
            productAttributes.select_swatch_design(self.swatch_type_list[i], self.design_type+'_design')
        swatchesDesign.commonFunctions.launch_variable_product_page(0)
        if swatchesDesign.check_design_styling(self.section, self.design_type, 'color'):
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_icon_height(self):
        self.section = 'icon_height'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
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
        if self.displayed_property == '2px':
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    # Hover and Border Styling Test Cases

    def test_border_color(self):
        self.section = 'border_color'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, self.section)
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

    def test_color_image_swatches_selection_style(self):
        self.section = 'color_image_selection_style_borders_on_selection'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        displayed_property_1 = swatchesDesign.check_design_styling('swatches_selection_style_border_on_selection', self.design_type, 'color')
        displayed_property_2 = swatchesDesign.check_design_styling('swatches_selection_style_border_on_selection', self.design_type, 'image')
        if int(displayed_property_1) > 1 and int(displayed_property_2) > 1:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    def test_color_label_button_swatches_selection_style(self):
        self.section = 'button_label_selection_style_borders_on_selection'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.displayed_property = swatchesDesign.check_design_styling('swatches_selection_style_border_on_selection', self.design_type, 'label')
        if int(self.displayed_property) > 1:
            swatchesDesign.update_test_run_pass(self.test_case_ids, self.section)
        else:
            swatchesDesign.update_test_run_fail(self.test_case_ids, self.section)

    # Swatch Type Specific Styling Test Cases

    def test_button_label_swatch_icon_height(self):
        self.section = 'button_label_icon_height'
        swatchesDesign = SwatchesDesign(self.driver, self.test_case_ids)
        self.design_property = swatchesDesign.commonFunctions.get_test_case_property(self.section, 'icon_height')
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