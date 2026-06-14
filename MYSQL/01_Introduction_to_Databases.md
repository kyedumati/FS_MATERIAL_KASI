# Introduction to Databases

## Concepts in Focus

- Data
- Database
- Database Management System (DBMS)
  - Advantages
- Types of Databases
  - Relational Database
  - Non-Relational Database

## Data

Any sort of information that is stored is called **data**.

**Examples:**

1. Messages & multimedia on WhatsApp
2. Products and orders on Amazon
3. Contact details in telephone directory, etc.

## Database

An organized collection of data is called a **database**.

## Database Management System (DBMS)

A software that is used to easily store and access data from the database in a secure way.

```
Web Application Servers  ──┐
AI Models                ──┼──► DBMS ◄──► Database
Recommendation Engines   ──┘
```

## Advantages

- **Security:** Data is stored & maintained securely.
- **Ease of Use:** Provides simpler ways to create & update data at the rate it is generated and updated respectively.
- **Durability and Availability:** Durable and provides access to all the clients at any point in time.
- **Performance:** Quickly accessible to all the clients (applications and stakeholders).

## Types of Databases

There are different types of databases based on how we organize the data:

| Type | Description |
|------|-------------|
| Relational | Data organized in tables |
| Analytical | Central data with branching structures |
| Key-Value | Key mapped to value pairs |
| Column Family | Column-oriented storage |
| Graph | Nodes and edges |
| Document | Hierarchical document structure |

## Relational Database

In relational databases, the data is organized in the form of **tables**.

## Tables, Rows, and Columns

A relational database stores data in **tables**. Understanding these three terms is essential before writing SQL.

| Term | Description | Example (player table) |
|------|-------------|------------------------|
| **Table** | A collection of related data organized in rows and columns | `player` |
| **Column** | A vertical field that stores one type of data (attribute) | `name`, `age`, `score` |
| **Row** | A horizontal record representing one entry (tuple) | `('Virat', 32, 50)` |

```
player table
┌──────────┬─────┬───────┐
│ name     │ age │ score │  ← columns (attributes)
├──────────┼─────┼───────┤
│ Virat    │ 32  │ 50    │  ← row 1
│ Rakesh   │ 39  │ 35    │  ← row 2
│ Sai      │ 47  │ 38    │  ← row 3
└──────────┴─────┴───────┘
```

## DBMS vs RDBMS

| | DBMS | RDBMS |
|---|------|-------|
| **Full form** | Database Management System | Relational Database Management System |
| **Data format** | Files, objects, documents, graphs, etc. | Tables with rows and columns |
| **Relationships** | Limited or no formal relationships | Enforces relationships via keys |
| **SQL support** | May or may not support SQL | Uses SQL as the standard language |
| **Examples** | MongoDB, Redis, Cassandra | MySQL, PostgreSQL, Oracle, SQL Server |

**Note:** All RDBMS are DBMS, but not all DBMS are RDBMS. This course focuses on **RDBMS using MySQL**.

## Non-Relational Database

Graph, Key-Value, Column Family, and Document — these four types are commonly referred to as **non-relational databases**.

**Note:**

- Choice of database depends on our requirements.
- Relational database is the most commonly used database.

## Relational DBMS

A Relational DBMS is a DBMS designed specifically for relational databases. Relational databases organize the data in the form of tables.

**Examples:** MySQL, Oracle, PostgreSQL, SQLite, SQL Server, IBM DB2, etc.

**Note:** This course uses **MySQL** as the primary RDBMS. See [MySQL Setup and Connection](00_MySQL_Setup_and_Connection.md) for installation.

## Non-Relational DBMS

A Non-Relational DBMS is a DBMS designed specifically for non-relational databases. Non-relational databases store the data in a "non-tabular form".

**Examples:** Elasticsearch, CouchDB, DynamoDB, MongoDB, Cassandra, Redis, etc.
