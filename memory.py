"""
Memory System - A simple in-memory key-value store with monitoring capabilities.

This module provides a Memory class that implements a basic memory management system
with support for storing, retrieving, and managing data in memory.
"""

from typing import Any, Dict, List, Optional
import time
from datetime import datetime


class Memory:
    """
    A memory management system that provides key-value storage with statistics.
    
    Features:
    - Store and retrieve data by key
    - Delete data
    - Clear all data
    - Track memory usage statistics
    - Monitor access patterns
    """
    
    def __init__(self):
        """Initialize an empty memory store."""
        self._store: Dict[str, Any] = {}
        self._metadata: Dict[str, Dict[str, Any]] = {}
        self._stats = {
            'total_reads': 0,
            'total_writes': 0,
            'total_deletes': 0,
            'creation_time': datetime.now()
        }
    
    def set(self, key: str, value: Any) -> None:
        """
        Store a value in memory with the given key.
        
        Args:
            key: The key to store the value under
            value: The value to store
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        is_new = key not in self._store
        existing_metadata = self._metadata.get(key, {})
        
        self._store[key] = value
        self._metadata[key] = {
            'created_at': datetime.now() if is_new else existing_metadata.get('created_at', datetime.now()),
            'updated_at': datetime.now(),
            'access_count': existing_metadata.get('access_count', 0)
        }
        self._stats['total_writes'] += 1
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value from memory by key.
        
        Args:
            key: The key to retrieve
            default: Default value to return if key doesn't exist
            
        Returns:
            The stored value or default if key doesn't exist
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        self._stats['total_reads'] += 1
        
        if key in self._store:
            self._metadata[key]['access_count'] += 1
            self._metadata[key]['last_accessed'] = datetime.now()
            return self._store[key]
        
        return default
    
    def delete(self, key: str) -> bool:
        """
        Delete a value from memory.
        
        Args:
            key: The key to delete
            
        Returns:
            True if the key was deleted, False if it didn't exist
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        if key in self._store:
            del self._store[key]
            del self._metadata[key]
            self._stats['total_deletes'] += 1
            return True
        return False
    
    def contains(self, key: str) -> bool:
        """
        Check if a key exists in memory.
        
        Args:
            key: The key to check
            
        Returns:
            True if the key exists, False otherwise
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        return key in self._store
    
    def clear(self) -> None:
        """Clear all data from memory."""
        self._store.clear()
        self._metadata.clear()
    
    def size(self) -> int:
        """
        Get the number of items in memory.
        
        Returns:
            The number of stored items
        """
        return len(self._store)
    
    def keys(self) -> List[str]:
        """
        Get all keys in memory.
        
        Returns:
            A list of all keys
        """
        return list(self._store.keys())
    
    def values(self) -> List[Any]:
        """
        Get all values in memory.
        
        Returns:
            A list of all values
        """
        return list(self._store.values())
    
    def items(self) -> List[tuple]:
        """
        Get all key-value pairs in memory.
        
        Returns:
            A list of (key, value) tuples
        """
        return list(self._store.items())
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get memory usage statistics.
        
        Returns:
            A dictionary containing usage statistics
        """
        return {
            'total_items': len(self._store),
            'total_reads': self._stats['total_reads'],
            'total_writes': self._stats['total_writes'],
            'total_deletes': self._stats['total_deletes'],
            'creation_time': self._stats['creation_time'],
            'uptime_seconds': (datetime.now() - self._stats['creation_time']).total_seconds()
        }
    
    def get_metadata(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Get metadata for a specific key.
        
        Args:
            key: The key to get metadata for
            
        Returns:
            Metadata dictionary or None if key doesn't exist
        """
        if not isinstance(key, str):
            raise TypeError("Key must be a string")
        
        return self._metadata.get(key)
    
    def __len__(self) -> int:
        """Return the number of items in memory."""
        return len(self._store)
    
    def __contains__(self, key: str) -> bool:
        """Support 'in' operator."""
        return key in self._store
    
    def __getitem__(self, key: str) -> Any:
        """Support bracket notation for getting values."""
        if key not in self._store:
            raise KeyError(f"Key '{key}' not found in memory")
        return self.get(key)
    
    def __setitem__(self, key: str, value: Any) -> None:
        """Support bracket notation for setting values."""
        self.set(key, value)
    
    def __delitem__(self, key: str) -> None:
        """Support del operator."""
        if not self.delete(key):
            raise KeyError(f"Key '{key}' not found in memory")
    
    def __repr__(self) -> str:
        """Return a string representation of the memory store."""
        return f"Memory(size={len(self._store)}, items={list(self._store.keys())})"
