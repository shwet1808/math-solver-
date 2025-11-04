# File: backend/app.py

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables first
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "dev-fallback-key")

    # ✅ Allow React (Vite) on http://localhost:5173
    CORS(app, origins=["http://localhost:5173"])

    # Register API routes
    from api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)