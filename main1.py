from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get():
    return {"message": "Hi!! My Name is Sundari"}

@app.get("/view")
def view():
    students = [
        {
            "id": 1,
            "name": "Sundari",
            "age": 7,
            "course": "BSc CS"
        },
        {
            "id": 2,
            "name": "Anjali",
            "age": 20,
            "course": "BSc DS"
        }
    ]

    return students