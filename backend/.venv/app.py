# save this as app.py
from flask import Flask
import json
import yaml


#Load config from YAML file
config = yaml.safe_load(open("config.yaml", "r"))
python_config = config["python_service"]

app = Flask(__name__)

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

if __name__ == "__main__":
    print(f"Starting Flask app on 0.0.0.0:{python_config['port']}")
    print("Available endpoints:")
    print(f"- http://0.0.0.0:{python_config['port']}/")
    print(f"- http://0.0.0.0:{python_config['port']}/api/hello")
    print(f"- http://0.0.0.0:{python_config['port']}/api/healthcheck")
    # Force bind to 0.0.0.0 for Docker containers
    app.run(host="0.0.0.0", port=python_config["port"], debug=True)