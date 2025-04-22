import pytest

from fastapi.testclient import TestClient
from pysvc.handlers.rest import server

@pytest.fixture(scope="package")
def test_client():
    client = TestClient(server.run())
    return client