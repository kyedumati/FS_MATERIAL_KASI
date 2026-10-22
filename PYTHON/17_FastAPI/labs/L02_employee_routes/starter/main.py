from fastapi import FastAPI

app = FastAPI(title="AcmeHR")

employees = [
    {
        "employee_id": "E-1042",
        "name": "Ananya Rao",
        "designation": "Senior Software Engineer",
        "department": "Engineering",
    },
    {
        "employee_id": "E-1043",
        "name": "Karthik Menon",
        "designation": "Engineering Manager",
        "department": "Engineering",
    },
    {
        "employee_id": "E-1044",
        "name": "Meera Iyer",
        "designation": "Accountant",
        "department": "Finance",
    },
    {
        "employee_id": "E-1045",
        "name": "Rahul Sharma",
        "designation": "HR Executive",
        "department": "Human Resources",
    },
    {
        "employee_id": "E-1046",
        "name": "Fatima Khan",
        "designation": "Product Designer",
        "department": "Product",
    },
    {
        "employee_id": "E-1047",
        "name": "Arjun Reddy",
        "designation": "QA Engineer",
        "department": "Engineering",
    },
]


@app.get("/")
def home():
    return {"message": "Welcome to AcmeHR"}


@app.get("/health")
def health():
    return {"status": "ok"}


# TODO: GET /employees
# Query name is department. Missing query returns the whole list.
# Engineering returns Ananya, Karthik, and Arjun.


# TODO: GET /employees/{employee_id}
# Unknown id returns 404 and {"detail": "Employee not found"}.


# TODO: POST /employees with status 201
# Body is a dict. Missing employee_id or name returns 400.


# TODO: PUT /employees/{employee_id}
# Replaces the stored employee. The id in the path wins.


# TODO: PATCH /employees/{employee_id}
# Updates only the keys in the body. The id in the path stays.


# TODO: DELETE /employees/{employee_id} with status 204 and an empty body.
