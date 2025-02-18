# src/ui/views/components/link_button.py

import flet as ft
import webbrowser

class LinkButton(ft.OutlinedButton):
    """Przycisk z linkiem"""

    def __init__(self, label: str, url: str):
        super().__init__()
        self.text = label
        self.col = {"xs": 12, "sm": 6, "md": 3, "xl": 3}
        self.expand = 1
        self.on_click = lambda _: webbrowser.open_new(url)
