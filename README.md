# Memory System

A simple, efficient in-memory key-value store with monitoring and statistics capabilities.

## Features

- **Key-Value Storage**: Store and retrieve data using string keys
- **Multiple Data Types**: Support for any Python data type (strings, integers, lists, dictionaries, etc.)
- **Statistics Tracking**: Monitor reads, writes, and deletes
- **Metadata**: Track creation time, update time, and access patterns for each key
- **Pythonic Interface**: Supports bracket notation, `in` operator, `len()`, and more
- **Memory Management**: Clear, delete, and manage stored data efficiently

## Installation

No external dependencies required! Just use the `memory.py` module directly.

## Quick Start

```python
from memory import Memory

# Create a new memory instance
mem = Memory()

# Store data
mem.set('username', 'john_doe')
mem.set('age', 30)

# Retrieve data
username = mem.get('username')  # Returns 'john_doe'
age = mem['age']  # Bracket notation also works

# Check existence
if 'username' in mem:
    print("Username exists!")

# Delete data
mem.delete('age')

# Get statistics
stats = mem.get_stats()
print(f"Total items: {stats['total_items']}")
```

## API Reference

### Basic Operations

- `set(key, value)` - Store a value with the given key
- `get(key, default=None)` - Retrieve a value by key, return default if not found
- `delete(key)` - Delete a key-value pair, returns True if deleted
- `contains(key)` - Check if a key exists
- `clear()` - Remove all data from memory

### Querying

- `size()` - Get the number of items stored
- `keys()` - Get a list of all keys
- `values()` - Get a list of all values
- `items()` - Get a list of (key, value) tuples

### Statistics & Metadata

- `get_stats()` - Get memory usage statistics (reads, writes, deletes, uptime)
- `get_metadata(key)` - Get metadata for a specific key (creation time, access count, etc.)

### Python Magic Methods

The Memory class supports Python's standard operators:

```python
mem = Memory()

# Bracket notation
mem['key'] = 'value'
value = mem['key']
del mem['key']

# Membership testing
if 'key' in mem:
    print("Key exists!")

# Length
count = len(mem)

# String representation
print(mem)  # Memory(size=3, items=['key1', 'key2', 'key3'])
```

## Examples

### Storing Complex Data

```python
mem = Memory()

# Store a dictionary
mem['user'] = {
    'name': 'Alice',
    'email': 'alice@example.com',
    'roles': ['admin', 'user']
}

# Store a list
mem['scores'] = [95, 87, 92, 88]

# Retrieve and use
user = mem['user']
print(f"User: {user['name']}")
```

### Tracking Access Patterns

```python
mem = Memory()
mem['counter'] = 0

# Access the key multiple times
for _ in range(5):
    mem.get('counter')

# Check metadata
metadata = mem.get_metadata('counter')
print(f"Access count: {metadata['access_count']}")
print(f"Last accessed: {metadata['last_accessed']}")
```

### Using Statistics

```python
mem = Memory()

# Perform operations
mem.set('a', 1)
mem.set('b', 2)
mem.get('a')
mem.delete('b')

# View statistics
stats = mem.get_stats()
print(f"Total writes: {stats['total_writes']}")
print(f"Total reads: {stats['total_reads']}")
print(f"Total deletes: {stats['total_deletes']}")
print(f"Current items: {stats['total_items']}")
```

## Running Tests

```bash
python test_memory.py
```

## Running Examples

```bash
python example.py
```

## Use Cases

- **Caching**: Store frequently accessed data in memory
- **Session Management**: Keep user session data
- **Configuration Storage**: Store application settings
- **Temporary Data**: Hold intermediate computation results
- **Testing**: Mock database operations in tests

## License

Open source - free to use and modify.