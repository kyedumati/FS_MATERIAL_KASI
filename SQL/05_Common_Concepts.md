# Common Concepts

## SQL Expressions

We can write **expressions** in various SQL clauses. Expressions can comprise of various data types like integers, floats, strings, datetime etc.

## Using Expressions in SELECT Clause

**Example:** Get profits of all movies. (Consider profit as difference between collection and budget.)

```sql
SELECT
    id, name, (collection_in_cr - budget_in_cr) AS profit
FROM
    movie;
```

**Output:**

| id | name | profit |
|----|------|--------|
| 1 | The matrix | 40.31 |
| 2 | Inception | 67.68 |
| 3 | The Dark knight | 82.5 |
| ... | ... | ... |

**Note:** We use `||` operator to concatenate strings in sqlite3.

**Example 2:** Get the movie name and genre in the following format: movie_name - genre.

```sql
SELECT
    name || " - " || genre AS movie_genre
FROM
    movie;
```

**Output:**

| movie_genre |
|-------------|
| The Matrix - Sci-fi |
| Inception - Action |
| The Dark knight - Drama |
| Toy Story 3 - Animation |
| ... |

## Using Expressions in WHERE Clause

**Example:** Get all the movies with a profit at least 50 crores.

```sql
SELECT
    *
FROM
    movie
WHERE
    (collection_in_cr - budget_in_cr) >= 50;
```

**Output:**

| id | name | genre | budget_in_cr | collection_in_cr | rating | release |
|----|------|-------|--------------|------------------|--------|---------|
| 2 | Inception | Action | 16.0 | 83.68 | 8.8 | 2010-07-14 |
| 3 | The dark knight | Action | 18.0 | 100.5 | 9.0 | 2008-07-16 |
| 4 | Toy story 3 | Animation | 20.0 | 1006.7 | 8.5 | 2010-06-25 |
| ... | ... | ... | ... | ... | ... | ... |

## Using Expressions in UPDATE Clause

**Example:** Scale down rating from 10 to 5 in movie table.

```sql
UPDATE
    movie
SET
    rating = rating/2;
```

## Expressions in HAVING Clause

**Example:** Get all the genres with an average profit of at least 100 crores.

```sql
SELECT
    genre
FROM
    movie
GROUP BY
    genre
HAVING
    AVG(collection_in_cr - budget_in_cr) >= 100;
```

**Output:**

| genre |
|-------|
| Action |
| Animation |
| Mystery |
| ... |

## SQL Functions

SQL provides many built-in functions to perform various operations over data that is stored in tables. SQL functions can be divided into different categories such as:

1. Date functions
2. Cast functions
3. Arithmetic functions

## Date Functions

Date functions are used to extract the date or time from a datetime field. One important function in date functions is the `strftime()` function.

**strftime():** Used to extract year, month, day, hour, etc. from a date (or) datetime field based on a specific format as strings.

**Syntax:** `strftime(format, field_name)`

**Example:** `strftime("%Y", release_date)`

| Format | Description | Function |
|--------|-------------|----------|
| `%Y` | year | `strftime("%Y", field_name)` |
| `%m` | month | `strftime("%m", field_name)` |
| `%d` | day | `strftime("%d", field_name)` |
| `%H` | hour | `strftime("%H", field_name)` |

**How to use strftime():**

1. Choose the format of the datetime that you want, such as the year, the month, or the day, etc.
2. Write the function using `strftime(format, field_name)` in SQL query.

**Note:** `strftime()` extracts date and time in the string format.

**Example:** Get the movie title and year for every movie from the database.

```sql
SELECT
    name,
    strftime('%Y', release_date)
FROM
    movie;
```

**Output:**

| name | strftime('%Y', release_date) |
|------|------------------------------|
| the Matrix | 1999 |
| Inception | 2010 |
| the dark knight | 2008 |
| ... | ... |

## CAST Function

In database management systems, the `CAST` function is used to convert a value from one data type to another data type.

**Syntax:** `CAST(value AS data_type)`

**Example:** `CAST(strftime('%Y', release_date) AS integer)`

The CAST function takes:

1. **Value:** The value that you want to convert into a specific data type.
2. **Data type:** The data type to which you want to convert the value.

**Example 2:** Find how many movies were released in each month of the year 2010.

