import uvicorn
from fastapi import FastAPI


from app.routes import health
from app.routes import examples


app = FastAPI(title="Simple FastAPI Application")
app.include_router(health.routes)
app.include_router(examples.routes)


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080)
