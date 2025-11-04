import os
import google.generativeai as genai
from flask import Blueprint, request, jsonify

api_bp = Blueprint("api", __name__)

# Configure Google Gemini
GOOGLE_API_KEY = "AIzaSyBg70DVkQY5gflpcwcUM5-FdvdqgcKE1Ts"
if not GOOGLE_API_KEY:
    raise ValueError("Missing Google API key")

genai.configure(api_key=GOOGLE_API_KEY)

@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})

@api_bp.route("/ask", methods=["POST"])
def ask():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "Question is required"}), 400

    try:
        # Use gemini-1.5-flash (free and fast)
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=(
                "You are a helpful math tutor. "
                "Always reason step by step. "
                "First, explain your thinking clearly. "
                "Then, on the last line, output ONLY the final answer as: 'Answer: X'"
            )
        )

        # Safety settings to prevent blocking
        safety_settings = [
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        ]

        response = model.generate_content(
            question,
            safety_settings=safety_settings
        )

        # Handle empty or blocked responses
        if not response.text:
            return jsonify({"error": "AI returned empty response. Try rephrasing."}), 500

        return jsonify({"response": response.text.strip()}), 200

    except Exception as e:
        print("🔥 Gemini Error:", str(e))
        return jsonify({"error": "AI service failed. Check API key and Google Cloud setup."}), 500