```sql
SELECT
    strftime("%m", release_date) AS month,
    COUNT(*) AS total_movies
FROM
    movie
WHERE
    CAST(strftime('%Y', release_date) AS integer) = 2010
GROUP BY
    month;
```

## Arithmetic Functions

Arithmetic functions in SQL are used to perform mathematical operations on numeric values. Some commonly used arithmetic functions are `FLOOR`, `CEIL`, `ROUND`.

**FLOOR function:** Rounds a number to the nearest integer, below its current value.

- Syntax: `FLOOR(number)`
- Example: `SELECT FLOOR(2.3);` → Output: 2

**CEIL function:** Rounds a number to the nearest integer above its current value.

- Syntax: `CEIL(number)`
- Example: `SELECT CEIL(-2.7);` → Output: -2

**ROUND function:** Rounds a number to a specified number of decimal places.

- Syntax: `ROUND(number, decimal_places)`
- Example: `SELECT ROUND(2.345, 2);` → Output: 2.35
- Example: `SELECT ROUND(2.345, 1);` → Output: 2.3

## String Functions

String functions in SQL are used to manipulate and operate on string values or character data.

| SQL Function | Behaviour |
|--------------|-----------|
| UPPER() | Converts a string to upper case |
| LOWER() | Converts a string to lowercase |

**Example:**

```sql
SELECT
    name
FROM
    movie
WHERE
    UPPER(name) LIKE UPPER("% avengers %");
```

**Output:**

| name |
|------|
| Avengers : Age of Ultron |
| Avengers : Endgame |

**Note:** Usually, UPPER() and LOWER() functions can help us to perform case-insensitive searches.

## SQL Set Operations

The SQL set operation is used to combine two or more SQL queries.

**Sets for understanding:**

- Cast in 'Sherlock Holmes' movie: Robert D Jr., Jude Law, Mark Strong
- Cast in 'Avengers Endgame' movie: Robert D Jr., Chris Evans, Mark Ruffalo

| Operator | Description | Result |
|----------|-------------|--------|
| INTERSECT | Actors who acted in both movies | Robert D Jr. |
| MINUS | Actors in Sherlock Holmes but not Avengers Endgame | Jude Law, Mark Strong |
| UNION | Unique actors in either movie | Jude Law, Mark Strong, Robert D Jr., Chris Evans, Mark Ruffalo |
| UNION ALL | Doesn't eliminate duplicate results | Jude Law, Mark Strong, Robert D Jr., Robert D Jr., Chris Evans, Mark Ruffalo |

**Syntax:**

```sql
SELECT
    C1, C2
FROM
    table_name_1
SET_OPERATOR
SELECT
    C1, C2
FROM
    table_name_2;
```

**Basic rules when combining two SQL queries using set operators:**

1. Each SELECT statement must have the same number of columns.
2. The columns must have similar data types.
3. The columns in each SELECT statement must be in the same order.

**Example:** Get ids of actors who acted in both Sherlock Holmes (id = 6) and Avengers Endgame (id = 15).

```sql
SELECT
    actor_id
FROM
    cast
WHERE
    movie_id = 6
INTERSECT
SELECT
    actor_id
FROM
    cast
WHERE
    movie_id = 15;
```

**Output:** actor_id = 6

## ORDER BY Clause in Set Operations

- ORDER BY clause can appear only once at the end of the query containing multiple SELECT statements.
- While using set operators, individual SELECT statements cannot have ORDER BY clause. Sorting can be done based on the columns that appear in the first SELECT query. It is recommended to sort using column positions.

**Example:**

```sql
SELECT actor_id FROM cast WHERE movie_id = 6
UNION
SELECT actor_id FROM cast WHERE movie_id = 15
ORDER BY 1 DESC;
```

## Pagination in Set Operations

Similar to ORDER BY clause, LIMIT and OFFSET clauses are used at the end of the list of queries.

**Example:** Get the first 5 ids of actors who acted in Sherlock Holmes (id=6) or Avengers Endgame (id=15). Sort ids in the descending order.

```sql
SELECT actor_id FROM cast WHERE movie_id = 6
UNION
SELECT actor_id FROM cast WHERE movie_id = 15
ORDER BY 1 DESC
LIMIT 5;
```
