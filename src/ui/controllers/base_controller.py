# src/ui/controllers/base_controller.py

from typing import Optional, Any
import flet as ft


class BaseController:
    """Bazowa klasa dla kontrolerów"""

    def __init__(self, page: ft.Page):
        self.page = page
        self._view: Optional[ft.Control] = None

    @property
    def view(self) -> ft.Control:
        """Zwraca widok kontrolera"""
        if not self._view:
            self._view = self._create_view()
        return self._view

    def _create_view(self) -> ft.Control:
        """
        Tworzy widok - metoda do nadpisania w klasach pochodnych.
        Domyślnie zwraca pusty kontener.
        """
        return ft.Container()  # Domyślny pusty widok zamiast rzucania wyjątku

    def update(self):
        """Aktualizuje widok"""
        if self._view:
            self._view.update()