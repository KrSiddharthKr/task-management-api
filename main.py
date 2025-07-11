from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/about")
def about_application():
    return {
        "project": "Task Management API",
        "version": "1.0.0",
        "description": "A backend API for managing tasks and projects"
    }