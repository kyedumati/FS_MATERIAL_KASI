from flask import Flask, jsonify, request

app = Flask(__name__)
notes = []

@app.get("/api/notes")
def list_notes():
    return notes  # Bug: must jsonify

@app.post("/api/notes")
def add_note():
    text = request.json["text"]  # Bug: crashes if no JSON
    notes.append(text)  # Bug: not an object with id
    return {"ok": True}, 201  # Bug: not jsonify / wrong type sometimes
