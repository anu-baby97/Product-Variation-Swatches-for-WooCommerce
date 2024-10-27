import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chrome_Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.firefox.service import Service as Firefox_Service



def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default='chrome'
        # to choose browser at run time
    )


@pytest.fixture(scope="session")
def setUp(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        try:
            chrome_options = Chrome_Options()
            chrome_options.add_argument("--start-maximized")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--incognito")
            chrome_options.add_argument('--headless')
            chrome_options.add_argument("enable-automation")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--dns-prefetch-disable")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-browser-side-navigation")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--profile-directory=Default")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("enable-features=NetworkServiceInProcess")
            chrome_options.add_argument("--disable-accelerated-2d-canvas")
            chrome_options.add_argument("--disable-accelerated-jpeg-decoding")
            chrome_options.add_argument("--disable-accelerated-video-decode")
            chrome_options.add_argument("--disable-accelerated-video-encode")
            chrome_options.add_argument("--disable-accelerated-plugins")
            chrome_options.add_argument("--disable-accelerated-plugins-for-whitelist")
            desiredCapabilities = DesiredCapabilities().CHROME
            desiredCapabilities["pageLoadStrategy"] = "normal"
            prefs = {"credentials_enable_service": False,
                     "profile.password_manager_enabled": False}
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--log-level=3")
            driver = webdriver.Chrome(service=Chrome_Service(ChromeDriverManager().install()), options=chrome_options)
            driver.set_window_size(1920, 1080)
        except WebDriverException:
            setUp(request)

    elif browser_name == "firefox":
        try:
            options = Firefox_Options()
            # script_dir = os.path.dirname(os.path.abspath(__file__))
            # geckodriver_path = os.path.join(script_dir, 'geckodriver')
            # log_path = os.path.join(script_dir, 'geckodriver.log')
            options.add_argument("--start-maximized")
            options.add_argument("--disable-gpu")
            options.add_argument("--incognito")
            options.add_argument('--headless')
            # options.add_argument("--window-size=1920,1080")
            options.add_argument("enable-automation")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-extensions")
            options.add_argument("--dns-prefetch-disable")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-browser-side-navigation")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--profile-directory=Default")
            options.add_argument("--ignore-certificate-errors")
            options.add_argument("--disable-plugins-discovery")
            options.add_argument("enable-features=NetworkServiceInProcess")
            options.add_argument("--disable-accelerated-2d-canvas")
            options.add_argument("--disable-accelerated-jpeg-decoding")
            options.add_argument("--disable-accelerated-video-decode")
            options.add_argument("--disable-accelerated-video-encode")
            options.add_argument("--disable-accelerated-plugins")
            options.add_argument("--disable-accelerated-plugins-for-whitelist")
            desiredCapabilities = DesiredCapabilities().FIREFOX
            desiredCapabilities["pageLoadStrategy"] = "normal"
            options.add_argument("--log-level=3")
            # firefox_service = Firefox_Service(executable_path=geckodriver_path)
            driver = webdriver.Firefox(options=options)
            driver.maximize_window()
            # driver.set_window_size(1920, 1080)
        except WebDriverException:
            setUp(request)

    elif browser_name == "edge":
        try:
            edge_options = webdriver.EdgeOptions()
            edge_options.add_argument("--start-maximized")
            edge_options.add_argument("--disable-gpu")
            edge_options.add_argument("--incognito")
            edge_options.add_argument('--headless')
            edge_options.add_argument("--window-size=1920,1080")
            edge_options.add_argument("enable-automation")
            edge_options.add_argument("--no-sandbox")
            edge_options.add_argument("--disable-extensions")
            edge_options.add_argument("--dns-prefetch-disable")
            edge_options.add_argument("--disable-dev-shm-usage")
            edge_options.add_argument("--disable-browser-side-navigation")
            edge_options.add_argument("--disable-popup-blocking")
            edge_options.add_argument("--profile-directory=Default")
            edge_options.add_argument("--ignore-certificate-errors")
            edge_options.add_argument("--disable-plugins-discovery")
            edge_options.add_argument("enable-features=NetworkServiceInProcess")
            edge_options.add_argument("--disable-accelerated-2d-canvas")
            edge_options.add_argument("--disable-accelerated-jpeg-decoding")
            edge_options.add_argument("--disable-accelerated-video-decode")
            edge_options.add_argument("--disable-accelerated-video-encode")
            edge_options.add_argument("--disable-accelerated-plugins")
            edge_options.add_argument("--disable-accelerated-plugins-for-whitelist")
            desiredCapabilities = DesiredCapabilities().EDGE
            desiredCapabilities["pageLoadStrategy"] = "normal"
            prefs = {"credentials_enable_service": False,
                     "profile.password_manager_enabled": False}
            edge_options.add_experimental_option("prefs", prefs)
            edge_options.add_argument("--log-level=3")
            driver = webdriver.Edge(options=edge_options)
            driver.set_window_size(1920, 1080)

        except WebDriverException:
            setUp(request)

    elif browser_name == "safari":
        try:
            driver = webdriver.Safari()
            driver.set_window_size(1920, 1280)
            # driver.maximize_window()
        except WebDriverException:
            setUp(request)

    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)

    yield
    driver.close()
