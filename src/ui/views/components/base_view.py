# src/ui/views/components/base_view.py

import flet as ft
from typing import Optional

class BaseView(ft.Container):
    """Bazowa klasa dla wszystkich widoków"""

    def __init__(self):
        super().__init__()
        self.bgcolor = ft.colors.WHITE12
        self.border_radius = ft.border_radius.all(5)
        self.padding = 5
        self.expand = 1
        self.page = None  # Dodajemy atrybut page

    # @property
    # def page(self):
    #     return self.content.page if self.content else None
