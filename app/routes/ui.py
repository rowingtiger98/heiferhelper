from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

routes = APIRouter()

templates = Jinja2Templates(directory="templates")

@routes.get("/")
def click_counter(request: Request):
    with open("count.txt", "r") as file:
        count = file.read()
    return templates.TemplateResponse(
        request=request, name="counter.html", context={"count": count}
    )

@routes.get("/echo", response_class="HTMLResponse")
async def echo(request: Request, item: str="No echo!"):
    return templates.TemplateResponse(
        request=request, name="echo.html", context={"item":item}
    )

@routes.post("/add-cow", response_class="HTMLResponse")
async def add_cow(request: Request):
    with open("count.txt", "r") as read_file:
        file_content = read_file.read()
    with open("count.txt", "w") as write_file:
        write_file.write(f"{int(file_content) + 1}")
    with open("count.txt", "r") as updated_file:
        updated_file_content = updated_file.read()
    return templates.TemplateResponse(request=request, name="partials/count.html", context={"count": updated_file_content})



@routes.post("/reset-cow-count", response_class="HTMLResponse")
async def reset_cows(request: Request):
    with open("count.txt", "w") as file:
        file.write("0")
    with open("count.txt", "r") as updated_file:
        updated_file_content = updated_file.read()
    return templates.TemplateResponse(request=request, name="partials/count.html", context={"count": updated_file_content})

    