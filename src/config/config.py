import os

# export DB_HOST="localhost"
# export DB_USER="studentsuser"
# export DB_PASSWORD="studentspassword"
# export DB_DATABASE="students"

DB_CONFIG = {
    'host': os.environ["DB_HOST"],
    'user': os.environ["DB_USER"],
    'password': os.environ["DB_PASSWORD"],
    'database': os.environ["DB_DATABASE"]
}
