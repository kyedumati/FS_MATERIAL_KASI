from fastapi import FastAPI

app = FastAPI()


@app.get("/Health")
def health():
    return "ok"


@app.get("/")
def home():
    return {"message": "Hello World"}
