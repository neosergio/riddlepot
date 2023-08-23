from fastapi import FastAPI
from adapters.api.routers import event_router
from config.settings import settings


app = FastAPI()

# Include API routers
app.include_router(event_router.router, prefix=settings.API_PREFIX + "/events", tags=["events"])


if __name__ == "__main__":
    import uvicorn

    # Use uvicorn to run the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000)
