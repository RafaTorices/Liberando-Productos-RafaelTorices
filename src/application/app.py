"""
Module define fastapi server configuration
"""

from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config as HyperCornConfig
from prometheus_client import Counter
# Library used for get the form data from the request
from fastapi import Form

app = FastAPI()

REQUESTS = Counter('server_requests_total',
                   'Total number of requests to this webserver')
HEALTHCHECK_REQUESTS = Counter(
    'healthcheck_requests_total', 'Total number of requests to healthcheck')
MAIN_ENDPOINT_REQUESTS = Counter(
    'main_requests_total', 'Total number of requests to main endpoint')
# Counter for register the number calls in webserver to the post endpoint
POST_ENDPOINT_REQUESTS = Counter(
    'post_requests_total', 'Total number of requests to post endpoint')


class SimpleServer:
    """
    SimpleServer class define FastAPI configuration and implemented endpoints
    """

    _hypercorn_config = None

    def __init__(self):
        self._hypercorn_config = HyperCornConfig()

    async def run_server(self):
        """Starts the server with the config parameters"""
        self._hypercorn_config.bind = ['0.0.0.0:8081']
        self._hypercorn_config.keep_alive_timeout = 90
        await serve(app, self._hypercorn_config)

    @app.get("/health")
    async def health_check():
        """Implement health check endpoint"""
        #  Increment counter used for register total number calls in webserver
        REQUESTS.inc()
        # Increment counter used for register requests to healtcheck endpoint
        HEALTHCHECK_REQUESTS.inc()
        return {"health": "ok"}

    @app.get("/")
    async def read_main():
        """Implement main endpoint"""
        #  Increment counter used for register the number calls in webserver
        REQUESTS.inc()
        # Increment counter used for register the number calls in main endpoint
        MAIN_ENDPOINT_REQUESTS.inc()
        return {"msg": "Hello World"}

    # Function for submit endpoint to return name passed in the form
    @app.post("/submit")
    async def submit(name: str = Form(..., min_length=3)):
        """Implement submit form endpoint"""
        # If the name is less than 3 characters, return an error
        if len(name) < 3:
            return {"error": "Name should be at least 3 characters"}
        # Increment counter used for register number calls to the post endpoint
        POST_ENDPOINT_REQUESTS.inc()
        # Return the name passed in the form
        return {"msg": f"Hello, {name}!!"}
