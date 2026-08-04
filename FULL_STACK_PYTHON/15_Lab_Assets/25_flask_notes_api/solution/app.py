from flask import Flask, jsonify, request

app = Flask(__name__)
notes = [{"id": 1, "text": "Buy milk"}]
_next = 2


@app.get("/api/notes")
def list_notes():
    return jsonify(notes)


@app.post("/api/notes")
def add_note():
    global _next
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"error": "text required"}), 400
    note = {"id": _next, "text": text}
    _next += 1
    notes.append(note)
    return jsonify(note), 201


if __name__ == "__main__":
    app.run(debug=True)
