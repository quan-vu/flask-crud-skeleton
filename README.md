# Flask Skeleton

A simple Flask application for practice.

**Prerequisites**

1. Virtualenv
2. Python 3
2. Flask
3. MySQL Client

To works with MySQL in Python 3, we need to install the Python and MySQL development headers and libraries like so:

```
sudo apt-get install python-dev default-libmysqlclient-dev # Debian / Ubuntu
sudo yum install python-devel mysql-devel # Red Hat / CentOS
brew install mysql-connector-c # macOS (Homebrew) (Currently, it has bug. See below)
```

More here: https://pypi.org/project/mysqlclient/

Next, we will create virtual environtment with python3:

```shell
virtualenv -p python3 venv
source venv/bin/activate
```

Next, install Flask, Flask Sqlalchemy and MySQL client library w:

```
pip install flask flask-sqlalchemy mysqlclient
```

## Features

- [x] SQLAlchemy Database 
- [x] Models & Migration
- [x] Structuring project (Blueprints)
- [x] Authentication
- [x] Bootstrap
- [x] Templating
- [ ] Demo CRUD
- [ ] Deployment with Heroku
- [ ] CI/CD with Gitlab
- [ ] Travis test

## Database setup

Let create the MySQL database. Ensure you have MySQL installed and running, and then log in as the root user:

```
mysql -u root -p

mysql> CREATE USER 'flaskcrud_admin'@'localhost' IDENTIFIED BY 'flaskcrud';
Query OK, 0 rows affected (0.00 sec)

mysql> CREATE DATABASE flaskcrud_db;
Query OK, 1 row affected (0.00 sec)

mysql> GRANT ALL PRIVILEGES ON flaskcrud_db . - TO 'flaskcrud_admin'@'localhost';
Query OK, 0 rows affected (0.00 sec)
```

## Models & Migrations

To create migrations directory run: 

```
flask db init
```

To create migratons: 

```
flask db migrate
```

To apply migrations: 

```
flask db upgrade
```

## Run project

**Start flask app with python3 virtual environtment**

```shell
# Create virtual environtment with python3
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

**Start Flask app**

```shell
export FLASK_CONFIG=development
export FLASK_APP=run.py
flask run
```

## Reference:

- https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one

Enjoy :) !
