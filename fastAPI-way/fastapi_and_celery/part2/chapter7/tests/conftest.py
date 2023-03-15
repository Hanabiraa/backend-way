import os

import pytest

os.environ["FASTAPI_CONFIG"] = "testing"  # noqa

"""
When pytest runs, it will load tests/conftest.py first.
os.environ["FASTAPI_CONFIG"] = "testing" ensures that
TestingConfig is returned as project.config.settings.

The app fixture uses the create_app factory to generate a new FastAPI app.
"""

from pytest_factoryboy import register
from project.users.factories import UserFactory
from project.tdd.factories import MemberFactory

""" 
with pytest-factoryboy.register
Model fixture implements an instance of a model created by the factory. Name convention is model's lowercase-underscore class name.
"""
register(UserFactory)  # in our tests, we'll have access to a variable called !!! user !!! created by UserFactory automatically.
register(MemberFactory)  # in our tests, we'll have access to a variable called !!! member !!! created by UserFactory automatically.


@pytest.fixture
def settings():
    from project.config import settings as _settings

    return _settings


@pytest.fixture
def app(settings):
    from project import create_app

    app = create_app()
    return app


@pytest.fixture
def db_session(app):
    from project.database import Base, engine, SessionLocal

    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client(app):
    from fastapi.testclient import TestClient

    yield TestClient(app)


@pytest.fixture(autouse=True)
def tmp_upload_dir(tmpdir, settings):
    settings.UPLOADS_DEFAULT_DEST = tmpdir.mkdir("tmp")
