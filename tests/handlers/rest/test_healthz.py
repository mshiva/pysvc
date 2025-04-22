from .conftest import test_client

def test_liveness_check(test_client):
    resp = test_client.get("/healthz/live")
    assert resp.status_code == 200
