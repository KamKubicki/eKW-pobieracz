from pathlib import Path
from typing import Dict, Any
from .settings import read_settings, write_settings

class ConfigManager:
    """Klasa zarządzająca konfiguracją aplikacji"""

    def __init__(self):
        self._config: Dict[str, Any] = {}
        self.load_config()

    def load_config(self):
        """Ładuje konfigurację z pliku"""
        self._config = read_settings()

    def save_config(self):
        """Zapisuje konfigurację do pliku"""
        write_settings(self._config)

    def get(self, key: str, default: Any = None) -> Any:
        """Pobiera wartość z konfiguracji"""
        return self._config.get(key, default)

    def set(self, key: str, value: Any):
        """Ustawia wartość w konfiguracji"""
        self._config[key] = value
        self.save_config()

    @property
    def config(self) -> Dict[str, Any]:
        """Zwraca całą konfigurację"""
        return self._config.copy()
