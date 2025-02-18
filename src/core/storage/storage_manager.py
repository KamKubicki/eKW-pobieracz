from typing import Dict, List, Optional
from pathlib import Path

from .storage_interface import StorageInterface, StorageResult
from .file_storage import FileStorage
from src.utils import logger

class StorageManager:
    """
    Manager zarządzający zapisem danych w różnych formatach
    """

    def __init__(self, storage: Optional[StorageInterface] = None):
        self.storage = storage or FileStorage()

    def save_all_formats(
        self,
        kw_number: str,
        pdf_data: Optional[bytes] = None,
        html_content: Optional[str] = None,
        json_data: Optional[Dict] = None,
        csv_data: Optional[List[Dict]] = None
    ) -> List[StorageResult]:
        """
        Zapisuje dane we wszystkich wymaganych formatach

        Args:
            kw_number: Numer księgi wieczystej (używany jako nazwa pliku)
            pdf_data: Dane PDF w formacie bajtowym
            html_content: Zawartość HTML
            json_data: Dane do zapisu w JSON
            csv_data: Dane do zapisu w CSV

        Returns:
            Lista wyników operacji zapisu
        """
        results = []
        filename = kw_number.replace("/", ".")

        # Zapis PDF
        if pdf_data:
            results.append(self.storage.save_pdf(pdf_data, filename))

        # Zapis HTML
        if html_content:
            results.append(self.storage.save_html(html_content, filename))

        # Zapis JSON
        if json_data:
            results.append(self.storage.save_json(json_data, filename))

        # Zapis CSV
        if csv_data:
            results.append(self.storage.save_csv(csv_data, filename))

        return results

    def merge_pdf_files(self, filenames: List[str], output_filename: str) -> StorageResult:
        """
        Łączy wiele plików PDF w jeden

        Args:
            filenames: Lista nazw plików do połączenia
            output_filename: Nazwa pliku wynikowego

        Returns:
            Wynik operacji
        """
        try:
            import pypdf

            merger = pypdf.PdfMerger()

            for filename in filenames:
                file_path = self.storage.get_file_path(filename)
                if file_path.exists():
                    merger.append(str(file_path))

            output_path = self.storage.get_file_path(output_filename)
            merger.write(str(output_path))
            merger.close()

            # Usuń oryginalne pliki
            for filename in filenames:
                file_path = self.storage.get_file_path(filename)
                if file_path.exists():
                    file_path.unlink()

            return StorageResult(True, "Połączono pliki PDF", output_path)

        except Exception as e:
            logger.log_error(f"Błąd podczas łączenia plików PDF: {e}")
            return StorageResult(False, str(e))
