import json
from pathlib import Path
from typing import TextIO

def read_settings(logs: bool = False) -> dict:
    path = Path(__file__).parent / "download_config.json"
    jsonloaded = dict()

    if not path.exists():
        raise FileNotFoundError(f"Plik konfiguracyjny nie istnieje: {path}")

    with open(path, "r", encoding="utf-8") as file:
        jsonloaded = json.load(file)

    if logs:
        for key, val in jsonloaded.items():
            print(f"{key}: {val}")

    return jsonloaded

def write_settings(params: dict):
    path = Path(__file__).parent / "download_config.json"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(params, file, ensure_ascii=False, indent=1)

def write_unfinished_tasks(tasks: dict):
    path = Path(__file__).parent / "unfinished_tasks.json"

    with open(path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=1)

def read_unfinished_tasks(logs=False):
    path = Path(__file__).parent / "unfinished_tasks.json"
    jsonloaded = dict()

    with open(path, "r", encoding="utf-8") as file:
        jsonloaded = json.load(file)

    if logs:
        for val in jsonloaded.values():
            print(f"{val}")

    return jsonloaded
