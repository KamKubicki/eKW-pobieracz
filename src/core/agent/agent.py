from dataclasses import dataclass
from typing import List, Optional, Dict
from datetime import datetime
import threading
import queue
import time

from src.core.scraping import LandRegisterScraper, ScrapingResult
from src.core.storage import StorageManager
from src.utils import logger
from src.config.config_manager import ConfigManager

@dataclass
class TaskResult:
    """Wynik wykonania zadania"""
    task_id: str
    kw_number: str
    status: str
    start_time: datetime
    end_time: datetime
    error: Optional[str] = None
    files: List[str] = None

class ScrapingAgent:
    """
    Agent odpowiedzialny za wykonywanie zadań scrapingu
    """

    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.config = ConfigManager()
        self.scraper = LandRegisterScraper()
        self.storage = StorageManager()

        self.task_queue = queue.Queue()
        self.results = []
        self.is_running = False
        self.current_task = None

        # Statystyki
        self.tasks_completed = 0
        self.tasks_failed = 0
        self.start_time = None

    def add_task(self, task_id: str, kw_number: str):
        """Dodaje nowe zadanie do kolejki"""
        self.task_queue.put((task_id, kw_number))
        logger.log_info(f"Agent {self.agent_id}: Dodano zadanie {task_id} dla KW {kw_number}")

    def start(self):
        """Uruchamia agenta"""
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.worker_thread = threading.Thread(target=self._worker)
            self.worker_thread.start()
            logger.log_info(f"Agent {self.agent_id}: Uruchomiono")

    def stop(self):
        """Zatrzymuje agenta"""
        self.is_running = False
        if self.worker_thread:
            self.worker_thread.join()
        self.scraper.close()
        logger.log_info(f"Agent {self.agent_id}: Zatrzymano")

    def pause(self):
        """Wstrzymuje pracę agenta"""
        self.is_running = False
        logger.log_info(f"Agent {self.agent_id}: Wstrzymano")

    def resume(self):
        """Wznawia pracę agenta"""
        self.start()
        logger.log_info(f"Agent {self.agent_id}: Wznowiono")

    def _worker(self):
        """Główna pętla robocza agenta"""
        while self.is_running:
            try:
                # Pobranie zadania z kolejki
                if self.task_queue.empty():
                    time.sleep(1)
                    continue

                task_id, kw_number = self.task_queue.get(timeout=1)
                self.current_task = (task_id, kw_number)

                start_time = datetime.now()

                try:
                    # Wykonanie zadania
                    result = self._process_task(kw_number)

                    # Zapisanie wyniku
                    task_result = TaskResult(
                        task_id=task_id,
                        kw_number=kw_number,
                        status="SUCCESS" if result.success else "FAILED",
                        start_time=start_time,
                        end_time=datetime.now(),
                        error=None if result.success else result.message,
                        files=[str(f) for f in (result.files or [])]
                    )

                    self.results.append(task_result)

                    if result.success:
                        self.tasks_completed += 1
                    else:
                        self.tasks_failed += 1

                except Exception as e:
                    logger.log_error(f"Agent {self.agent_id}: Błąd podczas przetwarzania zadania {task_id}: {e}")
                    self.tasks_failed += 1

                finally:
                    self.current_task = None
                    self.task_queue.task_done()

            except queue.Empty:
                continue
            except Exception as e:
                logger.log_error(f"Agent {self.agent_id}: Błąd w pętli roboczej: {e}")

    def _process_task(self, kw_number: str) -> ScrapingResult:
        """Przetwarza pojedyncze zadanie"""
        try:
            # Pobranie danych
            result = self.scraper.scrape_register(kw_number)

            if result.success and result.data:
                # Zapis danych
                self.storage.save_all_formats(
                    kw_number=kw_number,
                    pdf_data=result.data.get("pdf"),
                    html_content=result.data.get("html"),
                    json_data=result.data,
                    csv_data=[result.data]
                )

            return result

        except Exception as e:
            logger.log_error(f"Agent {self.agent_id}: Błąd podczas przetwarzania KW {kw_number}: {e}")
            return ScrapingResult(False, str(e))

    def get_status(self) -> Dict:
        """Zwraca aktualny status agenta"""
        return {
            "agent_id": self.agent_id,
            "is_running": self.is_running,
            "current_task": self.current_task,
            "queue_size": self.task_queue.qsize(),
            "tasks_completed": self.tasks_completed,
            "tasks_failed": self.tasks_failed,
            "uptime": str(datetime.now() - self.start_time) if self.start_time else "0:00:00",
            "success_rate": f"{(self.tasks_completed / (self.tasks_completed + self.tasks_failed)) * 100:.2f}%"
                           if (self.tasks_completed + self.tasks_failed) > 0 else "N/A"
        }
