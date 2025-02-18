# src/ui/controllers/dialog_controller.py

import flet as ft
from tkinter import filedialog
from pathlib import Path
from typing import Optional, List

class DialogController:
    """Kontroler do obsługi dialogów"""

    @staticmethod
    def open_file(
        multiple: bool = False,
        file_types: Optional[List[tuple]] = None
    ) -> Optional[List[str]]:
        """Otwiera dialog wyboru pliku"""
        if file_types is None:
            file_types = [
                ("pliki txt", "*.txt"),
                ("pliki kw", "*.kw"),
                ("Wszystkie pliki", "*.*"),
            ]

        paths = filedialog.askopenfilenames(
            title="Wybierz plik lub pliki",
            filetypes=file_types
        )

        if not paths:
            return None

        return list(paths)

    @staticmethod
    def save_file(
        default_extension: str = ".txt",
        file_types: Optional[List[tuple]] = None
    ) -> Optional[Path]:
        """Otwiera dialog zapisu pliku"""
        if file_types is None:
            file_types = [
                ("pliki txt", "*.txt"),
                ("Wszystkie pliki", "*.*")
            ]

        path = filedialog.asksaveasfilename(
            title="Zapisz plik",
            defaultextension=default_extension,
            filetypes=file_types
        )

        if not path:
            return None

        return Path(path)

    @staticmethod
    def select_directory() -> Optional[Path]:
        """Otwiera dialog wyboru katalogu"""
        path = filedialog.askdirectory(
            title="Wybierz folder"
        )

        if not path:
            return None

        return Path(path)

