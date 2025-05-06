from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API для курсовой работы УиАИС"}

@app.get("/health")
def health_check():
    return {"status": "OK", "service": "Zavtur API"}
