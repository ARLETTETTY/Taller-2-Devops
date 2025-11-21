from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Estudiar DevOps"},
        {"id": 2, "title": "Preparar certamen"},
        {"id": 3, "title": "Descansar 10 minutos"},
    ]
