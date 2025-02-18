import json
import csv
import base64
from pathlib import Path
from typing import Dict, List, Optional
import pandas as pd

from .storage_interface import StorageInterface, StorageResult
from src.utils import logger
from src.config.config_manager import ConfigManager

class FileStorage(StorageInterface):
    """Implementacja storage'a zapisującego dane do plików"""

    def __init__(self):
        self.config = ConfigManager()
        self.base_path = Path(self.config.get("save_path"))
        self.base_path.mkdir(parents=True, exist_ok=True)

    def save_pdf(self, data: bytes, filename: str) -> StorageResult:
        """
        Zapisuje dane w formacie PDF

        Args:
            data: Dane PDF w formacie bajtowym
            filename: Nazwa pliku bez rozszerzenia
        """
        try:
            file_path = self.base_path / f"{filename}.pdf"

            # Jeśli plik istnieje i jest włączona opcja pomijania
            if file_path.exists() and self.config.get("already_exist", False):
                return StorageResult(
                    True,
                    "Plik już istnieje, pominięto",
                    file_path
                )

            with open(file_path, "wb") as f:
                f.write(data)

            logger.log_info(f"Zapisano PDF: {file_path}")
            return StorageResult(True, "Zapisano PDF", file_path)

        except Exception as e:
            logger.log_error(f"Błąd podczas zapisu PDF: {e}")
            return StorageResult(False, str(e))

    def save_html(self, content: str, filename: str) -> StorageResult:
        """Zapisuje dane w formacie HTML"""
        try:
            file_path = self.base_path / f"{filename}.html"

            if file_path.exists() and self.config.get("already_exist", False):
                return StorageResult(
                    True,
                    "Plik już istnieje, pominięto",
                    file_path
                )

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            logger.log_info(f"Zapisano HTML: {file_path}")
            return StorageResult(True, "Zapisano HTML", file_path)

        except Exception as e:
            logger.log_error(f"Błąd podczas zapisu HTML: {e}")
            return StorageResult(False, str(e))

    def save_json(self, data: Dict, filename: str) -> StorageResult:
        """Zapisuje dane w formacie JSON"""
        try:
            file_path = self.base_path / f"{filename}.json"

            if file_path.exists() and self.config.get("already_exist", False):
                return StorageResult(
                    True,
                    "Plik już istnieje, pominięto",
                    file_path
                )

            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)

            logger.log_info(f"Zapisano JSON: {file_path}")
            return StorageResult(True, "Zapisano JSON", file_path)

        except Exception as e:
            logger.log_error(f"Błąd podczas zapisu JSON: {e}")
            return StorageResult(False, str(e))

    def save_csv(self, data: List[Dict], filename: str) -> StorageResult:
        """Zapisuje dane w formacie CSV"""
        try:
            file_path = self.base_path / f"{filename}.csv"

            if file_path.exists() and self.config.get("already_exist", False):
                return StorageResult(
                    True,
                    "Plik już istnieje, pominięto",
                    file_path
                )

            df = pd.DataFrame(data)
            df.to_csv(
                file_path,
                index=False,
                encoding="utf-8-sig",
                sep=";",
                quoting=csv.QUOTE_ALL
            )

            logger.log_info(f"Zapisano CSV: {file_path}")
            return StorageResult(True, "Zapisano CSV", file_path)

        except Exception as e:
            logger.log_error(f"Błąd podczas zapisu CSV: {e}")
            return StorageResult(False, str(e))

    def file_exists(self, filename: str) -> bool:
        """Sprawdza czy plik istnieje"""
        # Sprawdza wszystkie możliwe rozszerzenia
        extensions = [".pdf", ".html", ".json", ".csv"]
        return any((self.base_path / f"{filename}{ext}").exists() for ext in extensions)

    def get_file_path(self, filename: str) -> Path:
        """Zwraca pełną ścieżkę do pliku"""
        return self.base_path / filename
