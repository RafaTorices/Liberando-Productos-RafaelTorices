import os

# export MYSQL_HOST="localhost"
# export MYSQL_USER="studentsuser"
# export MYSQL_PASSWORD="studentspassword"
# export MYSQL_DATABASE="students"

DB_DEFAULT_CONFIG = {
    "host": "localhost",
    "user": "studentsuser",
    "password": "studentspassword",
    "database": "students"
}

DB_CONFIG = {
    'host': os.getenv("MYSQL_HOST", DB_DEFAULT_CONFIG["host"]),
    'user': os.getenv("MYSQL_USER", DB_DEFAULT_CONFIG["user"]),
    'password': os.getenv("MYSQL_PASSWORD", DB_DEFAULT_CONFIG["password"]),
    'database': os.getenv("MYSQL_DATABASE", DB_DEFAULT_CONFIG["database"])
}
