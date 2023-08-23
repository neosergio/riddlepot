from fastapi import FastAPI


app = FastAPI()


if __name__ == "__main__":
    import uvicorn

    # Use uvicorn to run the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000)
