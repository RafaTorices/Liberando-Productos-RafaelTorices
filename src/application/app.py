"""
Module define fastapi server configuration
"""

from fastapi import FastAPI, HTTPException
from hypercorn.asyncio import serve
from hypercorn.config import Config as HyperCornConfig
from prometheus_client import Counter
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

REQUESTS = Counter('server_requests_total',
                   'Total number of requests to this webserver')
HEALTHCHECK_REQUESTS = Counter(
    'healthcheck_requests_total', 'Total number of requests to healthcheck')
MAIN_ENDPOINT_REQUESTS = Counter(
    'main_requests_total', 'Total number of requests to main endpoint')

# Counter for register the number calls in webserver to the create_student endpoint
CREATE_STUDENT_ENDPOINT_REQUESTS = Counter(
    'create_student_requests_total', 'Total number of requests to create_student endpoint')
# Counter for register the number calls in webserver to the get_students endpoint
GET_STUDENTS_ENDPOINT_REQUESTS = Counter(
    'get_students_requests_total', 'Total number of requests to get_students endpoint')

dbconfig = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="students"
)


class Item(BaseModel):
    name: str


class SimpleServer:
    """
    SimpleServer class define FastAPI configuration and implemented endpoints
    """

    _hypercorn_config = None

    def __init__(self):
        self._hypercorn_config = HyperCornConfig()

    async def run_server(self):
        """Starts the server with the config parameters"""
        self._hypercorn_config.bind = ['0.0.0.0:8082']
        self._hypercorn_config.keep_alive_timeout = 90
        await serve(app, self._hypercorn_config)

    @app.get("/health")
    async def health_check():
        """Implement health check endpoint"""
        # Increment counter used for register total number calls in webserver
        REQUESTS.inc()
        # Increment counter used for register requests to healtcheck endpoint
        HEALTHCHECK_REQUESTS.inc()
        return {"health": "ok"}

    @app.get("/")
    async def read_main():
        """Implement main endpoint"""
        # Increment counter used for register the number calls in webserver
        REQUESTS.inc()
        # Increment counter used for register the number calls in main endpoint
        MAIN_ENDPOINT_REQUESTS.inc()
        return {"msg": "Hello World"}

    # Function for create_student endpoint to create new student in app
    @app.post("/create_student")
    async def create_student(item: Item):
        """Implement create_student endpoint"""
        # Increment counter used for register number calls to the endpoint create_student
        CREATE_STUDENT_ENDPOINT_REQUESTS.inc()
        try:
            mycursor = dbconfig.cursor()
            sql = "INSERT INTO students (name) VALUES (%s)"
            values = (item.name,)
            mycursor.execute(sql, values)
            dbconfig.commit()
            return {"msg": "OK!!"}
        except Exception as e:
            raise HTTPException(status_code=500, Detail=str(e))

    # Function for get_students endpoint to get all students in app

    @app.get("/get_students")
    async def get_students():
        """Implement get_students endpoint"""
        # Increment counter used for register the number calls in webserver to the endpoint get_students
        GET_STUDENTS_ENDPOINT_REQUESTS.inc()
        # Return the list of students
        try:
            mycursor = dbconfig.cursor()
            sql = "SELECT * FROM students"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            return myresult
        except Exception as e:
            raise HTTPException(status_code=500, Detail=str(e))
