import os
from flask import Flask, request, jsonify
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client()

COLLECTION = os.getenv("COLLECTION_NAME", "items")
API_TOKEN = os.getenv("API_TOKEN", "")

@app.get("/")
def home():
    return jsonify({
        "status": "ok",
        "service": "cloudrun-firestore-demo",
        "secret_loaded": bool(API_TOKEN)
    })

@app.post("/items")
def create_item():
    data = request.get_json(force=True) or {}
    name = data.get("name", "Unnamed")
    doc_ref = db.collection(COLLECTION).document()
    doc_ref.set({"name": name})
    return jsonify({"id": doc_ref.id, "name": name}), 201

@app.get("/items")
def list_items():
    docs = db.collection(COLLECTION).stream()
    items = [{"id": d.id, **d.to_dict()} for d in docs]
    return jsonify(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8080")))
