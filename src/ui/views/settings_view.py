import flet as ft
from .components.base_view import BaseView

class SettingsView(BaseView):
    """Widok ustawień aplikacji"""

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # Motywy
        self.theme_dropdown = ft.Dropdown(
            label="Kolor motywu",
            value=self.controller.config.get("theme", "Blue"),
            options=[
                ft.dropdown.Option("Red"),
                ft.dropdown.Option("Green"),
                ft.dropdown.Option("Blue"),
                ft.dropdown.Option("Purple"),
                ft.dropdown.Option("Orange"),
            ],
            on_change=lambda e: self.controller.change_theme(e.data),
            expand=1
        )

        self.theme_mode_dropdown = ft.Dropdown(
            label="Tryb motywu",
            value=self.controller.config.get("theme_mode", "System"),
            options=[
                ft.dropdown.Option("System"),
                ft.dropdown.Option("Jasny"),
                ft.dropdown.Option("Ciemny"),
            ],
            on_change=lambda e: self.controller.change_theme_mode(e.data),
            expand=1
        )

        # Ścieżka zapisu
        self.save_path = ft.TextField(
            label="Ścieżka zapisu",
            value=self.controller.config.get("save_path", ""),
            expand=1,
            read_only=True
        )

        self.save_path_button = ft.IconButton(
            icon=ft.icons.FOLDER_OPEN,
            tooltip="Wybierz folder",
            on_click=lambda _: self.controller.change_save_path()
        )

        # Liczba wątków
        self.threads_slider = ft.Slider(
            value=self.controller.config.get("threads", 1),
            min=1,
            max=32,
            divisions=31,
            label="{value} wątków",
            on_change=lambda e: self.controller.change_threads(e.data),
        )

        # Przełączniki
        self.switches = {
            "save_pdf": ft.Switch(
                label="Zapisuj PDF",
                value=self.controller.config.get("save_pdf", True),
                on_change=lambda e: self.controller.toggle_setting("save_pdf", e.data)
            ),
            "save_html": ft.Switch(
                label="Zapisuj HTML",
                value=self.controller.config.get("save_html", False),
                on_change=lambda e: self.controller.toggle_setting("save_html", e.data)
            ),
            "save_json": ft.Switch(
                label="Zapisuj JSON",
                value=self.controller.config.get("save_json", False),
                on_change=lambda e: self.controller.toggle_setting("save_json", e.data)
            ),
            # ... więcej przełączników
        }

        # Układamy kontrolki w kolumnach
        self.content = ft.Column(
            controls=[
                ft.Text("Ustawienia:", size=20, weight=ft.FontWeight.BOLD),

                # Motywy
                ft.Container(
                    content=ft.Column([
                        ft.Text("Wygląd", size=16),
                        self.theme_dropdown,
                        self.theme_mode_dropdown
                    ]),
                    padding=10
                ),

                # Ścieżka zapisu
                ft.Container(
                    content=ft.Column([
                        ft.Text("Zapisywanie", size=16),
                        ft.Row([
                            self.save_path,
                            self.save_path_button
                        ]),
                    ]),
                    padding=10
                ),

                # Wątki
                ft.Container(
                    content=ft.Column([
                        ft.Text("Wydajność", size=16),
                        self.threads_slider
                    ]),
                    padding=10
                ),

                # Przełączniki
                ft.Container(
                    content=ft.Column([
                        ft.Text("Opcje zapisu", size=16),
                        *self.switches.values()
                    ]),
                    padding=10
                ),
            ],
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            expand=1
        )
