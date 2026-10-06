

-----------------
Architecture:
Python
  ↓
List / Dictionary
  ↓
JSON file
------------------

You learn:
- json.load()
- json.dump()
- File persistence
- Serialization/deserialization
- Reading/writing structured data

Pros
- Very easy
- No database installation
- Human-readable
- Good for small projects
- Easy to backup

Cons
- ❌ Poor for large amounts of data
- ❌ No SQL queries
- ❌ No proper relationships
- ❌ Entire file can become cumbersome to manage
- ❌ Concurrent users can cause problems
- ❌ No database constraints

Use it for: small CLI tools, configuration, prototypes, simple data storage.