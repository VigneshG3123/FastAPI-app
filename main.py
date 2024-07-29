from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # Ensure the path argument is specified
def read_root():
    return {"Hello": "World"}
