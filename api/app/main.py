from fastapi import FastAPI

app = FastAPI(title="Registro de Mediciones")


@app.get("/health")
def health():
    return {"estado": "ok"}