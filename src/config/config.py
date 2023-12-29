import os

# export MYSQL_HOST="localhost"
# export MYSQL_USER="studentsuser"
# export MYSQL_PASSWORD="studentspassword"
# export MYSQL_DATABASE="students"

DB_CONFIG = {
    'host': os.environ["MYSQL_HOST"],
    'user': os.environ["MYSQL_USER"],
    'password': os.environ["MYSQL_PASSWORD"],
    'database': os.environ["MYSQL_DATABASE"]
}

DB_CONFIG_TEST = {
    'host': 'localhost',
    'user': 'studentsuser',
    'password': 'studentspassword',
    'database': 'students'
}
