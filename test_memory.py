"""
Test suite for the Memory system.
"""

import unittest
import time
from memory import Memory


class TestMemory(unittest.TestCase):
    """Test cases for the Memory class."""
    
    def setUp(self):
        """Set up a fresh Memory instance for each test."""
        self.memory = Memory()
    
    def test_initialization(self):
        """Test that Memory initializes correctly."""
        self.assertEqual(self.memory.size(), 0)
        self.assertEqual(len(self.memory), 0)
    
    def test_set_and_get(self):
        """Test basic set and get operations."""
        self.memory.set('key1', 'value1')
        self.assertEqual(self.memory.get('key1'), 'value1')
    
    def test_set_multiple_values(self):
        """Test storing multiple values."""
        self.memory.set('key1', 'value1')
        self.memory.set('key2', 'value2')
        self.memory.set('key3', 'value3')
        
        self.assertEqual(self.memory.get('key1'), 'value1')
        self.assertEqual(self.memory.get('key2'), 'value2')
        self.assertEqual(self.memory.get('key3'), 'value3')
        self.assertEqual(self.memory.size(), 3)
    
    def test_get_nonexistent_key(self):
        """Test getting a key that doesn't exist."""
        self.assertIsNone(self.memory.get('nonexistent'))
    
    def test_get_with_default(self):
        """Test getting with a default value."""
        self.assertEqual(self.memory.get('nonexistent', 'default'), 'default')
    
    def test_update_existing_key(self):
        """Test updating an existing key."""
        self.memory.set('key1', 'value1')
        self.memory.set('key1', 'value2')
        self.assertEqual(self.memory.get('key1'), 'value2')
        self.assertEqual(self.memory.size(), 1)
    
    def test_delete(self):
        """Test deleting a key."""
        self.memory.set('key1', 'value1')
        self.assertTrue(self.memory.delete('key1'))
        self.assertIsNone(self.memory.get('key1'))
        self.assertEqual(self.memory.size(), 0)
    
    def test_delete_nonexistent(self):
        """Test deleting a nonexistent key."""
        self.assertFalse(self.memory.delete('nonexistent'))
    
    def test_contains(self):
        """Test the contains method."""
        self.memory.set('key1', 'value1')
        self.assertTrue(self.memory.contains('key1'))
        self.assertFalse(self.memory.contains('key2'))
    
    def test_clear(self):
        """Test clearing all data."""
        self.memory.set('key1', 'value1')
        self.memory.set('key2', 'value2')
        self.memory.clear()
        self.assertEqual(self.memory.size(), 0)
        self.assertIsNone(self.memory.get('key1'))
    
    def test_size(self):
        """Test the size method."""
        self.assertEqual(self.memory.size(), 0)
        self.memory.set('key1', 'value1')
        self.assertEqual(self.memory.size(), 1)
        self.memory.set('key2', 'value2')
        self.assertEqual(self.memory.size(), 2)
        self.memory.delete('key1')
        self.assertEqual(self.memory.size(), 1)
    
    def test_keys(self):
        """Test getting all keys."""
        self.memory.set('key1', 'value1')
        self.memory.set('key2', 'value2')
        keys = self.memory.keys()
        self.assertEqual(len(keys), 2)
        self.assertIn('key1', keys)
        self.assertIn('key2', keys)
    
    def test_values(self):
        """Test getting all values."""
        self.memory.set('key1', 'value1')
        self.memory.set('key2', 'value2')
        values = self.memory.values()
        self.assertEqual(len(values), 2)
        self.assertIn('value1', values)
        self.assertIn('value2', values)
    
    def test_items(self):
        """Test getting all items."""
        self.memory.set('key1', 'value1')
        self.memory.set('key2', 'value2')
        items = self.memory.items()
        self.assertEqual(len(items), 2)
        self.assertIn(('key1', 'value1'), items)
        self.assertIn(('key2', 'value2'), items)
    
    def test_stats(self):
        """Test statistics tracking."""
        self.memory.set('key1', 'value1')
        self.memory.get('key1')
        self.memory.get('key1')
        self.memory.delete('key1')
        
        stats = self.memory.get_stats()
        self.assertEqual(stats['total_items'], 0)
        self.assertEqual(stats['total_writes'], 1)
        self.assertEqual(stats['total_reads'], 2)
        self.assertEqual(stats['total_deletes'], 1)
        self.assertIn('creation_time', stats)
        self.assertIn('uptime_seconds', stats)
    
    def test_metadata(self):
        """Test metadata tracking."""
        self.memory.set('key1', 'value1')
        time.sleep(0.01)  # Small delay to ensure different timestamps
        self.memory.get('key1')
        
        metadata = self.memory.get_metadata('key1')
        self.assertIsNotNone(metadata)
        self.assertIn('created_at', metadata)
        self.assertIn('updated_at', metadata)
        self.assertIn('access_count', metadata)
        self.assertIn('last_accessed', metadata)
        self.assertEqual(metadata['access_count'], 1)
    
    def test_metadata_nonexistent(self):
        """Test getting metadata for nonexistent key."""
        self.assertIsNone(self.memory.get_metadata('nonexistent'))
    
    def test_bracket_notation_get(self):
        """Test bracket notation for getting values."""
        self.memory.set('key1', 'value1')
        self.assertEqual(self.memory['key1'], 'value1')
    
    def test_bracket_notation_set(self):
        """Test bracket notation for setting values."""
        self.memory['key1'] = 'value1'
        self.assertEqual(self.memory.get('key1'), 'value1')
    
    def test_bracket_notation_delete(self):
        """Test del operator."""
        self.memory.set('key1', 'value1')
        del self.memory['key1']
        self.assertIsNone(self.memory.get('key1'))
    
    def test_in_operator(self):
        """Test 'in' operator."""
        self.memory.set('key1', 'value1')
        self.assertIn('key1', self.memory)
        self.assertNotIn('key2', self.memory)
    
    def test_len(self):
        """Test len() function."""
        self.assertEqual(len(self.memory), 0)
        self.memory.set('key1', 'value1')
        self.assertEqual(len(self.memory), 1)
    
    def test_repr(self):
        """Test string representation."""
        self.memory.set('key1', 'value1')
        repr_str = repr(self.memory)
        self.assertIn('Memory', repr_str)
        self.assertIn('key1', repr_str)
    
    def test_various_data_types(self):
        """Test storing various data types."""
        self.memory.set('int', 42)
        self.memory.set('float', 3.14)
        self.memory.set('list', [1, 2, 3])
        self.memory.set('dict', {'a': 1, 'b': 2})
        self.memory.set('tuple', (1, 2, 3))
        self.memory.set('bool', True)
        
        self.assertEqual(self.memory.get('int'), 42)
        self.assertEqual(self.memory.get('float'), 3.14)
        self.assertEqual(self.memory.get('list'), [1, 2, 3])
        self.assertEqual(self.memory.get('dict'), {'a': 1, 'b': 2})
        self.assertEqual(self.memory.get('tuple'), (1, 2, 3))
        self.assertEqual(self.memory.get('bool'), True)
    
    def test_key_type_validation(self):
        """Test that only string keys are accepted."""
        with self.assertRaises(TypeError):
            self.memory.set(123, 'value')
        
        with self.assertRaises(TypeError):
            self.memory.get(123)
        
        with self.assertRaises(TypeError):
            self.memory.delete(123)
        
        with self.assertRaises(TypeError):
            self.memory.contains(123)
        
        with self.assertRaises(TypeError):
            self.memory.get_metadata(123)
    
    def test_bracket_notation_keyerror(self):
        """Test that bracket notation raises KeyError for missing keys."""
        with self.assertRaises(KeyError):
            _ = self.memory['nonexistent']
        
        with self.assertRaises(KeyError):
            del self.memory['nonexistent']


if __name__ == '__main__':
    unittest.main()
