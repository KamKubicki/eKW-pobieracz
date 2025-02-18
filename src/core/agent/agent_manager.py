from typing import Dict, List, Optional
import threading
import uuid

from .agent import ScrapingAgent
from src.utils import logger
from src.config.config_manager import ConfigManager

class AgentManager:
    """
    Zarządza pulą agentów scrapujących
    """

    def __init__(self):
        self.config = ConfigManager()
        self.agents: Dict[str, ScrapingAgent] = {}
        self.tasks: Dict[str, List[str]] = {}  # agent_id -> [task_ids]
        self.lock = threading.Lock()

    def create_agent(self) -> str:
        """
        Tworzy nowego agenta

        Returns:
            ID utworzonego agenta
        """
        with self.lock:
            agent_id = str(uuid.uuid4())
            self.agents[agent_id] = ScrapingAgent(agent_id)
            self.tasks[agent_id] = []
            logger.log_info(f"Utworzono nowego agenta: {agent_id}")
            return agent_id

    def remove_agent(self, agent_id: str):
        """Usuwa agenta"""
        with self.lock:
            if agent_id in self.agents:
                self.agents[agent_id].stop()
                del self.agents[agent_id]
                del self.tasks[agent_id]
                logger.log_info(f"Usunięto agenta: {agent_id}")

    def start_agent(self, agent_id: str):
        """Uruchamia agenta"""
        if agent_id in self.agents:
            self.agents[agent_id].start()

    def stop_agent(self, agent_id: str):
        """Zatrzymuje agenta"""
        if agent_id in self.agents:
            self.agents[agent_id].stop()

    def add_task(self, kw_number: str) -> str:
        """
        Dodaje nowe zadanie i przydziela je do agenta

        Args:
            kw_number: Numer księgi wieczystej

        Returns:
            ID zadania
        """
        with self.lock:
            task_id = str(uuid.uuid4())

            # Wybierz agenta z najmniejszą liczbą zadań
            agent_id = min(self.tasks.items(), key=lambda x: len(x[1]))[0]

            # Dodaj zadanie do agenta
            self.agents[agent_id].add_task(task_id, kw_number)
            self.tasks[agent_id].append(task_id)

            logger.log_info(f"Dodano zadanie {task_id} do agenta {agent_id}")
            return task_id

    def add_tasks_batch(self, kw_numbers: List[str]) -> List[str]:
        """Dodaje wiele zadań jednocześnie"""
        return [self.add_task(kw) for kw in kw_numbers]

    def get_agent_status(self, agent_id: str) -> Optional[Dict]:
        """Zwraca status agenta"""
        if agent_id in self.agents:
            return self.agents[agent_id].get_status()
        return None

    def get_all_agents_status(self) -> Dict[str, Dict]:
        """Zwraca status wszystkich agentów"""
        return {
            agent_id: agent.get_status()
            for agent_id, agent in self.agents.items()
        }

    def start_all_agents(self):
        """Uruchamia wszystkich agentów"""
        for agent_id in self.agents:
            self.start_agent(agent_id)

    def stop_all_agents(self):
        """Zatrzymuje wszystkich agentów"""
        for agent_id in self.agents:
            self.stop_agent(agent_id)
