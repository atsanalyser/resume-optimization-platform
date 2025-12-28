from fastapi import FastAPI
from app.api.parser import router as parser_router

app = FastAPI(title="Resume Optimization Platform")


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(parser_router)
