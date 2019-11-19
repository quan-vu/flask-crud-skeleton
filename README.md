# Demo Restful API using Flask, Flask-RESTPlus and Swagger UI

Flask enables exposure of Python functions as APIs. Flask-RESTPlus is an extension to Flask which allows we define the Restful API with the Swagger UI is integrated for all the APIs.

In this demo, we will develope a Flask application with several APIs and dummy data.

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

## TODO

- [x] Database Setup
- [x] Models
- [x] Migration
- [x] Blueprints
- [x] Home page
- [x] Authentication
- [ ] Conclusion

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

## Reference

- https://flask-login.readthedocs.io/en/latest/









## Test the application

Start flask app with virtualenv

```shell
# Create virtual environtment with python3
virtualenv -p python3 venv
source venv/bin/activate

# Run flask app
FLASK_APP=app.py flask run
```

Try to test it with Swagger UI here:

http://127.0.0.1:5000/