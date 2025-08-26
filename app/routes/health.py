from fastapi import APIRouter

routes = APIRouter(tags=["API Status"])


@routes.get(
    "/",
    summary="API health check endpoint",
    description="Returns 200 status code with 'ok' if service is in a healthy state")
def get_api_status():
    return "OK"
