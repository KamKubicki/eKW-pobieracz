import time
from typing import List, Optional
import flet as ft
from dataclasses import dataclass
import threading

from src.core.agent import WorkDistributor
from src.utils import logger
from .base_controller import BaseController


@dataclass
class DownloadTask:
    """Reprezentacja zadania pobierania"""
    name: str
    path: str
    type: str = "list"  # "list", "generator" lub "clipboard"
    status: str = "pending"
    progress: float = 0
    message: str = "Oczekuje na rozpoczęcie"

    # Dodajemy parametry dla generatora
    generator_params: dict = None


class DownloadController(BaseController):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.tasks: List[DownloadTask] = []
        self.distributor = WorkDistributor()
        self.processing_thread: Optional[threading.Thread] = None

    def add_generator_task(self):
        """Dodaje nowe zadanie generatora"""
        # Tworzymy zadanie z domyślnymi parametrami generatora
        task = DownloadTask(
            name="Generator",
            path="",
            type="generator",
            generator_params={
                "sad": "",
                "start": "",
                "end": "",
                "last_digit": "",
                "control_digit": ""
            }
        )
        self.tasks.append(task)
        self._show_generator_dialog(task)
        self.update()

    def _show_generator_dialog(self, task: DownloadTask):
        """Pokazuje dialog konfiguracji generatora"""

        def close_dialog():
            dialog.open = False
            self.page.update()

        def save_generator_params():
            task.generator_params.update({
                "sad": sad_input.value,
                "start": start_input.value,
                "end": end_input.value,
                "last_digit": last_digit_input.value,
                "control_digit": control_digit_input.value
            })
            task.name = f"Generator: {sad_input.value} ({start_input.value}-{end_input.value})"
            close_dialog()
            self.update()

        # Tworzenie kontrolek formularza
        sad_input = ft.TextField(
            label="Oznaczenie sądu",
            value=task.generator_params.get("sad", ""),
            hint_text="np. BB1B"
        )

        start_input = ft.TextField(
            label="Początek zakresu",
            value=task.generator_params.get("start", ""),
            hint_text="np. 00000001"
        )

        end_input = ft.TextField(
            label="Koniec zakresu",
            value=task.generator_params.get("end", ""),
            hint_text="np. 00000100"
        )

        last_digit_input = ft.TextField(
            label="Ostatnia cyfra (opcjonalnie)",
            value=task.generator_params.get("last_digit", ""),
            hint_text="np. 1"
        )

        control_digit_input = ft.TextField(
            label="Cyfra kontrolna (opcjonalnie)",
            value=task.generator_params.get("control_digit", ""),
            hint_text="np. 7"
        )

        # Tworzenie dialogu
        dialog = ft.AlertDialog(
            title=ft.Text("Konfiguracja generatora"),
            content=ft.Column(
                controls=[
                    sad_input,
                    start_input,
                    end_input,
                    last_digit_input,
                    control_digit_input,
                ],
                tight=True,
                spacing=10
            ),
            actions=[
                ft.TextButton("Anuluj", on_click=lambda _: close_dialog()),
                ft.TextButton("Zapisz", on_click=lambda _: save_generator_params()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        # Pokazanie dialogu
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def _create_view(self) -> ft.Control:
        """Tworzy widok kontrolera"""
        from src.ui.views.download_view import DownloadView
        return DownloadView(self)

    def process_generator_task(self, task: DownloadTask):
        """Przetwarza zadanie generatora"""
        try:
            from src.scraper.eKW_generator import kw_from_range

            params = task.generator_params
            last_digit = int(params["last_digit"]) if params["last_digit"].isdigit() else -1
            control_digit = int(params["control_digit"]) if params["control_digit"].isdigit() else -1

            # Generowanie numerów KW
            kw_numbers = list(kw_from_range(
                params["sad"],
                int(params["start"]),
                int(params["end"]),
                last_digit,
                control_digit
            ))

            # Aktualizacja statusu
            task.message = f"Wygenerowano {len(kw_numbers)} numerów KW"
            task.progress = 0.5
            self.update()

            # Rozpoczęcie pobierania
            self.distributor.start_processing(kw_numbers)

            # Monitorowanie postępu
            total = len(kw_numbers)
            while True:
                progress = self.distributor.get_progress()
                completed = progress["completed"] + progress["failed"]

                task.progress = 0.5 + (completed / total) * 0.5
                task.message = f"Przetworzono: {completed}/{total}"
                self.update()

                if completed == total:
                    break

                time.sleep(1)

            task.status = "completed"
            task.message = f"Zakończono. Pobrano {progress['completed']}/{total} KW"

        except Exception as e:
            task.status = "failed"
            task.message = f"Błąd: {str(e)}"
            logger.log_error(f"Błąd podczas przetwarzania zadania generatora: {e}")

        finally:
            self.update()