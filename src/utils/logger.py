import logging
from pathlib import Path
from datetime import datetime

class Logger:
    """Klasa zarządzająca logowaniem w aplikacji"""

    def __init__(self):
        self.log_dir = Path(__file__).parent.parent.parent / "resources" / "log"
        self.log_dir.mkdir(exist_ok=True)

        self.app_log_file = self.log_dir / "app.log"
        self.error_log_file = self.log_dir / "errors.log"

        # Konfiguracja głównego loggera
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(self.app_log_file, encoding="utf-8"),
                logging.StreamHandler(),
            ],
        )

        # Konfiguracja loggera błędów
        self.error_logger = logging.getLogger("error_logger")
        self.error_logger.setLevel(logging.ERROR)
        error_handler = logging.FileHandler(self.error_log_file, encoding="utf-8")
        error_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        )
        self.error_logger.addHandler(error_handler)

    def log_error(self, message: str, raise_error: bool = False):
        """Logowanie błędów"""
        self.error_logger.error(message)
        if raise_error:
            raise Exception(message)

    def log_info(self, message: str):
        """Logowanie informacji"""
        logging.info(message)

    def clear_logs(self):
        """Czyszczenie plików logów"""
        for log_file in [self.app_log_file, self.error_log_file]:
            try:
                log_file.unlink(missing_ok=True)
                log_file.touch()
                print(f"✅ Wyczyszczono {log_file}")
            except Exception as e:
                print(f"⚠ Nie udało się wyczyścić {log_file}: {e}")

# Singleton instance
logger = Logger()
