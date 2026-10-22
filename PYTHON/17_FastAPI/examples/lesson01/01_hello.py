from fastapi import FastAPI

app = FastAPI(title="AcmeHR")


@app.get("/")
def home():
    return {"message": "Welcome to AcmeHR"}
