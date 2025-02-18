from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from pathlib import Path
from dataclasses import dataclass

@dataclass
class StorageResult:
    """Rezultat operacji storage'a"""
    success: bool
    message: str
    file_path: Optional[Path] = None
    data: Optional[Dict] = None

class StorageInterface(ABC):
    """Interfejs dla różnych implementacji storage'a"""

    @abstractmethod
    def save_pdf(self, data: bytes, filename: str) -> StorageResult:
        """Zapisuje dane w formacie PDF"""
        pass

    @abstractmethod
    def save_html(self, content: str, filename: str) -> StorageResult:
        """Zapisuje dane w formacie HTML"""
        pass

    @abstractmethod
    def save_json(self, data: Dict, filename: str) -> StorageResult:
        """Zapisuje dane w formacie JSON"""
        pass

    @abstractmethod
    def save_csv(self, data: List[Dict], filename: str) -> StorageResult:
        """Zapisuje dane w formacie CSV"""
        pass

    @abstractmethod
    def file_exists(self, filename: str) -> bool:
        """Sprawdza czy plik istnieje"""
        pass

    @abstractmethod
    def get_file_path(self, filename: str) -> Path:
        """Zwraca pełną ścieżkę do pliku"""
        pass
