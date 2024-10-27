from selenium.webdriver.common.by import By

from config import TestData
from pages.BasePage import BasePage
from pages.CommonFunctions import CommonFunctions
from utilities.case_id import CaseID


class SwatchesDesign(BasePage):
    displayed_property, border = '', ''
    design_name = (By.NAME, "i_design_name")
    icon_height = (By.NAME, "i_icon_height")
    icon_width = (By.NAME, "i_icon_width")
    design_save_settings = (By.NAME, "design_save_settings")
    design_reset_settings = (By.XPATH, "//aside//input[@name='design_reset_settings']")
    icon_shape = (By.NAME, "i_icon_shape")
    hover_border_styling_section = (By.XPATH, "//span[text()='Hover and Border Styling']")
    icon_border_color = (By.NAME, "i_icon_border_color")
    icon_border_color_hover = (By.NAME, "i_icon_border_color_hover")
    icon_border_color_selected = (By.NAME, "i_icon_border_color_selected")
    tool_tip_styling_section = (By.XPATH, "//span[text()='Tooltip Styling']")
    icon_label_height = (By.NAME, "i_icon_label_height")
    icon_label_width = (By.NAME, "i_icon_label_width")
    label_size = (By.NAME, "i_label_size")
    label_background_color = (By.NAME, "i_label_background_color")
    label_background_color_title = (By.XPATH, "//input[@name='i_label_background_color']/ancestor::tr/td[@class='titledesc']")
    label_text_color = (By.NAME, "i_label_text_color")
    label_text_color_title = (By.XPATH, "//input[@name='i_label_text_color']/ancestor::tr/td[@class='titledesc']")
    swatch_type_specific_styling_section = (By.XPATH, "//span[text()='Swatch Type Specific Styling']")
    color_image_selection_style_label = (By.XPATH, "//td[contains(text(), 'Color,Image Selection Style')]")
    button_label_selection_style_label = (By.XPATH, "//td[contains(text(), 'Button/Label Selection Style')]")
    common_swatches_selection_style = (By.NAME, "i_common_selection_style")
    label_selection_style = (By.NAME, "i_label_selection_style")
    common_tick_color = (By.NAME, "i_tick_color")
    common_tick_size = (By.NAME, "i_tick_size")
    label_tick_size = (By.NAME, "i_label_tick_size")
    label_tick_color = (By.NAME, "i_label_tick_color")
    label_background_color_hover = (By.NAME, "i_label_background_color_hover")
    label_text_color_hover = (By.NAME, "i_label_text_color_hover")
    label_background_color_selection = (By.NAME, "i_label_background_color_selection")
    label_text_color_selection = (By.NAME, "i_label_text_color_selection")
    enable_tooltip_toggle = (By.XPATH, "//label[@for='i_tooltip_enable']")
    enable_tooltip_checkbox = (By.NAME, "i_tooltip_enable" )
    term_name_text_color = (By.NAME, "i_tooltip_text_color")
    term_name_background_color = (By.NAME, "i_tooltip_text_background_color")
    tooltip_class = (By.XPATH, "//*[contains(@class, 'tooltiptext')]")
    enable_swatch_dropdown_toggle = (By.XPATH, "//label[@for='i_enable_swatch_dropdown']")
    enable_swatch_dropdown_checkbox = (By.NAME, "i_enable_swatch_dropdown")

    def __init__(self, driver, test_case_ids):
        super().__init__(driver)
        self.commonFunctions = CommonFunctions(self.driver, test_case_ids)

    def launch_swatches_design(self):
        self.launch_page(TestData.SWATCHES_DESIGN_URL)

    def edit_design_type(self, design_order):
        self.launch_swatches_design()
        design_templates_edit = self.get_elements(
            (By.XPATH, "//div[@class='thwvs-template-box']//span[@class='icon icon-edit']"))
        self.sleep(2)
        self.move_to_element(design_templates_edit[design_order])
        self.do_click(design_templates_edit[design_order])

    def reset_design_settings(self, design_type_order):
        self.edit_design_type(design_type_order)
        self.sleep(5)
        self.do_click(self.design_reset_settings)
        self.sleep(3)
        self.alert_accept()
        self.sleep(3)
        print('Design settings is reset')

    def save_design_settings(self):
        self.do_click(self.design_save_settings)

    def enter_common_attribute_styling(self, design_property, value):
        if design_property == 'design_name':
            self.edit_design_type(1)
            self.text_clear(self.design_name)
            self.do_sendkeys(self.design_name, value)
        elif design_property == 'icon_height':
            self.edit_design_type(1)
            self.text_clear(self.icon_height)
            self.do_sendkeys(self.icon_height, value)
        elif design_property == 'icon_width':
            self.text_clear(self.icon_width)
            self.do_sendkeys(self.icon_width, value)
        elif design_property == 'icon_shape':
            self.select_element_from_dropdown_by_value(self.icon_shape, "round")
        self.sleep(3)

    def enter_hover_and_border_styling(self, design_property, value):
        match design_property:
            case 'border_color':
                self.edit_design_type(1)
                self.do_click(self.hover_border_styling_section)
                self.text_clear(self.icon_border_color)
                self.do_sendkeys(self.icon_border_color, value)
            case 'border_color_on_hover':
                self.text_clear(self.icon_border_color_hover)
                self.do_sendkeys(self.icon_border_color_hover, value)
            case 'border_color_on_selected':
                self.text_clear(self.icon_border_color_selected)
                self.do_sendkeys(self.icon_border_color_selected, value)
            case 'color_image_selection_style_tick_color':
                self.do_click(self.color_image_selection_style_label)
                self.sleep(2)
                self.select_element_from_dropdown_by_value(self.common_swatches_selection_style, 'border_with_tick')
                self.text_clear(self.common_tick_color)
                self.do_sendkeys(self.common_tick_color, value)
            case 'color_image_selection_style_tick_size':
                self.text_clear(self.common_tick_size)
                self.do_sendkeys(self.common_tick_size, value)
            case 'button_label_selection_style_tick_color':
                self.do_click(self.button_label_selection_style_label)
                self.sleep(2)
                self.select_element_from_dropdown_by_value(self.label_selection_style, 'border_with_tick')
                self.text_clear(self.label_tick_color)
                self.do_sendkeys(self.label_tick_color, value)
            case 'button_label_selection_style_tick_size':
                self.text_clear(self.label_tick_size)
                self.do_sendkeys(self.label_tick_size, value)
            case 'button_label_background_color_on_hover':
                self.edit_design_type(1)
                self.do_click(self.hover_border_styling_section)
                self.select_element_from_dropdown_by_value(self.label_selection_style, 'background_color')
                self.text_clear(self.label_background_color_hover)
                self.do_sendkeys(self.label_background_color_hover, value)
            case 'button_label_text_color_on_hover':
                self.text_clear(self.label_text_color_hover)
                self.do_sendkeys(self.label_text_color_hover, value)
            case 'button_label_background_color_on_selection':
                self.text_clear(self.label_background_color_selection)
                self.do_sendkeys(self.label_background_color_selection, value)
            case 'button_label_text_color_on_selection':
                self.text_clear(self.label_text_color_selection)
                self.do_sendkeys(self.label_text_color_selection, value)
        self.sleep(3)

    def enter_tooltip_styling(self, design_property, value):
        match design_property:
            case 'term_name_text_color':
                self.edit_design_type(1)
                self.do_click(self.tool_tip_styling_section)
                if not self.is_element_selected(self.enable_tooltip_checkbox):
                    self.do_click(self.enable_tooltip_toggle)
                self.text_clear(self.term_name_text_color)
                self.do_sendkeys(self.term_name_text_color, value)
            case 'term_name_background_color':
                self.text_clear(self.term_name_background_color)
                self.do_sendkeys(self.term_name_background_color, value)
        self.sleep(3)

    def enter_swatch_type_specific_styling(self, design_property, value):
        match design_property:
            case 'button_label_icon_height':
                self.edit_design_type(1)
                self.do_click(self.swatch_type_specific_styling_section)
                self.text_clear(self.icon_label_height)
                self.do_sendkeys(self.icon_label_height, value)
            case 'button_label_icon_width':
                self.text_clear(self.icon_label_width)
                self.do_sendkeys(self.icon_label_width, value)
            case 'button_label_font_size':
                self.text_clear(self.label_size)
                self.do_sendkeys(self.label_size, value)
            case 'button_label_background_color':
                self.text_clear(self.label_background_color)
                self.do_sendkeys(self.label_background_color, value)
                self.do_click(self.label_background_color_title)
            case 'button_label_font_color':
                self.text_clear(self.label_text_color)
                self.do_sendkeys(self.label_text_color, value)
                self.do_click(self.label_text_color_title)
            case 'color_image_swatch_dropdown':
                self.edit_design_type(1)
                self.do_click(self.swatch_type_specific_styling_section)
                if value == 'on':
                    if not self.is_element_selected(self.enable_swatch_dropdown_checkbox):
                        self.do_click(self.enable_swatch_dropdown_toggle)
                else:
                    if self.is_element_selected(self.enable_swatch_dropdown_checkbox):
                        self.do_click(self.enable_swatch_dropdown_toggle)
        self.sleep(3)

    def check_design_styling(self, design_property, design_type, swatch_type):
        attribute_name = self.commonFunctions.get_attribute_name(swatch_type).lower()
        swatch_element = (By.XPATH, "//li[contains(@class, 'attribute_pa_"+attribute_name+"')]")
        swatch_element_text = (By.XPATH, "//li[contains(@class, 'attribute_pa_"+attribute_name+"')]/span[contains(@class, 'thwvsf-item-span item-span-text')]")
        match design_property:
            case 'design_name':
                self.displayed_property = self.is_element_displayed((By.XPATH, "//select[contains(@id,'"+attribute_name+"') and contains(@data-design_type,'" + design_type + "')]"))
            case 'icon_height':
                self.displayed_property = self.get_css_property(swatch_element, 'height')
            case 'icon_width':
                self.displayed_property = self.get_css_property(swatch_element, 'width')
            case 'icon_shape':
                self.displayed_property = self.get_css_property(swatch_element, 'border-radius')
            case 'border_color':
                self.border = self.get_css_property(swatch_element, 'box-shadow').split(')')
                self.displayed_property = self.get_hex(self.border[0] + ')')
            case 'background_color':
                self.displayed_property = self.get_hex(self.get_css_property(swatch_element, 'background-color'))
            case 'font_color':
                self.displayed_property = self.get_hex(self.get_css_property(swatch_element, 'color'))
            case 'font_size':
                self.displayed_property = self.get_css_property(swatch_element_text, 'font-size')
            case 'border_color_on_hover':
                self.move_to_swatch_element(swatch_element)
                self.border = self.get_css_property(swatch_element, 'box-shadow').split(')')
                self.displayed_property = self.get_hex(self.border[0] + ')')
            case 'border_color_on_selected':
                self.click_swatch_element(swatch_element)
                self.border = self.get_css_property(swatch_element, 'box-shadow').split(')')
                self.displayed_property = self.get_hex(self.border[0] + ')')
            case 'swatches_selection_style_border_on_selection':
                self.click_swatch_element(swatch_element)
                self.border = self.get_css_property(swatch_element, 'box-shadow').split('px')
                self.displayed_property = (self.border[3])
            case 'swatches_selection_style_checkmark_tick_color':
                self.click_swatch_element(swatch_element)
                tick = self.get_element(swatch_element)
                self.displayed_property = self.get_hex(self.driver.execute_script(
                    "return window.getComputedStyle(arguments[0], ':after').getPropertyValue('color');", tick))
            case 'swatches_selection_style_checkmark_tick_size':
                self.click_swatch_element(swatch_element)
                tick = self.get_element(swatch_element)
                self.displayed_property = self.driver.execute_script(
                    "return window.getComputedStyle(arguments[0], ':after').getPropertyValue('font-size');", tick)
            case 'button_label_background_color_on_hover':
                self.move_to_swatch_element(swatch_element)
                self.displayed_property = self.get_hex(self.get_css_property(swatch_element, 'background-color'))
            case 'button_label_text_color_on_hover':
                self.move_to_swatch_element(swatch_element)
                self.displayed_property = self.get_hex(self.get_css_property(swatch_element, 'color'))
            case 'button_label_background_color_on_selection':
                self.click_swatch_element(swatch_element)
                self.displayed_property = self.get_hex(self.get_css_property(swatch_element, 'background-color'))
            case 'button_label_text_color_on_selection':
                self.click_swatch_element(swatch_element)
                self.displayed_property = self.get_hex(self.get_css_property(swatch_element, 'color'))
            case 'term_name_text_color':
                self.displayed_property = self.get_hex(self.get_css_property(self.tooltip_class, 'color'))
            case 'term_name_background_color':
                self.displayed_property = self.get_hex(self.get_css_property(self.tooltip_class, 'background-color'))
            case 'color_image_swatch_dropdown':
                self.displayed_property = self.is_element_displayed((By.XPATH, "//*[contains(@data-swatchtype,'swatch_dropdown_"+swatch_type+"')]"))
        print('Displayed property value::', self.displayed_property)
        return self.displayed_property

    def click_swatch_element(self, swatch_element):
        self.scroll_element_into_view(swatch_element)
        self.sleep(2)
        self.do_click(swatch_element)
        self.sleep(2)

    def move_to_swatch_element(self, swatch_element):
        self.scroll_element_into_view(swatch_element)
        self.sleep(2)
        self.move_to_element(self.get_element(swatch_element))
        self.sleep(2)
