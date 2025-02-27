# src/ui/views/download_view.py

import flet as ft
from .components.base_view import BaseView
from .components.task_card import TaskCard

class DownloadView(BaseView):
    """Widok pobierania danych"""

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.page = controller.page

        # Lista zadań
        self.tasks_column = ft.Column(
            scroll=ft.ScrollMode.AUTO,
            expand=1,
            spacing=10
        )

        # Przycisk dodawania zadań
        self.add_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            tooltip="Dodaj nowe zadanie",
            on_click=self._show_add_task_dialog
        )

        # Dialog dodawania zadań
        self.add_task_dialog = ft.BottomSheet(
            content=ft.Container(
                padding=5,
                content=ft.Column(
                    tight=True,
                    controls=[
                        ft.ElevatedButton(
                            text="Lista z pliku txt",
                            icon=ft.icons.FILE_UPLOAD,
                            expand=1,
                            on_click=lambda _: self._add_file_task()
                        ),
                        ft.ElevatedButton(
                            text="Lista ze schowka",
                            icon=ft.icons.PASTE,
                            expand=1,
                            on_click=lambda _: self._add_clipboard_task()
                        ),
                        ft.ElevatedButton(
                            text="Generator",
                            icon=ft.icons.BUILD,
                            expand=1,
                            on_click=lambda _: self._add_generator_task()
                        ),
                        ft.ElevatedButton(
                            text="Anuluj",
                            expand=1,
                            on_click=lambda _: self.page.close(self.add_task_dialog)
                        ),
                    ],
                ),
            ),
        )

        self.content = ft.Column(
            controls=[
                ft.Text("Lista zadań:", size=20, weight=ft.FontWeight.BOLD),
                self.tasks_column,
                ft.Row(
                    controls=[self.add_button],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            spacing=20,
            expand=1
        )

    # def _show_add_task_dialog(self, _):
    #     """Pokazuje dialog dodawania zadań"""
    #     self.add_task_dialog.open = True
    #     self.update()
    def _show_add_task_dialog(self, _):
        """Pokazuje dialog dodawania zadań"""
        self.page.open(self.add_task_dialog)
        # self.add_task_dialog.open = True
        self.page.update()

    def update_tasks(self):
        """Aktualizuje listę zadań"""
        self.tasks_column.controls.clear()

        for task in self.controller.tasks:
            card = TaskCard(
                title=task.name,
                on_delete=lambda t=task: self.controller.remove_task(t),
                on_start=lambda t=task: self.controller.start_task(t),
                on_stop=lambda t=task: self.controller.stop_task(t),
                on_pause=lambda t=task: self.controller.pause_task(t)
            )
            self.tasks_column.controls.append(card)  # Najpierw dodajemy do strony
            card.update_progress(task.progress, task.message)  # Potem aktualizujemy

        self.update()

    def _add_file_task(self):
        """Dodaje zadanie z pliku"""
        self._close_dialog()
        self.controller.add_file_task()

    def _add_clipboard_task(self):
        """Dodaje zadanie ze schowka"""
        self._close_dialog()
        self.controller.add_clipboard_task()

    def _close_dialog(self):
        """Zamyka dialog"""
        if self.add_task_dialog:
            self.add_task_dialog.open = False
            self.page.update()

    def _add_generator_task(self):
        """Dodaje zadanie generatora"""
        self._close_dialog()
        self.controller.add_generator_task()

    def update_tasks(self):
        """Aktualizuje listę zadań"""
        self.tasks_column.controls.clear()

        for task in self.controller.tasks:
            card = TaskCard(
                title=task.name,
                on_delete=lambda: self.controller.remove_task(task),
                on_start=lambda: self.controller.start_task(task),
                on_stop=lambda: self.controller.stop_task(task),
                on_pause=lambda: self.controller.pause_task(task)
            )
            card.update_progress(task.progress, task.message)
            self.tasks_column.controls.append(card)

        self.update()
