from typing import Optional
from .webdriver_adapter import WebDriverAdapter, WebDriverOptions
from .selenium_adapter import SeleniumAdapter

class DriverFactory:
    """Fabryka do tworzenia instancji WebDrivera"""

    @staticmethod
    def create_driver(
        browser_type: str = "chrome",
        headless: bool = False,
        proxy: Optional[str] = None,
        load_images: bool = True,
        user_agent: Optional[str] = None
    ) -> WebDriverAdapter:
        """
        Tworzy i konfiguruje instancję WebDrivera

        Args:
            browser_type: Typ przeglądarki ('chrome', 'firefox', 'edge')
            headless: Czy uruchomić w trybie headless
            proxy: Adres proxy (opcjonalnie)
            load_images: Czy ładować obrazy
            user_agent: Własny user agent (opcjonalnie)

        Returns:
            Skonfigurowana instancja WebDriverAdapter
        """
        options = WebDriverOptions(
            headless=headless,
            proxy=proxy,
            load_images=load_images,
            user_agent=user_agent
        )

        driver = SeleniumAdapter(browser_type)
        driver.initialize(options)
        return driver
