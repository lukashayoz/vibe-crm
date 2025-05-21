"""
Test routes and views.
"""
def test_index(client):
    """Test the home page route."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to Simple CRM" in response.data

def test_leads_route(client):
    """Test the leads route."""
    response = client.get('/leads')
    assert response.status_code == 200
    assert b"Leads" in response.data
    assert b"Test Lead 1" in response.data
    assert b"Test Lead 2" in response.data
    assert b"$1000" in response.data