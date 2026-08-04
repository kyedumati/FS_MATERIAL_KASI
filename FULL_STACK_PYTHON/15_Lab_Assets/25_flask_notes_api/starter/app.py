"""STARTER Flask notes API."""
from flask import Flask, jsonify, request

app = Flask(__name__)
notes = [{"id": 1, "text": "Buy milk"}]


@app.get("/api/notes")
def list_notes():
    # TODO
    raise NotImplementedError


@app.post("/api/notes")
def add_note():
    # TODO: read JSON body {"text": "..."}
    raise NotImplementedError


if __name__ == "__main__":
    app.run(debug=True)
