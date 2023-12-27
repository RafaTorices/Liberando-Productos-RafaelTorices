"""
Module used for testing simple server module
"""

from fastapi.testclient import TestClient
import pytest
# Import mysql connector to connect to the database MySQL for testing
import mysql.connector

from application.app import app
from config.config import DB_CONFIG

client = TestClient(app)


class TestSimpleServer:
    """
    TestSimpleServer class for testing SimpleServer
    """
    @pytest.mark.asyncio
    async def read_health_test(self):
        """Tests the health check endpoint"""
        response = client.get("health")

        assert response.status_code == 200
        assert response.json() == {"health": "ok"}

    @pytest.mark.asyncio
    async def read_main_test(self):
        """Tests the main endpoint"""
        response = client.get("/")

        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}

    # Create a fixture for the database connection to use in the tests
    @pytest.fixture(scope="function")
    def db_connection(cls):
        connection = None
        try:
            # Config MySQL database connection for testing
            connection = mysql.connector.connect(**DB_CONFIG)
            yield connection
        finally:
            if connection:
                connection.close()

    @pytest.mark.asyncio
    async def create_student_test(self):
        """Tests the create_student endpoint function"""
        response = client.post("/create_student", json={"name": "Ana"})

        assert response.status_code == 200

    @pytest.mark.asyncio
    async def get_students_test(self):
        """Tests the get_students endpoint function"""
        response = client.get("/get_students")

        assert response.status_code == 200

    @pytest.mark.asyncio
    async def get_student_test(self):
        """Tests the get_student endpoint function"""
        response = client.get("/get_student?id=1")

        assert response.status_code == 200

    @pytest.mark.asyncio
    async def delete_student_test(self):
        """Tests the delete_student endpoint function"""
        response = client.delete("/delete_student?id=1")

        assert response.status_code == 200
