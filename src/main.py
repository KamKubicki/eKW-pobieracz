import flet as ft
from pathlib import Path
import sys
from typing import Any, Optional, Dict, List  # Dodajemy import typing

# Dodajemy katalog src do PYTHONPATH
sys.path.append(str(Path(__file__).parent.parent))

from src.ui.controllers.app_controller import AppController
from src.utils import logger
from src.config.config_manager import ConfigManager


def main(page: ft.Page):
    """
    Główna funkcja aplikacji

    Args:
        page: Obiekt strony Flet
    """
    try:
        # Inicjalizacja kontrolera aplikacji
        app = AppController(page)

        # Obsługa zamykania aplikacji
        def on_window_event(e):
            if e.data == "close":
                logger.log_info("Zamykanie aplikacji...")

                # Zapisanie konfiguracji
                config = ConfigManager()
                config.save_config()

                # Zatrzymanie wszystkich zadań
                download_controller = app.controllers["download"]
                download_controller.stop_processing()

                # Zamknięcie okna
                page.window.destroy()

        # Konfiguracja okna
        page.window.on_event = on_window_event
        page.window.prevent_close = True

        # Uruchomienie aplikacji
        app.run()

    except Exception as e:
        logger.log_error(f"Błąd podczas uruchamiania aplikacji: {e}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        # Konfiguracja logowania
        logger.log_info("Uruchamianie aplikacji eKW - Pobieraczek 2.0")

        # Uruchomienie aplikacji Flet
        ft.app(target=main)

    except Exception as e:
        logger.log_error(f"Krytyczny błąd aplikacji: {e}")
        sys.exit(1)