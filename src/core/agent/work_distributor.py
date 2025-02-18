# src/core/agent/work_distributor.py

from typing import List, Optional
import threading
import time

from .agent_manager import AgentManager
from src.utils import logger
from src.config.config_manager import ConfigManager

class WorkDistributor:
    """
    Klasa odpowiedzialna za dystrybucję pracy między agentami
    """

    def __init__(self):
        self.config = ConfigManager()
        self.agent_manager = AgentManager()
        self.is_running = False
        self.lock = threading.Lock()

        # Utworzenie początkowej puli agentów
        self._initialize_agents()

    def _initialize_agents(self):
        """Inicjalizuje początkową pulę agentów"""
        num_agents = self.config.get("threads", 1)
        for _ in range(num_agents):
            self.agent_manager.create_agent()

    def start_processing(self, kw_numbers: List[str]):
        """
        Rozpoczyna przetwarzanie listy numerów KW

        Args:
            kw_numbers: Lista numerów KW do przetworzenia
        """
        with self.lock:
            self.is_running = True

            # Uruchom wszystkich agentów
            self.agent_manager.start_all_agents()

            # Dodaj zadania do kolejki
            task_ids = self.agent_manager.add_tasks_batch(kw_numbers)

            logger.log_info(f"Rozpoczęto przetwarzanie {len(kw_numbers)} numerów KW")

            return task_ids

    def stop_processing(self):
        """Zatrzymuje przetwarzanie"""
        with self.lock:
            self.is_running = False
            self.agent_manager.stop_all_agents()
            logger.log_info("Zatrzymano przetwarzanie")

    def get_progress(self) -> dict:
        """Zwraca postęp przetwarzania"""
        statuses = self.agent_manager.get_all_agents_status()

        total_completed = sum(s["tasks_completed"] for s in statuses.values())
        total_failed = sum(s["tasks_failed"] for s in statuses.values())
        total_tasks = sum(s["queue_size"] for s in statuses.values()) + total_completed + total_failed

        return {
            "total_tasks": total_tasks,
            "completed": total_completed,
            "failed": total_failed,
            "in_progress": total_tasks - (total_completed + total_failed),
            "success_rate": f"{(total_completed / total_tasks * 100):.2f}%" if total_tasks > 0 else "N/A",
            "agent_statuses": statuses
        }
