from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def ping_request():
    return {"message": "pong"}
