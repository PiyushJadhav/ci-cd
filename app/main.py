from fastapi import FastPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Starlink"}