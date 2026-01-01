from flask import Flask, jsonify, render_template
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    """
    Serve the HTML dashboard
    """
    return render_template('index.html')

@app.route("/api/health", methods=["GET"])
def health_check():
    """
    Basic health endpoint for container validation
    """
    return jsonify({
        "status": "ok",
        "service": "DevOps Demo Application",
        "hostname": socket.gethostname(),
        "environment": os.getenv("ENV", "production"),
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route("/api/version", methods=["GET"])
def version():
    """
    Application version endpoint
    """
    return jsonify({
        "version": os.getenv("APP_VERSION", "1.0.0"),
        "build": os.getenv("BUILD_NUMBER", "latest")
    }), 200

@app.route("/api/info", methods=["GET"])
def info():
    """
    System information endpoint
    """
    return jsonify({
        "hostname": socket.gethostname(),
        "platform": "Kubernetes on AWS EKS",
        "region": "eu-west-1",
        "deployed_by": "GitHub Actions CI/CD",
        "container_registry": "GitHub Container Registry"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
