"""
Test database models.
"""
from app.models import Lead

def test_lead_model(app):
    """Test Lead model creation and query."""
    with app.app_context():
        # Test that the test data was correctly inserted
        leads = Lead.query.all()
        assert len(leads) == 2
        
        # Test creating a new lead
        new_lead = Lead(title="New Test Lead", amount=3000.00)
        assert new_lead.title == "New Test Lead"
        assert new_lead.amount == 3000.00