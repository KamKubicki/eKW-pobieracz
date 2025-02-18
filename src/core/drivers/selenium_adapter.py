from typing import Any

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

from .webdriver_adapter import WebDriverAdapter, WebDriverOptions
from src.utils import logger

class SeleniumAdapter(WebDriverAdapter):
    """Implementacja WebDriverAdapter dla Selenium"""

    def __init__(self, browser_type: str = "chrome"):
        self.browser_type = browser_type
        self.driver = None

    def initialize(self, options: WebDriverOptions) -> None:
        try:
            if self.browser_type == "chrome":
                chrome_options = webdriver.ChromeOptions()
                self._configure_chrome_options(chrome_options, options)
                self.driver = webdriver.Chrome(options=chrome_options)
            elif self.browser_type == "firefox":
                firefox_options = webdriver.FirefoxOptions()
                self._configure_firefox_options(firefox_options, options)
                self.driver = webdriver.Firefox(options=firefox_options)
            elif self.browser_type == "edge":
                edge_options = webdriver.EdgeOptions()
                self._configure_edge_options(edge_options, options)
                self.driver = webdriver.Edge(options=edge_options)
            else:
                raise ValueError(f"Nieobsługiwany typ przeglądarki: {self.browser_type}")

            self.driver.implicitly_wait(options.implicit_wait)
            self.driver.set_page_load_timeout(options.page_load_timeout)

        except Exception as e:
            logger.log_error(f"Błąd podczas inicjalizacji drivera: {e}")
            raise

    def _configure_chrome_options(self, chrome_options, options: WebDriverOptions):
        """Konfiguracja opcji dla Chrome"""
        if options.headless:
            chrome_options.add_argument("--headless=new")
        if options.proxy:
            chrome_options.add_argument(f'--proxy-server={options.proxy}')
        if not options.load_images:
            chrome_options.add_argument('--blink-settings=imagesEnabled=false')
        if options.user_agent:
            chrome_options.add_argument(f'user-agent={options.user_agent}')

        # Dodatkowe optymalizacje
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Ustawienia eksperymentalne
        prefs = {
            "profile.managed_default_content_settings.images": 2 if not options.load_images else 1,
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False
        }
        chrome_options.add_experimental_option("prefs", prefs)

    def _configure_firefox_options(self, firefox_options, options: WebDriverOptions):
        """Konfiguracja opcji dla Firefox"""
        if options.headless:
            firefox_options.add_argument("--headless")
        if options.proxy:
            firefox_options.set_preference("network.proxy.type", 1)
            proxy_parts = options.proxy.split(":")
            firefox_options.set_preference("network.proxy.http", proxy_parts[0])
            if len(proxy_parts) > 1:
                firefox_options.set_preference("network.proxy.http_port", int(proxy_parts[1]))

    def _configure_edge_options(self, edge_options, options: WebDriverOptions):
        """Konfiguracja opcji dla Edge"""
        # Podobne do Chrome, bo Edge jest oparty na Chromium
        self._configure_chrome_options(edge_options, options)

    def quit(self) -> None:
        try:
            if self.driver:
                self.driver.quit()
        except Exception as e:
            logger.log_error(f"Błąd podczas zamykania drivera: {e}")

    def get(self, url: str) -> None:
        try:
            self.driver.get(url)
        except Exception as e:
            logger.log_error(f"Błąd podczas ładowania strony {url}: {e}")
            raise

    def find_element(self, by: str, value: str, timeout: int = 10) -> Any:
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((getattr(By, by), value))
            )
            return element
        except TimeoutException:
            logger.log_error(f"Timeout podczas szukania elementu {by}={value}")
            raise
        except Exception as e:
            logger.log_error(f"Błąd podczas szukania elementu {by}={value}: {e}")
            raise

    def find_elements(self, by: str, value: str) -> list:
        return self.driver.find_elements(getattr(By, by), value)

    def get_page_source(self) -> str:
        return self.driver.page_source

    def save_screenshot(self, filename: str) -> None:
        try:
            self.driver.save_screenshot(filename)
        except Exception as e:
            logger.log_error(f"Błąd podczas zapisywania zrzutu ekranu: {e}")
            raise
