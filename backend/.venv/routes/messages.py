from flask import Blueprint, jsonify, request
from db import get_db_connection
from datetime import datetime


messages_bp = Blueprint("messages", __name__)
                        
@messages_bp.route("/api/messages", methods=["GET"])
def get_messages():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM messages ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])

@messages_bp.route("/api/messages", methods=["POST"])
def post_message():
    data = request.get_json()
    content = data.get("content", "").strip()

    if not content:
        return jsonify({"error": "Content is required"}), 400
    
    timestamp = datetime.now().isoformat()
    conn = get_db_connection()
    conn.execute("INSERT INTO messages (content, timestamp) VALUES (?, ?)", (content, timestamp))
    conn.commit()
    conn.close()

    return jsonify({"status": "ok"}), 201