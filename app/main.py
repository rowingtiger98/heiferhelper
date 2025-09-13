import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


from app.routes import health
from app.routes import examples
from app.routes import ui

app = FastAPI(title="Simple FastAPI Application")
app.include_router(health.routes)
app.include_router(examples.routes)
app.include_router(ui.routes)
app.mount("/static", StaticFiles(directory="static"), name="static")



if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=8080)
