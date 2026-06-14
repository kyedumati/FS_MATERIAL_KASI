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

## Non-Relational Database

Graph, Key-Value, Column Family, and Document — these four types are commonly referred to as **non-relational databases**.

**Note:**

- Choice of database depends on our requirements.
- Relational database is the most commonly used database.

## Relational DBMS

A Relational DBMS is a DBMS designed specifically for relational databases. Relational databases organize the data in the form of tables.

**Examples:** Oracle, PostgreSQL, MySQL, SQLite, SQL Server, IBM DB2, etc.

## Non-Relational DBMS

A Non-Relational DBMS is a DBMS designed specifically for non-relational databases. Non-relational databases store the data in a "non-tabular form".

**Examples:** Elasticsearch, CouchDB, DynamoDB, MongoDB, Cassandra, Redis, etc.
