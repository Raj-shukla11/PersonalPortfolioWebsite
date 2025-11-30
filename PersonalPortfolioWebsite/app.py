import os
import logging
from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-change-in-production")
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Register blueprints
from blueprints.main import main_bp
from blueprints.contact import contact_bp

app.register_blueprint(main_bp)
app.register_blueprint(contact_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
