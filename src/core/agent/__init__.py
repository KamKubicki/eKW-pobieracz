# src/core/agent/__init__.py

from .agent import ScrapingAgent, TaskResult
from .agent_manager import AgentManager
from .work_distributor import WorkDistributor

__all__ = ['ScrapingAgent', 'TaskResult', 'AgentManager', 'WorkDistributor']