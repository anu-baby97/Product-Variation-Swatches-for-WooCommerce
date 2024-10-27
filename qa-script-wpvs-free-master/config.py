import os
from dotenv import load_dotenv

load_dotenv()


class TestData:
    BASE_URL = os.getenv('WEBSITE_BASE_URL')
    PLUGIN_URL = BASE_URL + "/wp-admin/edit.php?post_type=product&page=thwepof_extra_product_options&tab=general_settings"
    EDIT_PRODUCT_ATTRIBUTES_URL = BASE_URL + "/wp-admin/edit.php?post_type=product&page=product_attributes"
    GLOBAL_ATTRIBUTES_URL = BASE_URL + "/wp-admin/edit.php?post_type=product&page=th_product_variation_swatches_for_woocommerce&tab=global_product_attributes"
    SWATCHES_DESIGN_URL = BASE_URL + "/wp-admin/edit.php?post_type=product&page=th_product_variation_swatches_for_woocommerce&tab=swatches_design_settings"
    GLOBAL_SETTINGS_URL = BASE_URL + "/wp-admin/edit.php?post_type=product&page=th_product_variation_swatches_for_woocommerce&tab=general_settings"
    USER_NAME = os.getenv('WEBSITE_USER_NAME')
    PASSWORD = os.getenv('WEBSITE_PASSWORD')
    CHECKOUT_URL = BASE_URL + "/checkout/"
    SHOP_URL = BASE_URL + "/shop/"
    CART_URL = BASE_URL + "/cart/"
    VARIABLE_PRODUCT_1 = os.getenv('VARIABLE_PRODUCT_1')
    VARIABLE_PRODUCT_1_ID = os.getenv('VARIABLE_PRODUCT_1_ID')
    VARIABLE_PRODUCT_2 = os.getenv('VARIABLE_PRODUCT_2')
    VARIABLE_PRODUCT_2_ID = os.getenv('VARIABLE_PRODUCT_2_ID')

    PRODUCT_1_URL = BASE_URL + "/product/" + VARIABLE_PRODUCT_1
    PRODUCT_1_EDIT_URL = BASE_URL + "/wp-admin/post.php?post=" + VARIABLE_PRODUCT_1_ID + "&action=edit"
    PRODUCT_2_URL = BASE_URL + "/product/" + VARIABLE_PRODUCT_2
    PRODUCT_2_EDIT_URL = BASE_URL + "/wp-admin/post.php?post=" + VARIABLE_PRODUCT_2_ID + "&action=edit"

    USER_PROFILE_URL = BASE_URL + "/wp-admin/profile.php?wp_http_referer=%2Fwp-admin%2Fusers.php"
    ORDERS_PAGE = BASE_URL + "/wp-admin/admin.php?page=wc-orders"
    ALL_PRODUCTS_TAB = BASE_URL + "/wp-admin/edit.php?post_type=product"
    password = 'pwd123'
    MY_ACCOUNT_ORDERS = BASE_URL + "/my-account/orders/"
    first_name = "John"
    last_name = "Doe"
    email_address = "johndoe123@gmail.com"
    country = "IN"
    state = "KL"
    state_full_form = 'Kerala'
    address_1 = "ABC House"
    city = "Kozhikode"
    phone = '9876543210'
    postcode = "673012"
# anu@zennode.com
# znode123
