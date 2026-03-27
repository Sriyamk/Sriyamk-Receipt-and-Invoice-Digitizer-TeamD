from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from FastAPI"}


@app.get("/assignment1/endpoint2/dashboard")
def dashboard():
    return "Hello Flask API!"


@app.post("/enpoint3/send")
def send_data(payload: dict):
    return {"received_payload": payload}


@app.get("/user/{username}")
def user(username):
    return {"user": username}
