# src/core/storage/__init__.py

from .storage_interface import StorageInterface, StorageResult
from .file_storage import FileStorage
from .storage_manager import StorageManager

__all__ = ['StorageInterface', 'StorageResult', 'FileStorage', 'StorageManager']