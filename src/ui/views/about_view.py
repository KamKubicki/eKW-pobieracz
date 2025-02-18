# src/ui/views/about_view.py

import flet as ft
from .components.base_view import BaseView
from .components.link_button import LinkButton

class AboutView(BaseView):
    """Widok informacji o programie"""

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Tytuł
        self.title = ft.Text(
            "eKW - Pobieraczek 2.0",
            size=24,
            weight=ft.FontWeight.BOLD
        )

        # Linki
        self.links = [
            LinkButton("GitHub", "https://github.com/user/ekw-pobieracz"),
            LinkButton("Wykop", "https://wykop.pl/tag/ekwpobieraczek"),
            LinkButton("Dokumentacja", "https://ekw-pobieracz.readthedocs.io"),
            LinkButton("Zgłoś błąd", "https://github.com/user/ekw-pobieracz/issues"),
        ]

        # Dokumentacja
        self.doc_button = ft.ElevatedButton(
            text="Otwórz dokumentację PDF",
            icon=ft.icons.DESCRIPTION,
            on_click=lambda _: self.controller.open_documentation()
        )

        # Informacje
        self.info = ft.Column(
            controls=[
                ft.Text("Autor: Imię Nazwisko"),
                ft.Text("Wersja: 2.0.0"),
                ft.Text("Licencja: MIT"),
            ],
            spacing=5
        )

        self.content = ft.Column(
            controls=[
                self.title,
                ft.Container(height=20),  # Odstęp
                self.info,
                ft.Container(height=20),  # Odstęp
                ft.Text("Przydatne linki:", size=16),
                ft.ResponsiveRow(controls=self.links),
                ft.Container(height=20),  # Odstęp
                self.doc_button
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
