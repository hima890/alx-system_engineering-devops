
# MySQL Setup and Backup

This repository contains the configuration and setup for MySQL database servers, including replication and backup strategies.

## 0. Install MySQL

### Objective

Install MySQL version 5.7.x on both `web-01` and `web-02` servers.

### Instructions

- Ensure that the MySQL distribution is `5.7.x`.
- Confirm MySQL status using the command:

  ```bash
  mysql --version
  ```

### Example

```bash
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
```

## 1. Let Us In

### Objective

Create a database and table on the primary MySQL server (`web-01`) for replication.

### Instructions

- Create a database named `tyrell_corp`.
- Create a table named `nexus6` and add at least one entry.
- Ensure `holberton_user` has SELECT permissions.

### Example

```bash
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
```

## 2. Quite an Experience to Live in Fear

### Objective

Set up replication by creating a user on the primary MySQL server for the replica server.

### Instructions

- Create a user named `replica_user` with replication permissions.
- Check the replication privileges for `replica_user`.

### Example

```bash
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| replica_user     | Y               |
+------------------+-----------------+
```

## 3. Setup a Primary-Replica Infrastructure

### Objective

Configure MySQL replication between `web-01` (primary) and `web-02` (replica).

### Instructions

- Primary MySQL server on `web-01` (do not use `bind-address`).
- Replica MySQL server on `web-02`.
- Configure replication and verify using `show master status` on `web-01` and `show slave status` on `web-02`.

### Example

- **Primary (web-01):**

  ```bash
  mysql> show master status;
  +------------------+----------+--------------------+------------------+
  | File             | Position | Binlog_Do_DB       | Binlog_Ignore_DB |
  +------------------+----------+--------------------+------------------+
  | mysql-bin.000009 |      107 | tyrell_corp        |                  |
  +------------------+----------+--------------------+------------------+
  ```

- **Replica (web-02):**

  ```bash
  mysql> show slave status\G
  ...
  Slave_IO_Running: Yes
  Slave_SQL_Running: Yes
  ...
  ```

## 4. MySQL Backup

### Objective

Create a Bash script to generate a MySQL dump and compress it into a tar.gz archive.

### Script Features

- Dumps all MySQL databases to `backup.sql`.
- Compresses `backup.sql` into a tar.gz archive named `day-month-year.tar.gz`.
- Accepts MySQL root password as an argument.

### Example

```bash
ubuntu@03-web-01:~$ ./5-mysql_backup mydummypassword
backup.sql
ubuntu@03-web-01:~$ ls
01-03-2017.tar.gz  5-mysql_backup  backup.sql
ubuntu@03-web-01:~$ file 01-03-2017.tar.gz
01-03-2017.tar.gz: gzip compressed data
```

### Files

- `4-mysql_configuration_primary`: MySQL configuration for primary server.
- `4-mysql_configuration_replica`: MySQL configuration for replica server.
- `5-mysql_backup`: Bash script for MySQL backup.

## GitHub Repository

- **Repository:** [alx-system_engineering-devops](https://github.com/hima890/alx-system_engineering-devops)
- **Directory:** `0x14-mysql`
