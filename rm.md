# eKW-pobieracz

Aplikacja do pobierania danych z elektronicznych ksiąg wieczystych.

## Instalacja

1. Sklonuj repozytorium:
```bash
git clone https://github.com/user/ekw-pobieracz.git
cd ekw-pobieracz
```

2. Utwórz i aktywuj wirtualne środowisko (opcjonalnie):
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Zainstaluj wymagane pakiety:
```bash
pip install -r requirements.txt
```

## Uruchomienie

```bash
python run.py
```

## Funkcje

- Pobieranie danych z pojedynczej księgi wieczystej
- Pobieranie danych z listy ksiąg wieczystych
- Generator numerów ksiąg wieczystych
- Zapis w różnych formatach (PDF, HTML, JSON, CSV)
- Wielowątkowe pobieranie danych
- Konfigurowalny interfejs użytkownika

## Konfiguracja

Ustawienia aplikacji znajdują się w pliku `src/config/download_config.json`.

## Logowanie

Logi aplikacji znajdują się w katalogu `resources/log/`:
- `app.log` - główny log aplikacji
- `errors.log` - log błędów

## Licencja
