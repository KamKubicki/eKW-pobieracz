from typing import Dict, List
from bs4 import BeautifulSoup
import re

class LandRegisterParser:
    """Klasa odpowiedzialna za parsowanie danych z księgi wieczystej"""

    @staticmethod
    def parse_basic_info(html: str) -> Dict:
        """Parsuje podstawowe informacje o księdze"""
        soup = BeautifulSoup(html, 'html.parser')
        info = {}

        elements = soup.find_all("div", class_="left")
        keys = ["Numer", "Typ", "Oznaczenie", "Zapis", "Zamknięcie", "Położenie", "Właściciel"]

        for i, element in enumerate(elements):
            text = element.get_text(strip=True)
            if i < len(keys):
                info[keys[i]] = text
            else:
                if "Właściciel" not in info:
                    info["Właściciel"] = []
                info["Właściciel"].append(text)

        return info

    @staticmethod
    def parse_section_1o(html: str) -> Dict:
        """Parsuje dane z działu I-O"""
        soup = BeautifulSoup(html, 'html.parser')
        data = {"działki": []}

        # Logika parsowania działu I-O
        # ...

        return data

    @staticmethod
    def parse_section_1s(html: str) -> Dict:
        """Parsuje dane z działu I-Sp"""
        soup = BeautifulSoup(html, 'html.parser')
        data = {"spis_praw": []}

        # Logika parsowania działu I-Sp
        # ...

        return data

    @staticmethod
    def clean_text(text: str) -> str:
        """Czyści tekst ze zbędnych białych znaków"""
        return re.sub(r'\s+', ' ', text).strip()
