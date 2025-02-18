from typing import List, Dict
import re

class DataValidator:
    """Klasa do walidacji danych z księgi wieczystej"""

    @staticmethod
    def validate_kw_number(number: str) -> bool:
        """Sprawdza poprawność numeru KW"""
        pattern = r'^[A-Z0-9]{4}/\d{8}/\d{1}$'
        return bool(re.match(pattern, number))

    @staticmethod
    def validate_section_data(data: Dict, required_fields: List[str]) -> bool:
        """Sprawdza czy wszystkie wymagane pola są obecne"""
        return all(field in data for field in required_fields)

    @staticmethod
    def validate_plot_number(plot: str) -> bool:
        """Sprawdza poprawność numeru działki"""
        # Implementacja walidacji numeru działki
        return True
