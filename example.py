"""
Example usage of the Memory system.
"""

from memory import Memory


def main():
    """Demonstrate the Memory system functionality."""
    
    # Create a new memory instance
    print("=== Memory System Demo ===\n")
    memory = Memory()
    
    # Basic operations
    print("1. Basic Operations:")
    memory.set('username', 'john_doe')
    memory.set('email', 'john@example.com')
    memory.set('age', 30)
    print(f"   Stored username: {memory.get('username')}")
    print(f"   Stored email: {memory.get('email')}")
    print(f"   Stored age: {memory.get('age')}")
    print(f"   Memory size: {memory.size()}")
    print()
    
    # Using bracket notation
    print("2. Bracket Notation:")
    memory['score'] = 100
    print(f"   Score: {memory['score']}")
    print()
    
    # Checking existence
    print("3. Checking Key Existence:")
    print(f"   'username' exists: {'username' in memory}")
    print(f"   'password' exists: {'password' in memory}")
    print()
    
    # Storing complex data types
    print("4. Complex Data Types:")
    memory['settings'] = {
        'theme': 'dark',
        'notifications': True,
        'language': 'en'
    }
    memory['tags'] = ['python', 'memory', 'storage']
    print(f"   Settings: {memory['settings']}")
    print(f"   Tags: {memory['tags']}")
    print()
    
    # Getting all keys and values
    print("5. All Keys and Values:")
    print(f"   Keys: {memory.keys()}")
    print(f"   Number of items: {len(memory)}")
    print()
    
    # Statistics
    print("6. Memory Statistics:")
    stats = memory.get_stats()
    print(f"   Total items: {stats['total_items']}")
    print(f"   Total reads: {stats['total_reads']}")
    print(f"   Total writes: {stats['total_writes']}")
    print(f"   Total deletes: {stats['total_deletes']}")
    print()
    
    # Metadata
    print("7. Key Metadata:")
    metadata = memory.get_metadata('username')
    if metadata:
        print(f"   Created at: {metadata['created_at']}")
        print(f"   Updated at: {metadata['updated_at']}")
        print(f"   Access count: {metadata['access_count']}")
    print()
    
    # Deleting data
    print("8. Deleting Data:")
    memory.delete('age')
    print(f"   Deleted 'age'")
    print(f"   'age' exists: {'age' in memory}")
    print(f"   Memory size: {memory.size()}")
    print()
    
    # Using default values
    print("9. Default Values:")
    print(f"   Get 'missing' with default: {memory.get('missing', 'default_value')}")
    print()
    
    # Clear all data
    print("10. Clearing Memory:")
    print(f"   Size before clear: {memory.size()}")
    memory.clear()
    print(f"   Size after clear: {memory.size()}")
    print()
    
    # Representation
    memory['key1'] = 'value1'
    memory['key2'] = 'value2'
    print("11. Memory Representation:")
    print(f"   {repr(memory)}")


if __name__ == '__main__':
    main()
