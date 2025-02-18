import os
import sys
import traceback
from pathlib import Path


def setup_environment():
    """Konfiguruje środowisko uruchomieniowe"""
    project_root = Path(__file__).parent
    sys.path.append(str(project_root))
    (project_root / "resources" / "log").mkdir(parents=True, exist_ok=True)
    os.environ["EKW_ROOT"] = str(project_root)


if __name__ == "__main__":
    setup_environment()

    try:
        from src.main import main
        import flet as ft

        ft.app(target=main)

    except ImportError as e:
        print(f"Błąd importu modułów: {e}")
        print("Upewnij się, że wszystkie wymagane pakiety są zainstalowane:")
        print("pip install -r requirements.txt")
        traceback.print_exc()  # Dodajemy pełny stack trace
        sys.exit(1)
    except Exception as e:
        print(f"Nieoczekiwany błąd: {e}")
        print("Pełny stack trace:")
        traceback.print_exc()  # Dodajemy pełny stack trace
        sys.exit(1)