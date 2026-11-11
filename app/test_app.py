from app import app

def test_home():
    resp = app.test_client().get("/")
    assert resp.status_code == 200

def test_health():
    resp = app.test_client().get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}
