import pytest
from app import app as flask_app
from models.database import db
from utils.auth import create_access_token

@pytest.fixture
def app():
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })

    with flask_app.app_context():
        db.create_all()
        yield flask_app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header():
    def _gen_header(user_id):
        token = create_access_token(user_id)
        return {"Authorization": f"Bearer {token}"}
    return _gen_header
