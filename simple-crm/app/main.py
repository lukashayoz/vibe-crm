import os
from flask import Flask, render_template
from flask_migrate import Migrate
from app.models import db, Lead
from app.seed import run_seed
from app.config import config

def create_app(config_name="default"):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Register routes
    @app.route('/')
    def index():
        """
        Endpoint for the home page.
        
        Returns:
            Rendered HTML template for the home page.
        """
        return render_template('index.html')
    
    @app.route('/leads')
    def leads():
        """
        Endpoint to display all leads.
        
        Returns:
            Rendered HTML template with all leads.
        """
        all_leads = Lead.query.order_by(Lead.created_at.desc()).all()
        return render_template('leads.html', leads=all_leads)
    
    # Initialize the database
    with app.app_context():
        db.create_all()
        
        # Check if we need to seed the database
        if config_name == "development" and Lead.query.count() == 0:
            run_seed()
    
    return app

if __name__ == '__main__':
    env = os.getenv('FLASK_ENV', 'development')
    app = create_app(env)
    app.run(host='0.0.0.0', port=5000)
