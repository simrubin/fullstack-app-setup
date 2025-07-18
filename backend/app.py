# save this as app.py
from flask import Flask, app
import json
import yaml
from db import init_db
from routes.messages import messages_bp
from flask_cors import CORS
import os

#Load config from YAML file
config = yaml.safe_load(open("config.yaml", "r"))
python_config = config["python_service"]


def init_app():
    app = Flask(__name__)
    allowed_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
    CORS(app, origins=[allowed_origin]) # Allow CORS from frontend origin
    
    # Initialize database
    init_db()
    print("[INFO] Database initialized at db/app.db")

    # Register routes
    app.register_blueprint(messages_bp)

    @app.route("/")
    def home():
        return json.dumps({"message": "Flask app is running!", "endpoints": ["/api/hello", "/api/healthcheck"]})

    @app.route("/api/hello")
    def hello():
        return json.dumps({"message":"Hello, World!"})

    @app.route("/api/healthcheck")
    def healthcheck():
        if not config or not python_config:  #rest of global variables are not set:
            return json.dumps({"status": "ERROR", "message": "Configuration not set"}), 500
        return json.dumps({"status": "OK"}), 200

    return app

if __name__ == "__main__":
    print(f"Starting Flask app on 0.0.0.0:{python_config['port']}")
    print("Available endpoints:")
    print(f"- http://0.0.0.0:{python_config['port']}/")
    print(f"- http://0.0.0.0:{python_config['port']}/api/hello")
    print(f"- http://0.0.0.0:{python_config['port']}/api/healthcheck")
    # Force bind to 0.0.0.0 for Docker containers
    app = init_app()
    app.run(host=python_config["host"], port=python_config["port"], debug=True)