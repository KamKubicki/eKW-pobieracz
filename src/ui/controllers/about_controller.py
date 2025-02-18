# src/ui/controllers/about_controller.py
import os
from pathlib import Path

import flet as ft
import webbrowser
from .base_controller import BaseController
from ...utils import logger


class AboutController(BaseController):
    """Kontroler obsługujący zakładkę 'O programie'"""

    def __init__(self, page: ft.Page):
        super().__init__(page)

    def open_link(self, url: str):
        """Otwiera link w przeglądarce"""
        webbrowser.open_new(url)

    def open_documentation(self):
        """Otwiera dokumentację"""
        try:
            path = Path("docs/manual.pdf")
            if path.exists():
                os.startfile(path)
            else:
                logger.log_error("Nie znaleziono dokumentacji")
        except Exception as e:
            logger.log_error(f"Błąd podczas otwierania dokumentacji: {e}")

    def _create_view(self) -> ft.Control:
        from src.ui.views.about_view import AboutView
        return AboutView(self)
