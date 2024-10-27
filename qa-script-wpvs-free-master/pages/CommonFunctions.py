from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By

from config import TestData
from pages.BasePage import BasePage
from utilities.case_id import CaseID
from utilities.helper import get_id_property


class CommonFunctions(BasePage):
    image_upload_button = (By.XPATH, "//button[contains(@class,'thwvsf-upload-image-button')]")
    upload_files_button = (By.XPATH, "//button[text()='Upload files']")
    media_library_tab = (By.XPATH, "//button[text()='Media Library']")
    select_files_button = (By.XPATH, "//button[text()='Select Files']")
    attachments_wrapper = (By.XPATH, "//div[@class='attachments-wrapper']")
    first_image = (By.XPATH, "//*[contains(@id,'attachments-view')]/li[1]/div/div")
    second_image = (By.XPATH, "//*[contains(@id,'attachments-view')]/li[2]/div/div")
    choose_image_button = (By.XPATH, "//div[@class='media-toolbar']//button[contains(text(),'Choose Image')]")
    variable_product_options = (By.XPATH, "//div[@id='variable_product_options']")
    variable_product_name = (By.XPATH, "//a[contains(text(), 'Select options')]")
    variable_product_link = (By.XPATH, "//a[contains(text(), 'Select options')]/preceding-sibling::a")
    product_search_field = (By.XPATH, "//input[@id='post-search-input']")
    search_submit = (By.ID, "search-submit")
    product_data = (By.XPATH, "//div[@class='postbox-header']/h2[text()='Product data']")
    product_image = (By.XPATH, "//div[@class='postbox-header']/h2[text()='Product image']")
    product_description = (By.XPATH, "//div[@class='postbox-header']/h2[text()='Product short description']")
    attributes_tab = (By.XPATH, "//span[text()='Attributes']/parent::a")
    actions_bar = (By.XPATH, "//div[@class='actions']")
    remove_attribute = (
        By.XPATH, "//div[contains(@class,'woocommerce_attribute wc-metabox postbox')]//a[text()='Remove']")
    select_all_button = (By.XPATH, "//button[text()='Select all']")
    save_attributes_button = (By.XPATH, "//button[text()='Save attributes']")
    variations_tab = (By.XPATH, "//span[text()='Variations']/parent::a")
    generate_variations_button = (By.XPATH, "//button[text()='Generate variations']")
    zero_variations_message = (By.XPATH,
                               "//div[@class='components-snackbar__content components-snackbar__content-with-icon'][contains(text(), '0 variations added')]")
    add_price_button = (By.XPATH, "//button[text()='Add price']")
    variation_price_input_field = (
        By.XPATH, "//div[@class='woocommerce-usage-modal__message']/input[contains(@class,'input_variations_price')]")
    add_prices_button = (By.XPATH, "//button[text()='Add prices']")
    page_selector = (By.XPATH, "//select[@class='page-selector'][1]")
    variations_table = (By.XPATH, "//div[@class='woocommerce_variations wc-metaboxes ui-sortable']")
    variation_actions = (By.XPATH, "//select[@class='select variation_actions']")
    close_variations = (By.XPATH, "//div[@class='variations-pagenav']//a[text()='Close'][1]")
    save_changes = (By.XPATH, "//button[text()='Save changes']")
    update_button = (By.XPATH, "//input[@id='publish']")
    success_message = (
        By.XPATH, "//div[contains(@class,'notice notice-success')]/p[contains(text(),'Product updated')]")
    product_page_link = (By.XPATH, "//span[@id='sample-permalink']/a")
    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
    place_order_button = (By.XPATH, "//div[@class='form-row place-order']/button[text()='Place order']")
    order_page_view_buttons = (By.XPATH, "//a[text()='View']")
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    billing_first_name = (By.ID, "billing_first_name")
    billing_last_name = (By.ID, "billing_last_name")
    billing_address_1 = (By.ID, "billing_address_1")
    billing_city = (By.ID, "billing_city")
    billing_postcode = (By.ID, "billing_postcode")
    billing_country = (By.ID, "billing_country")
    billing_state = (By.ID, "billing_state")
    billing_email = (By.ID, "billing_email")
    billing_phone = (By.ID, "billing_phone")
    order_received_heading = (By.XPATH, "//h1[text()='Order received']")

    def __init__(self, driver, test_case_ids):
        super().__init__(driver)
        self.test_case_ids = test_case_ids

    def launch_edit_product_attributes_page(self):
        self.launch_page(TestData.EDIT_PRODUCT_ATTRIBUTES_URL)

    def launch_variable_product_edit_page(self, product_order):
        if product_order == 0:
            self.launch_page(TestData.PRODUCT_1_EDIT_URL)
        elif product_order == 1:
            self.launch_page(TestData.PRODUCT_2_EDIT_URL)
        print('Product edit page is launched')

    def launch_variable_product_page(self, product_order):
        if product_order == 0:
            self.launch_page(TestData.PRODUCT_1_URL)
        elif product_order == 1:
            self.launch_page(TestData.PRODUCT_2_URL)
        print('Product page is launched')

    def delete_attributes(self):
        remove_attribute_links = self.get_elements(self.remove_attribute)
        if len(remove_attribute_links) == 0:
            pass
        else:
            for i in range(0, len(remove_attribute_links)):
                i = 0
                self.move_to_element(remove_attribute_links[i])
                remove_attribute_links[i].click()
                self.sleep(3)
                try:
                    self.alert_accept()
                    self.sleep(3)
                except NoAlertPresentException:
                    pass
                if len(remove_attribute_links) == 1:
                    break
                remove_attribute_links = self.get_elements(self.remove_attribute)
            # self.do_click(self.save_attributes_button)
            # self.sleep(15)
            # self.check_product_update_success_message()
            print('\nDeleted attributes if any already selected')

    def view_product_page(self):
        self.scroll_window_to_top()
        self.do_click(self.product_page_link)

    def choose_option_using_swatch_type(self, swatch_type, attribute_name, option_name):
        if swatch_type == 'select':
            self.select_element_from_dropdown_by_visible_text(
                (By.XPATH, "//label[text()='" + attribute_name + "']/parent::th/following-sibling::td//select"),
                option_name)
        elif swatch_type == 'color' or swatch_type == 'label' or swatch_type == 'image':
            swatch_element = (By.XPATH,
                           "//label[text()='" + attribute_name + "']/parent::th/following-sibling::td//li[@title='" + option_name + "']")
            self.scroll_element_into_view(swatch_element)
            self.sleep(2)
            self.do_click(swatch_element)
        elif swatch_type == 'radio':
            swatch_element = (By.XPATH,
                           "//label[text()='" + attribute_name + "']/parent::th/following-sibling::td//span[@class='variation-name' and text()='" + option_name + "']")
            self.scroll_element_into_view(swatch_element)
            self.sleep(2)
            self.do_click(swatch_element)
        self.sleep(2)
        print(attribute_name, 'attribute with option', option_name, 'is selected')

    def click_add_to_cart(self):
        self.sleep(2)
        self.scroll_element_into_view(self.add_to_cart_button)
        self.sleep(2)
        self.do_click(self.add_to_cart_button)
        self.sleep(3)

    def place_order(self):
        self.click_add_to_cart()
        self.sleep(2)
        self.launch_page(TestData.CHECKOUT_URL)
        self.sleep(3)
        self.enter_details()
        self.sleep(5)
        self.scroll_element_into_view(self.place_order_button)
        self.sleep(5)
        self.do_click(self.place_order_button)
        print('Order placed')
        self.check_visibility_of_element(self.order_received_heading)
        self.sleep(5)

    def enter_details(self):
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.text_clear(self.billing_first_name)
        self.text_clear(self.billing_last_name)
        self.text_clear(self.billing_address_1)
        self.text_clear(self.billing_city)
        self.text_clear(self.billing_postcode)
        self.text_clear(self.billing_email)
        self.text_clear(self.billing_phone)

        self.do_sendkeys(self.billing_first_name, TestData.first_name)
        self.do_sendkeys(self.billing_last_name, TestData.last_name)
        self.select_element_from_dropdown_by_value(self.billing_country, TestData.country)
        self.do_sendkeys(self.billing_address_1, TestData.address_1)
        self.do_sendkeys(self.billing_city, TestData.city)
        self.select_element_from_dropdown_by_value(self.billing_state, TestData.state)
        self.do_sendkeys(self.billing_postcode, TestData.postcode)
        self.do_sendkeys(self.billing_phone, TestData.phone)
        self.do_sendkeys(self.billing_email, TestData.email_address)

    def check_swatches_in_order_details_page(self, swatch_type, attribute_name, option_name):
        for i in range(0, len(swatch_type)):
            return self.is_element_displayed((By.XPATH,
                                              "//strong[text()='" + attribute_name + "']/following-sibling::p[text()='" + option_name + "']"))

    def launch_orders_in_my_account_page(self):
        self.launch_page(TestData.MY_ACCOUNT_ORDERS)
        self.sleep(2)
        view_buttons = self.get_elements(self.order_page_view_buttons)
        self.sleep(3)
        self.do_click(view_buttons[0])
        self.sleep(5)

    def remove_all_products_in_cart(self):
        self.launch_page(TestData.CART_URL)
        self.sleep(3)
        global products_in_cart
        products_in_cart_remove_buttons = self.get_elements((By.XPATH, "//td[@class='product-remove']/a"))
        if (len(products_in_cart_remove_buttons)) == 0:
            pass
        else:
            for i in range(0, len(products_in_cart_remove_buttons)):
                i = 0
                self.sleep(2)
                self.driver.execute_script("window.scrollTo(0, 400);")
                self.sleep(2)
                products_in_cart_remove_buttons[i].click()
                self.sleep(12)
                if len(products_in_cart_remove_buttons) == 1:
                    break
                products_in_cart_remove_buttons = self.get_elements((By.XPATH, "//td[@class='product-remove']/a"))
                self.sleep(2)
        print('All products removed from cart')

    def navigate_to_attributes_tab(self):
        # self.launch_page("https://test1.floopbox.com/wp-admin/post.php?post=11959&action=edit")
        self.scroll_element_into_view(self.product_image)
        self.sleep(5)
        self.do_click(self.attributes_tab)
        self.sleep(7)

    def generate_variations(self):
        self.do_click(self.variations_tab)
        self.sleep(8)
        self.check_visibility_of_element(self.variable_product_options)
        if self.check_element_displayed(self.variation_actions):
            self.select_element_from_dropdown_by_value(self.variation_actions, 'delete_all')
            self.sleep(3)
            self.alert_accept()
            self.sleep(2)
            self.alert_accept()
            self.check_visibility_of_element(self.variable_product_options)
            self.sleep(15)
            print('Variations deleted')
        else:
            print('No variations found')
        self.do_click(self.generate_variations_button)
        self.sleep(3)
        self.alert_accept()
        self.check_visibility_of_element(self.variations_table)
        self.sleep(15)
        print('Variations generated successfully')

    def assign_general_regular_price(self, price):
        self.scroll_element_into_view(self.product_data)
        self.select_element_from_dropdown_by_value(self.variation_actions, 'variable_regular_price')
        self.sleep(3)
        self.alert_enter_text(price)
        self.sleep(3)
        print('Common regular price assigned')

    def assign_different_regular_prices(self, price):
        self.sleep(8)
        global variation_boxes
        for i in range(1, 3):
            variation_boxes = self.get_elements(
                (By.XPATH, "//div[contains(@class, 'woocommerce_variation')]/h3/a[text()='Edit']"))
            self.sleep(8)
            # self.move_to_element(variation_boxes[i])
            # self.sleep(5)
            variation_boxes[i].click()
            regular_price_input_boxes = self.get_elements((By.XPATH,
                                                           "//div[contains(@class, 'woocommerce_variable_attributes')]//input[contains(@id,'variable_regular_price')]"))
            regular_price_input_boxes[i].click()
            self.action_clear_text()
            regular_price_input_boxes[i].send_keys(price)
            variation_boxes[i].click()
            self.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView();", variation_boxes[len(variation_boxes) - 4])
        self.do_click(self.save_changes)
        self.sleep(5)
        print('Different regular price assigned')

    def check_product_update_success_message(self):
        self.scroll_window_to_top()
        self.do_click(self.update_button)
        self.sleep(3)
        print('Product updated')
        return self.is_element_displayed(self.success_message)

    def get_test_case_property(self, test_case, property_name):
        return get_id_property(self.test_case_ids[test_case], 'custom_' + property_name).strip()

    def get_attribute_name(self, swatch_type):
        return get_id_property(CaseID.GLOBAL_ATTRIBUTES[swatch_type], 'custom_attribute_name').strip()

    def get_term_name_one(self, swatch_type):
        return self.get_test_case_property(swatch_type, 'term_name_one')

    def get_term_name_two(self, swatch_type):
        return self.get_test_case_property(swatch_type, 'term_name_two')

    def get_term_color_one(self, swatch_type):
        return self.get_test_case_property(swatch_type, 'term_color_one')

    def get_term_color_two(self, swatch_type):
        return self.get_test_case_property(swatch_type, 'term_color_two')

    def get_term_image_one(self, swatch_type):
        return self.get_test_case_property(swatch_type, 'term_image_one')

    def get_term_image_two(self, swatch_type):
        return self.get_test_case_property(swatch_type, 'term_image_two')

    def get_term_label_one(self, swatch_type):
        return self.get_test_case_property(swatch_type, 'term_label_one')

    def get_term_label_two(self, swatch_type):
        return self.get_test_case_property(swatch_type, 'term_label_two')
