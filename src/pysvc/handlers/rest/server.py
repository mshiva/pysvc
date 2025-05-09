"""Server setup and runner"""
from fastapi import FastAPI


def run():
    """Returns the ASGI compatible server app"""
    from pysvc.handlers.rest import healthz

    server = FastAPI()
    server.include_router(healthz.router)

    return server