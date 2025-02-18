# src/ui/controllers/app_controller.py

import flet as ft
from typing import Dict

from .base_controller import BaseController
from .download_controller import DownloadController
from .settings_controller import SettingsController
from .about_controller import AboutController
from src.utils import logger

class AppController:
    """Główny kontroler aplikacji"""

    def __init__(self, page: ft.Page):
        self.page = page
        self.controllers: Dict[str, BaseController] = {
            "download": DownloadController(page),
            "settings": SettingsController(page),
            "about": AboutController(page)
        }
        self._setup_page()

    def _setup_page(self):
        """Konfiguruje główne okno aplikacji"""
        self.page.title = "eKW - Pobieraczek 2.0"

        # Ustawienia okna
        self.page.window.width = 450
        self.page.window.height = 700
        self.page.window.min_width = 450
        self.page.window.min_height = 700
        self.page.window.resizable = True

        # Konfiguracja strony
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.adaptive = True

        # Dodanie widoków
        for controller in self.controllers.values():
            self.page.add(controller.view)
            controller.view.visible = False

        # Domyślnie pokazujemy zakładkę pobierania
        self.controllers["download"].view.visible = True

        # Dodanie paska nawigacji
        self._setup_navigation()

    def _setup_navigation(self):
        """Konfiguruje pasek nawigacji"""
        self.page.navigation_bar = ft.NavigationBar(
            selected_index=0,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.icons.DOWNLOAD_OUTLINED,
                    selected_icon=ft.icons.DOWNLOAD,
                    label="Pobieranie"
                ),
                ft.NavigationBarDestination(
                    icon=ft.icons.SETTINGS_OUTLINED,
                    selected_icon=ft.icons.SETTINGS,
                    label="Ustawienia"
                ),
                ft.NavigationBarDestination(
                    icon=ft.icons.HELP_OUTLINE,
                    selected_icon=ft.icons.HELP,
                    label="O programie"
                ),
            ],
            on_change=self._handle_navigation
        )

    def _handle_navigation(self, e):
        """Obsługuje zmianę zakładki"""
        tabs = ["download", "settings", "about"]
        for i, tab in enumerate(tabs):
            self.controllers[tab].view.visible = (i == e.control.selected_index)
        self.page.update()

    def run(self):
        """Uruchamia aplikację"""
        try:
            self.page.update()
        except Exception as e:
            logger.log_error(f"Błąd podczas uruchamiania aplikacji: {e}")
