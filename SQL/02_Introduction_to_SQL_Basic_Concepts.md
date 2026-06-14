# Introduction to SQL (Basic Concepts)

## Introduction to SQL [Basics]

- SQL stands for **Structured Query Language**.
- SQL is used to perform operations on Relational DBMS.
- SQL is declarative. Hence, easy to learn.
- SQL provides multiple clauses (commands) to perform various operations like create, retrieve, update and delete the data.

## Creating Tables

**Create Table** — Creates a new table in the database.

**Syntax:**

```sql
CREATE TABLE table_name (
    column1 type1,
    column2 type2,
    ....
);
```

Here, `type1` and `type2` in the syntax are the datatypes of `column1` and `column2` respectively.

**Example:** Create a player table to store the following details of players.

| column_name | data_type |
|-------------|-----------|
| name | VARCHAR(200) |
| age | INT / INTEGER |
| score | INT / INTEGER |

```sql
CREATE TABLE player(
    name VARCHAR(200),
    age INTEGER,
    score INTEGER
);
```

We can check the details of the created table at any point in time using the **PRAGMA** command.

## Data Types

| Datatype | Syntax |
|----------|--------|
| Integer | INT/INTEGER |
| Float | FLOAT |
| String | VARCHAR |
| Text | TEXT |
| Date | DATE |
| Time | TIME |
| Datetime | DATETIME |
| Boolean | BOOLEAN |

**Note:**

1. Boolean values are stored as integers 0 (FALSE) and 1 (TRUE)
2. Date object is represented as: `'YYYY-MM-DD'`
3. Datetime object is represented as: `'YYYY-MM-DD HH:MM:SS'`

## PRAGMA

`PRAGMA TABLE_INFO` command returns the information about a specific table in a database.

**Syntax:**

```sql
PRAGMA TABLE_INFO(table_name);
```

**Example:**

```sql
PRAGMA TABLE_INFO(employee);
```

**Note:** If the given table name does not exist, PRAGMA TABLE_INFO doesn't give any result.

## Inserting Rows

`INSERT` clause is used to insert new rows in a table.

**Syntax:**

```sql
INSERT INTO
    table_name (column1, column2, ..., columnN)
VALUES
    (value1, value2, ..., valueN),
    (value1, value2, ..., valueN);
```

Any number of rows from 1 to n can be inserted into a specific table using the above syntax.

**Example:** Insert name, age and score of 2 players in the player table.

```sql
INSERT INTO
    player (name, age, score)
VALUES
    ("Rakesh", 39, 35),
    ("Sai", 47, 38);
```

Upon executing the above code, both the entries would be added to the player table.

```sql
SELECT *
FROM player;
```

**Output:**

| name | age | score |
|------|-----|-------|
| Rakesh | 39 | 35 |
| Sai | 47 | 38 |

## Possible Mistakes

**Mistake 1:** The number of values that we're inserting must match with the number of column names that are specified in the query.

```sql
INSERT INTO
    player (name, age, score)
VALUES
    ("Virat", 31);
```

**Output:** Error: 2 values for 3 columns

**Mistake 2:** We have to specify only the existing tables in the database.

```sql
INSERT INTO
    player_Information (name, age, score)
VALUES
    ("Virat", 31, 38);
```

**Output:** Error: no such table: player_Information

**Mistake 3:** Do not add additional parenthesis `()` post VALUES keyword in the code.

```sql
INSERT INTO
    player (name, age, score)
VALUES
    (("Rakesh", 39, 35), ("Sai", 39, 40));
```

**Output:** Error: 2 values for 3 columns

**Mistake 4:** While inserting data, be careful with the datatypes of the input values. Input value datatype should be same as the column datatype.

```sql
INSERT INTO
    player(name, age, score)
VALUES
    ("Virat", 30, "Hundred");
```

**WARNING:** If the datatype of the input value doesn't match with the datatype of column, SQLite doesn't raise an error.

## Retrieving Data

`SELECT` clause is used to retrieve rows from a table.

