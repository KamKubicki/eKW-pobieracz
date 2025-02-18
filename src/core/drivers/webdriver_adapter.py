from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from dataclasses import dataclass

@dataclass
class WebDriverOptions:
    """Konfiguracja dla WebDrivera"""
    headless: bool = False
    proxy: Optional[str] = None
    load_images: bool = True
    user_agent: Optional[str] = None
    page_load_timeout: int = 30
    implicit_wait: int = 10

class WebDriverAdapter(ABC):
    """Abstrakcyjny interfejs dla różnych implementacji WebDrivera"""

    @abstractmethod
    def initialize(self, options: WebDriverOptions) -> None:
        """Inicjalizacja drivera"""
        pass

    @abstractmethod
    def quit(self) -> None:
        """Zamknięcie drivera"""
        pass

    @abstractmethod
    def get(self, url: str) -> None:
        """Załadowanie strony"""
        pass

    @abstractmethod
    def find_element(self, by: str, value: str) -> Any:
        """Znalezienie elementu na stronie"""
        pass

    @abstractmethod
    def find_elements(self, by: str, value: str) -> list:
        """Znalezienie elementów na stronie"""
        pass

    @abstractmethod
    def get_page_source(self) -> str:
        """Pobranie źródła strony"""
        pass

    @abstractmethod
    def save_screenshot(self, filename: str) -> None:
        """Zapisanie zrzutu ekranu"""
        pass
