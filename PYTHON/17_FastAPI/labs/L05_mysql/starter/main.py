from fastapi import FastAPI

app = FastAPI(title="AcmeHR")


@app.get("/")
def home():
    return {"message": "Welcome to AcmeHR"}


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO: DATABASE_URL for trainee on localhost, database training_db.
# TODO: Employee table class matching the CREATE TABLE in Lesson 5.
# TODO: On startup, create the table and insert the six employees when it is empty.
# TODO: GET /employees and GET /employees/{employee_id} read that table.
# Unknown id returns 404.
