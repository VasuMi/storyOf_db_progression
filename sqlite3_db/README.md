##Python + SQLite

This is where the current project has become much more interesting.

----------
Python
   ↓
SQLite
   ↓
expenses.db
-----------

SQLite is a real relational database.

You now have:
CREATE TABLE expenses (...)

and can use:
INSERT
SELECT
UPDATE
DELETE

What SQLite adds
You learn:
- Tables
- Rows
- Columns
- Primary keys
- SQL
- CRUD
- WHERE
- ORDER BY
- SUM()
- Database relationships
- Transactions
- Constraints

For your Expense Tracker:
expenses
---------------------------------
id
date
category
description
amount

Pros
- ✅ Built into Python
- ✅ No database server required
- ✅ Very easy to use
- ✅ Much better than JSON for structured data
- ✅ Supports SQL
- ✅ ACID transactions
- ✅ Very fast for small/local applications
- ✅ Database is just one .db file

Cons
- ❌ Not ideal for many simultaneous users
- ❌ Limited server/client architecture
- ❌ Less suitable for large production applications
- ❌ Advanced PostgreSQL features aren't available

Use it for:
- Desktop applications
- CLI applications
- Small applications
- Prototypes
- Learning SQL
- Local development