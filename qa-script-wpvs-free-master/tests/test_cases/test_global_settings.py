import pytest

from pages.GlobalSettings import GlobalSettings
from tests.BaseClass import BaseClass
from utilities.case_id import CaseID


# @pytest.mark.skip
@pytest.mark.order(8)
class TestGlobalSettings(BaseClass):
    section, option, displayed_property = '', '', True
    swatch_type = []

    def test_toggle_off_convert_all_dropdown_swatches_to_label_swatches(self):
        self.section = 'convert_to_label_swatches'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'off')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.displayed_property = globalSettings.check_global_settings(self.section, 'off', 'select')
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'disable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'disable_' + self.section)

    def test_toggle_on_convert_all_dropdown_swatches_to_label_swatches(self):
        self.section = 'convert_to_label_swatches'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'on')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.displayed_property = globalSettings.check_global_settings(self.section, 'on', 'select')
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'enable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'enable_' + self.section)

    def test_toggle_off_clear_on_reselect(self):
        self.section = 'clear_on_reselect'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'off')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.swatch_type = ['select', 'color', 'image', 'label']
        for i in range(len(self.swatch_type)):
            self.displayed_property = self.displayed_property and globalSettings.check_global_settings(self.section,
                                                                                                       'off',
                                                                                                       self.swatch_type[
                                                                                                           i])
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'disable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'disable_' + self.section)

    def test_toggle_on_clear_on_reselect(self):
        self.section = 'clear_on_reselect'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'on')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.swatch_type = ['select', 'color', 'image', 'label']
        for i in range(len(self.swatch_type)):
            self.displayed_property = self.displayed_property and globalSettings.check_global_settings(self.section,
                                                                                                       'on',
                                                                                                       self.swatch_type[
                                                                                                           i])
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'enable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'enable_' + self.section)

    def test_toggle_off_disable_swatches_plugin_stylesheet(self):
        self.section = 'disable_swatches_plugin_stylesheet'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'off')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.swatch_type = ['select', 'color', 'image', 'label']
        for i in range(len(self.swatch_type)):
            self.displayed_property = self.displayed_property and globalSettings.check_global_settings(self.section,
                                                                                                       'off',
                                                                                                       self.swatch_type[
                                                                                                           i])
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'disable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'disable_' + self.section)

    def test_toggle_on_disable_swatches_plugin_stylesheet(self):
        self.section = 'disable_swatches_plugin_stylesheet'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'on')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.swatch_type = ['select', 'color', 'image', 'label']
        for i in range(len(self.swatch_type)):
            self.displayed_property = self.displayed_property and globalSettings.check_global_settings(self.section,
                                                                                                       'on',
                                                                                                       self.swatch_type[
                                                                                                           i])
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'enable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'enable_' + self.section)

    def test_toggle_off_show_selected_variation_name_beside_attribute_label(self):
        self.section = 'show_selected_variation_name_beside_attribute_label'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings('disable_swatches_plugin_stylesheet', 'off')
        globalSettings.select_global_settings(self.section, 'off')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.swatch_type = ['select', 'color', 'image', 'label', 'radio']
        for i in range(len(self.swatch_type)):
            self.displayed_property = self.displayed_property and globalSettings.check_global_settings(self.section,
                                                                                                       'off',
                                                                                                       self.swatch_type[
                                                                                                           i])
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'disable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'disable_' + self.section)

    def test_toggle_on_show_selected_variation_name_beside_attribute_label(self):
        self.section = 'show_selected_variation_name_beside_attribute_label'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'on')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.swatch_type = ['select', 'color', 'image', 'label', 'radio']
        for i in range(len(self.swatch_type)):
            self.displayed_property = self.displayed_property and globalSettings.check_global_settings(self.section,
                                                                                                       'on',
                                                                                                       self.swatch_type[
                                                                                                           i])
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'enable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'enable_' + self.section)

    def test_toggle_off_enable_swatches_on_additional_info(self):
        self.section = 'enable_swatches_on_additional_info'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'off')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.swatch_type = ['select', 'color', 'image', 'label']
        for i in range(len(self.swatch_type)):
            self.displayed_property = self.displayed_property and globalSettings.check_global_settings(self.section,
                                                                                                       'off',
                                                                                                       self.swatch_type[
                                                                                                           i])
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'disable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'disable_' + self.section)

    def test_toggle_on_enable_swatches_on_additional_info(self):
        self.section = 'enable_swatches_on_additional_info'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, 'on')
        globalSettings.commonFunctions.launch_variable_product_page(0)
        self.swatch_type = ['select', 'color', 'image', 'label']
        for i in range(len(self.swatch_type)):
            self.displayed_property = self.displayed_property and globalSettings.check_global_settings(self.section,
                                                                                                       'on',
                                                                                                       self.swatch_type[
                                                                                                           i])
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, 'enable_' + self.section)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, 'enable_' + self.section)

    def test_behaviour_for_out_of_stock_variation_default(self):
        self.section = 'behaviour_for_out_of_stock_variation'
        self.option = 'default'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, self.option)
        globalSettings.assign_variation_as_out_of_stock()
        self.displayed_property = globalSettings.check_global_settings(self.section, self.option, 'label')
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, self.section + '_' + self.option)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, self.section + '_' + self.option)

    def test_behaviour_for_out_of_stock_variation_blur(self):
        self.section = 'behaviour_for_out_of_stock_variation'
        self.option = 'blur'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, self.option)
        self.displayed_property = globalSettings.check_global_settings(self.section, self.option, 'label')
        if self.displayed_property == '0.3':
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, self.section + '_' + self.option)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, self.section + '_' + self.option)

    def test_behaviour_for_out_of_stock_variation_blur_with_cross(self):
        self.section = 'behaviour_for_out_of_stock_variation'
        self.option = 'blur_with_cross'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, self.option)
        self.displayed_property = globalSettings.check_global_settings(self.section, self.option, 'label')
        if self.displayed_property == '1px':
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, self.section + '_' + self.option)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, self.section + '_' + self.option)

    def test_behaviour_for_unavailable_variation_hide(self):
        self.section = 'behaviour_for_unavailable_variation'
        self.option = 'hide'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, self.option)
        globalSettings.assign_variation_as_unavailable()
        self.displayed_property = globalSettings.check_global_settings(self.section, self.option, 'label')
        if self.displayed_property:
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, self.section + '_' + self.option)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, self.section + '_' + self.option)

    def test_behaviour_for_unavailable_variation_blur(self):
        self.section = 'behaviour_for_unavailable_variation'
        self.option = 'blur'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, self.option)
        self.displayed_property = globalSettings.check_global_settings(self.section, self.option, 'label')
        if self.displayed_property == '0.3':
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, self.section + '_' + self.option)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, self.section + '_' + self.option)

    def test_behaviour_for_unavailable_variation_blur_with_cross(self):
        self.section = 'behaviour_for_unavailable_variation'
        self.option = 'blur_with_cross'
        globalSettings = GlobalSettings(self.driver)
        globalSettings.select_global_settings(self.section, self.option)
        self.displayed_property = globalSettings.check_global_settings(self.section, self.option, 'label')
        if self.displayed_property == '1px':
            globalSettings.commonFunctions.update_test_run_pass(globalSettings.test_case_ids, self.section + '_' + self.option)
        else:
            globalSettings.commonFunctions.update_test_run_fail(globalSettings.test_case_ids, self.section + '_' + self.option)
