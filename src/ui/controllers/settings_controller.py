# src/ui/controllers/settings_controller.py

import flet as ft
from typing import Callable

from src.config.config_manager import ConfigManager
from .base_controller import BaseController
from .dialog_controller import DialogController

class SettingsController(BaseController):
    """Kontroler obsługujący ustawienia aplikacji"""

    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.config = ConfigManager()

    def change_theme(self, theme: str):
        """Zmienia motyw aplikacji"""
        self.config.set("theme", theme)
        self.page.theme = ft.Theme(color_scheme_seed=theme.lower())
        self.page.update()

    def change_theme_mode(self, mode: str):
        """Zmienia tryb motywu (jasny/ciemny)"""
        self.config.set("theme_mode", mode)
        if mode == "Jasny":
            self.page.theme_mode = ft.ThemeMode.LIGHT
        elif mode == "System":
            self.page.theme_mode = ft.ThemeMode.SYSTEM
        else:
            self.page.theme_mode = ft.ThemeMode.DARK
        self.page.update()

    def change_save_path(self):
        """Zmienia ścieżkę zapisu"""
        path = DialogController.select_directory()
        if path:
            self.config.set("save_path", str(path))
            self.update()

    def change_threads(self, value: int):
        """Zmienia liczbę wątków"""
        self.config.set("threads", value)
        self.update()

    def toggle_setting(self, key: str, value: bool):
        """Przełącza ustawienie typu bool"""
        self.config.set(key, value)
        self.update()

    def _create_view(self) -> ft.Control:
        from src.ui.views.settings_view import SettingsView
        return SettingsView(self)
