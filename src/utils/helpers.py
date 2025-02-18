from random import randint
from typing import Dict, List
from pathlib import Path

class KWNumberHelper:
    """Klasa pomocnicza do operacji na numerach ksiąg wieczystych"""

    REP_DICT: Dict[str, str] = {
        "X": "10", "A": "11", "B": "12", "C": "13", "D": "14",
        "E": "15", "F": "16", "G": "17", "H": "18", "I": "19",
        "J": "20", "K": "21", "L": "22", "M": "23", "N": "24",
        "O": "25", "P": "26", "R": "27", "S": "28", "T": "29",
        "U": "30", "W": "31", "Y": "32", "Z": "33",
        **{str(i): str(i) for i in range(10)}  # cyfry 0-9
    }

    @classmethod
    def correct_kw_number(cls, sad: str, number: str) -> str:
        """Koryguje i weryfikuje numer księgi wieczystej"""
        try:
            sad_value = [cls.REP_DICT[s] for s in sad.upper()]
            wei = [1, 3, 7] * 4

            # Uzupełnienie numeru zerami z przodu
            number = number.zfill(8)

            temp_kw = sad_value + [x for x in number]
            ctrl_dig = sum(wei[k] * int(temp_kw[k]) for k in range(len(wei))) % 10

            return f"{sad}/{number}/{ctrl_dig}"
        except KeyError as e:
            raise ValueError(f"Nieprawidłowy znak w numerze KW: {e}")
        except Exception as e:
            raise ValueError(f"Błąd podczas przetwarzania numeru KW: {e}")

class ProxyHelper:
    """Klasa pomocnicza do operacji na proxy"""

    @staticmethod
    def get_proxy(proxy_file_path: str) -> str:
        """Pobiera losowe proxy z pliku"""
        try:
            with open(proxy_file_path, "r", encoding="utf-8") as file:
                proxies = [line.strip() for line in file if line.strip()]
                if not proxies:
                    raise ValueError("Lista proxy jest pusta")
                return proxies[randint(0, len(proxies) - 1)]
        except FileNotFoundError:
            raise FileNotFoundError(f"Nie znaleziono pliku proxy: {proxy_file_path}")
        except Exception as e:
            raise Exception(f"Błąd podczas pobierania proxy: {e}")

# Dodajmy też Constants do przechowywania stałych
class Constants:
    """Stałe używane w aplikacji"""

    ERROR_FILE_NOT_SELECTED = "File not selected"
    ERROR_INVALID_DATA = "Invalid data format"

    # Możemy dodać więcej stałych w miarę potrzeb
