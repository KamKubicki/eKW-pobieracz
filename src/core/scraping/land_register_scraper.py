from typing import Optional, Dict, List
from dataclasses import dataclass
from pathlib import Path
import time

from src.core.drivers import DriverFactory, WebDriverAdapter
from src.utils import logger, KWNumberHelper
from src.config.config_manager import ConfigManager

@dataclass
class ScrapingResult:
    """Klasa przechowująca wyniki scrapingu"""
    success: bool
    message: str
    data: Optional[Dict] = None
    files: List[Path] = None

class LandRegisterScraper:
    """Główna klasa odpowiedzialna za scraping ksiąg wieczystych"""

    BASE_URL = "https://przegladarka-ekw.ms.gov.pl/eukw_prz/KsiegiWieczyste/wyszukiwanieKW"

    def __init__(self):
        self.config = ConfigManager()
        self.driver: Optional[WebDriverAdapter] = None

    def initialize(self):
        """Inicjalizacja scrapera"""
        try:
            self.driver = DriverFactory.create_driver(
                browser_type=self.config.get("browser", "chrome"),
                headless=True,
                proxy=self.config.get("proxy_value") if self.config.get("use_proxy") else None,
                load_images=self.config.get("page_image", True)
            )
            logger.log_info("Zainicjalizowano scraper")
        except Exception as e:
            logger.log_error(f"Błąd podczas inicjalizacji scrapera: {e}")
            raise

    def scrape_register(self, kw_number: str) -> ScrapingResult:
        """
        Pobiera dane dla pojedynczej księgi wieczystej

        Args:
            kw_number: Numer księgi wieczystej

        Returns:
            ScrapingResult z wynikami scrapingu
        """
        try:
            if not self.driver:
                self.initialize()

            # Walidacja numeru KW
            try:
                court, number, control = kw_number.split('/')
                validated_number = KWNumberHelper.correct_kw_number(court, number)
                if validated_number != kw_number:
                    logger.log_info(f"Skorygowano numer KW z {kw_number} na {validated_number}")
                    kw_number = validated_number
            except ValueError as e:
                return ScrapingResult(False, f"Nieprawidłowy format numeru KW: {e}", None)

            # Ładowanie strony
            self.driver.get(self.BASE_URL)
            time.sleep(1)  # Krótkie opóźnienie

            # Wypełnienie formularza
            self._fill_search_form(kw_number)

            # Sprawdzenie dostępności treści
            if not self._check_content_availability():
                return ScrapingResult(False, "Treść niedostępna", None)

            # Pobranie danych
            data = self._extract_data()

            # Zapis plików
            saved_files = self._save_files(kw_number, data)

            return ScrapingResult(True, "Sukces", data, saved_files)

        except Exception as e:
            logger.log_error(f"Błąd podczas scrapowania KW {kw_number}: {e}")
            return ScrapingResult(False, str(e), None)

    def _fill_search_form(self, kw_number: str):
        """Wypełnia formularz wyszukiwania"""
        try:
            court, number, control = kw_number.split('/')

            # Wypełnienie pól
            court_input = self.driver.find_element("ID", "kodWydzialuInput")
            number_input = self.driver.find_element("ID", "numerKsiegiWieczystej")
            control_input = self.driver.find_element("ID", "cyfraKontrolna")

            court_input.send_keys(court)
            number_input.send_keys(number)
            control_input.send_keys(control)

            # Kliknięcie przycisku wyszukiwania
            search_button = self.driver.find_element("ID", "wyszukaj")
            search_button.click()

        except Exception as e:
            raise Exception(f"Błąd podczas wypełniania formularza: {e}")

    def _check_content_availability(self) -> bool:
        """Sprawdza dostępność treści księgi"""
        try:
            # Sprawdzenie czy jest dostępna treść zwykła
            normal_content = self.driver.find_element("NAME", "przyciskWydrukZwykly")
            if normal_content:
                return True

            # Jeśli nie ma treści zwykłej, sprawdź czy można pobrać treść zupełną
            if self.config.get("try_zupelna", False):
                full_content = self.driver.find_element("NAME", "przyciskWydrukZupelny")
                return bool(full_content)

            return False

        except Exception:
            return False

    def _extract_data(self) -> Dict:
        """Ekstrahuje dane z księgi"""
        data = {}
        try:
            # Pobieranie podstawowych informacji
            data["basic_info"] = self._get_basic_info()

            # Pobieranie poszczególnych działów jeśli są włączone
            if self.config.get("dzial_1o"):
                data["dzial_1o"] = self._get_section_data("Dział I-O")
            if self.config.get("dzial_1s"):
                data["dzial_1s"] = self._get_section_data("Dział I-Sp")
            if self.config.get("dzial_2"):
                data["dzial_2"] = self._get_section_data("Dział II")
            if self.config.get("dzial_3"):
                data["dzial_3"] = self._get_section_data("Dział III")
            if self.config.get("dzial_4"):
                data["dzial_4"] = self._get_section_data("Dział IV")

            return data

        except Exception as e:
            raise Exception(f"Błąd podczas ekstrakcji danych: {e}")

    def _get_basic_info(self) -> Dict:
        """Pobiera podstawowe informacje o księdze"""
        try:
            info = {}
            elements = self.driver.find_elements("XPATH", "//div[@class='left']")
            keys = ["Numer", "Typ", "Oznaczenie", "Zapis", "Zamknięcie", "Położenie", "Właściciel"]

            for i, element in enumerate(elements):
                if i < len(keys):
                    info[keys[i]] = element.text.strip()
                else:
                    if "Właściciel" not in info:
                        info["Właściciel"] = []
                    info["Właściciel"].append(element.text.strip())

            return info

        except Exception as e:
            raise Exception(f"Błąd podczas pobierania podstawowych informacji: {e}")

    def _get_section_data(self, section: str) -> Dict:
        """Pobiera dane z konkretnego działu"""
        try:
            # Kliknięcie w odpowiedni dział
            section_button = self.driver.find_element("XPATH", f"//input[@value='{section}']")
            section_button.click()
            time.sleep(1)

            # Pobranie danych z działu
            data = {}
            elements = self.driver.find_elements("XPATH", "//td")

            # Tutaj dokładna logika parsowania zależna od działu
            # ...

            return data

        except Exception as e:
            raise Exception(f"Błąd podczas pobierania danych z działu {section}: {e}")

    def _save_files(self, kw_number: str, data: Dict) -> List[Path]:
        """Zapisuje pliki w wybranych formatach"""
        saved_files = []
        save_path = Path(self.config.get("save_path"))
        base_filename = save_path / kw_number.replace("/", ".")

        try:
            # Zapis PDF
            if self.config.get("save_pdf"):
                pdf_path = base_filename.with_suffix(".pdf")
                # logika zapisu PDF
                saved_files.append(pdf_path)

            # Zapis HTML
            if self.config.get("save_html"):
                html_path = base_filename.with_suffix(".html")
                with open(html_path, "w", encoding="utf-8") as f:
                    f.write(self.driver.get_page_source())
                saved_files.append(html_path)

            # Zapis JSON
            if self.config.get("save_json"):
                json_path = base_filename.with_suffix(".json")
                # logika zapisu JSON
                saved_files.append(json_path)

            return saved_files

        except Exception as e:
            raise Exception(f"Błąd podczas zapisywania plików: {e}")

    def close(self):
        """Zamyka scraper i zwalnia zasoby"""
        if self.driver:
            self.driver.quit()
            self.driver = None
