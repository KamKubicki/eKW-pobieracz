# src/ui/views/components/task_card.py

import flet as ft
from typing import Callable, Optional

class TaskCard(ft.Container):
    """Karta zadania"""

    def __init__(
        self,
        title: str,
        on_delete: Callable,
        on_start: Callable,
        on_stop: Callable,
        on_pause: Callable
    ):
        super().__init__()

        self.border = ft.border.all(1)
        self.bgcolor = ft.colors.WHITE10
        self.border_radius = ft.border_radius.all(5)
        self.padding = 5

        self.progress_bar = ft.ProgressBar(
            bgcolor="#eeeeee",
            expand=1,
            value=0,
            bar_height=6,
            border_radius=ft.border_radius.all(5),
        )

        self.status_text = ft.Text("Gotowe do rozpoczęcia", italic=True)

        self.control_buttons = ft.Row(
            controls=[
                ft.IconButton(
                    icon=ft.icons.PLAY_ARROW,
                    tooltip="Rozpocznij",
                    on_click=lambda _: on_start()
                ),
                ft.IconButton(
                    icon=ft.icons.PAUSE,
                    tooltip="Pauza",
                    on_click=lambda _: on_pause()
                ),
                ft.IconButton(
                    icon=ft.icons.STOP,
                    tooltip="Zatrzymaj",
                    on_click=lambda _: on_stop()
                ),
                ft.IconButton(
                    icon=ft.icons.DELETE_OUTLINE,
                    tooltip="Usuń",
                    on_click=lambda _: on_delete()
                ),
            ],
            alignment=ft.MainAxisAlignment.END
        )

        self.content = ft.Column(
            controls=[
                ft.Text(title, size=16, weight=ft.FontWeight.BOLD),
                self.progress_bar,
                self.status_text,
                self.control_buttons
            ],
            spacing=10
        )

    def update_progress(self, progress: float, status: str):
        """Aktualizuje postęp i status"""
        self.progress_bar.value = progress
        self.status_text.value = status
        # Aktualizujemy tylko jeśli kontrolka jest już na stronie
        if hasattr(self, '_page') and self._page:
            self.update()
