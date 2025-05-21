"""
Seed script to populate the database with initial data.
"""
import random
from decimal import Decimal
from app.models import db, Lead

# Sample lead titles
LEAD_TITLES = [
    "Enterprise Software Solution",
    "Cloud Migration Project",
    "IT Infrastructure Upgrade",
    "Digital Transformation Initiative",
    "Mobile App Development",
    "E-commerce Platform",
    "Custom CRM Implementation",
    "Data Analytics Service",
    "Network Security Assessment",
    "Managed IT Services"
]

def seed_leads(count=5):
    """Seed the leads table with random data."""
    for _ in range(count):
        # Generate random title and amount
        title = random.choice(LEAD_TITLES)
        amount = Decimal(random.uniform(1000, 50000)).quantize(Decimal('0.01'))
        
        # Create new lead
        lead = Lead(title=title, amount=amount)
        db.session.add(lead)
    
    # Commit all changes
    db.session.commit()
    print(f"Successfully seeded {count} leads")


def run_seed():
    """Run seed functions."""
    seed_leads()

if __name__ == "__main__":
    run_seed()