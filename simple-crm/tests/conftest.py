"""
Test configuration and fixtures.
"""
import os
import pytest
from app.main import create_app
from app.models import db as database, Lead

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app('testing')
    
    # Create a test database
    with app.app_context():
        database.create_all()
        
        # Add test data
        test_leads = [
            Lead(title="Test Lead 1", amount=1000.00),
            Lead(title="Test Lead 2", amount=2000.00)
        ]
        database.session.add_all(test_leads)
        database.session.commit()
    
    yield app
    
    # Clean up
    with app.app_context():
        database.session.remove()
        database.drop_all()

@pytest.fixture
def client(app):
    """Test client for the Flask app."""
    return app.test_client()

@pytest.fixture
def runner(app):
    """Test CLI runner for the Flask app."""
    return app.test_cli_runner()