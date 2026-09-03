# MySQL Setup and Connection

This course uses **MySQL 8+** as the primary database. You can interact with MySQL through the **command-line client (CLI)** or **MySQL Workbench** (GUI).

---

**Module Outcome:**

- Install MySQL 8+ and open it from CLI or Workbench with a password you actually remember
- Connect, run `SELECT 1`, and know the service is up
- Keep root credentials off GitHub and off the projector

## Installing MySQL

### Windows

1. Download **MySQL Installer** from [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)
2. Choose **MySQL Server** and **MySQL Workbench** during setup.
3. Set a **root password** during installation and note it down.
4. Complete the installer and start the MySQL service.

### macOS

```bash
brew install mysql
brew services start mysql
mysql_secure_installation
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation
```

**Verify installation:**

```bash
mysql --version
```

Expected output: `mysql  Ver 8.x.x`

---

## Installing MySQL Workbench

1. Download from [https://dev.mysql.com/downloads/workbench/](https://dev.mysql.com/downloads/workbench/)
2. Install and open MySQL Workbench.
3. Workbench provides a visual interface for writing queries, viewing schemas, and managing databases.

---

## Connecting via CLI

**Step 1:** Open terminal (macOS/Linux) or Command Prompt (Windows).

**Step 2:** Connect as root:

```bash
mysql -u root -p
```

Enter your root password when prompted.

**Step 3:** Create a database for practice:

```sql
CREATE DATABASE training_db;
USE training_db;
```

**Step 4:** Verify connection:

```sql
SELECT DATABASE();
SHOW TABLES;
```

**Step 5 (before querying homework):** Load sample tables from [`labs/training_db_seed.sql`](labs/training_db_seed.sql). Module 02 still has you `CREATE` `player` yourself. How to run the script: [`labs/README.md`](labs/README.md).

**Common CLI commands:**

| Command | Description |
|---------|-------------|
| `mysql -u root -p` | Connect as root |
| `mysql -u username -p -h hostname` | Connect to remote server |
| `exit` or `quit` | Disconnect from MySQL |
| `SHOW DATABASES;` | List all databases |
| `USE database_name;` | Switch to a database |

---

## Connecting via MySQL Workbench

**Step 1:** Open MySQL Workbench.

**Step 2:** Click **+** next to "MySQL Connections" to add a new connection.

**Step 3:** Configure:

| Field | Value |
|-------|-------|
| Connection Name | Local MySQL |
| Hostname | `127.0.0.1` or `localhost` |
| Port | `3306` |
| Username | `root` |

**Step 4:** Click **Test Connection** → enter password → **OK**.

**Step 5:** Double-click the connection to open. Use the SQL editor tab to run queries.

**Step 6:** Select your database:

```sql
USE training_db;
```

---

## Useful MySQL Commands (Both CLI and Workbench)

```sql
-- Show current database
SELECT DATABASE();

-- Show all tables in current database
SHOW TABLES;

-- Describe table structure
DESCRIBE player;
-- or
SHOW COLUMNS FROM player;

-- Show MySQL version
SELECT VERSION();
```

---

## Creating a Practice User (Optional)

For training environments, create a dedicated user instead of using root:

```sql
CREATE USER 'trainee'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON training_db.* TO 'trainee'@'localhost';
FLUSH PRIVILEGES;
```

Connect as the new user:

```bash
mysql -u trainee -p training_db
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `Access denied for user` | Check username/password; verify user has privileges |
| `Can't connect to MySQL server` | Ensure MySQL service is running (`brew services start mysql` or Windows Services) |
| `Unknown database` | Run `CREATE DATABASE training_db;` first |
| Port 3306 in use | Check if another MySQL instance is running |

**Note:** All SQL examples in this course assume you are connected to MySQL 8+ and have run `USE training_db;` (or your project database) before executing queries.

**What next:** [MYSQL README](README.md) — two teaching tracks, homework, and the seed lab.
