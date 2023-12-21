"""
Module used for testing simple server module
"""

from fastapi.testclient import TestClient
import pytest
import mysql.connector

from application.app import app

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

    @pytest.fixture(scope="function")
    def db_connection(cls):
        # Establecer una conexión a la base de datos
        connection = None
        try:
            # Configuración de la base de datos de prueba
            db_config = {
                "host": "localhost",
                "user": "root",
                "password": "password",
                "database": "students",
            }
            # Crear la conexión
            connection = mysql.connector.connect(db_config)
            # Ejecutar las pruebas
            yield connection
        finally:
            # Cerrar la conexión después de las pruebas
            if connection:
                connection.close()

    @pytest.mark.asyncio
    async def create_student_test(self):
        """Tests the create_student endpoint function"""
        response = client.post("/create_student", json={"name": "Ana"})
        assert response.status_code == 200
        assert response.json() == {"msg": "OK!!"}

    @pytest.mark.asyncio
    async def get_students_test(self):
        """Tests the get_students endpoint function"""
        response = client.get("/get_students")
        assert response.status_code == 200
