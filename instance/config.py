# instance/config.py
import os

SECRET_KEY = '#%^^p9Bv9%$i01'
# Use local database
# SQLALCHEMY_DATABASE_URI = 'mysql://flaskcrud_admin:flaskcrud@localhost/flaskcrud_db'

# Use free cloud Postgres for demo
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