The database consists of a **player** table that stores the details of players who are a part of a tournament. The player table stores the name, age and score of players.

## Selecting Specific Columns

To retrieve the data of only specific columns from a table, add the respective column names in the SELECT clause.

**Syntax:**

```sql
SELECT
    Column1,
    Column2,
    ....
    columnN
FROM
    table_name;
```

**Example:** Fetch the name and age of the players from the player table.

```sql
SELECT
    name,
    age
FROM
    player;
```

**Output:**

| name | age |
|------|-----|
| Virat | 32 |
| Rakesh | 39 |
| Sai | 47 |
| ... | ... |

## Selecting All Columns

Sometimes, we may want to select all the columns from a table. Typing out every column name, for every time we have to retrieve the data, would be a pain.

**Syntax:**

```sql
SELECT *
FROM table_name;
```

**Example:** Get all the data of players from the player table.

```sql
SELECT *
FROM player;
```

**Output:**

| name | age | score |
|------|-----|-------|
| Virat | 32 | 50 |
| Rakesh | 39 | 35 |
| Sai | 47 | 30 |
| ... | ... | ... |

## Selecting Specific Rows

We use `WHERE` clause to retrieve only specific rows.

**Syntax:**

```sql
SELECT *
FROM table_name
WHERE condition;
```

**Note:** WHERE clause specifies a condition that has to be satisfied for retrieving the data from a database.

**Example:** Get name and age of the player whose name is 'Ram' from the player table.

```sql
SELECT *
FROM player
WHERE name = "Sai";
```

**Output:**

| name | age | score |
|------|-----|-------|
| Sai | 47 | 30 |

## Update Rows

`UPDATE` clause is used to update the data of an existing table in database. We can update all the rows or only specific rows as per the requirement.

## Update All Rows

**Syntax:**

```sql
UPDATE
    table_name
SET
    column1 = value1;
```

**Example:**

```sql
UPDATE
    player
SET
    score = 100;
```

## Update Specific Rows

**Syntax:**

```sql
UPDATE
    table_name
SET
    column1 = value1
WHERE
    column2 = value2;
```

**Example:**

```sql
UPDATE
    player
SET
    score = 150
WHERE
    name = 'Ram';
```

## Delete Rows

`DELETE` clause is used to delete existing records from a table.

## Delete All Rows

**Syntax:**

```sql
DELETE FROM
    table_name;
```

**Example:** Delete all the rows from player table.

```sql
DELETE FROM
    player;
```

## Delete Specific Rows

**Syntax:**

```sql
DELETE FROM
    table_name
WHERE
    column1 = value1;
```

**Example:** Delete 'shyam' from the player table.

**Note:** We can uniquely identify a player by name.

```sql
DELETE FROM
    player
WHERE
    name = "shyam";
```

**Warning:** We cannot retrieve the data once we delete the data from the table.

## DROP Table

`DROP` clause is used to delete a table from the database.

**Syntax:**

```sql
DROP TABLE
    table_name;
```

**Example:**

```sql
DROP TABLE player;
```

## Alter Tables

`ALTER` clause is used to add, delete, or modify columns in an existing table.

## Add Column

**Syntax:**

```sql
ALTER TABLE
    table_name
ADD
    column_name datatype;
```

**Example:** Add a new column `jersey_num` of type integer to the player table.

```sql
ALTER TABLE
    player
ADD
    jersey_num INT;
```

**Note:** Default values for newly added columns in the existing rows will be NULL.

## Rename Column

**Syntax:**

```sql
ALTER TABLE
    table_name RENAME COLUMN C1 TO C2;
```

**Example:** Rename the column `jersey_num` in the player table to `jersey_number`.

```sql
ALTER TABLE
    player RENAME COLUMN jersey_num TO jersey_number;
```

## Drop Column

**Syntax:**

```sql
ALTER TABLE
    table_name DROP COLUMN column_name;
```

**Example:**

```sql
ALTER TABLE
    player DROP COLUMN jersey_number;
```

**Note:** DROP COLUMN is not supported in some DBMS, including SQLite.
