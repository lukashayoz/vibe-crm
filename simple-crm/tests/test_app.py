import pytest
from simple_crm.app.main import create_app

@pytest.fixture
def app():
    app = create_app('testing') # Assuming you have a 'testing' config or will add one
    app.config.update({
        "TESTING": True,
        # Add other necessary testing configurations, e.g., a test database
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_home_page_status_code(client):
    """Test that the home page returns a 200 OK status."""
    response = client.get('/')
    assert response.status_code == 200

def test_home_page_content(client):
    """Test that the home page contains the 'Hello World' message."""
    response = client.get('/')
    assert b"Hello World" in response.data
