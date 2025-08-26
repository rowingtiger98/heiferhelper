from fastapi import APIRouter

routes = APIRouter(prefix="/examples", tags=["Example with a route prefix Status"])


@routes.get(
    "/moo",
    summary="Simple end point for POC",
    description="Returns 200 status code with a saying if service is in a healthy state")
def get_api_status():
    return "The cow says Mooooooooo..."
