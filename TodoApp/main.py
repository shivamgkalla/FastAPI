from fastapi import FastAPI, status
from starlette.requests import Request
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="TodoApp/static"), name="static")


# CORS #

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def test(request: Request):
    return RedirectResponse(url="/todos/todo-page", status_code=status.HTTP_302_FOUND)

@app.get("/health")
def health_check():
    return {'status': 'Healthy'}


# Docker test #

@app.get("/docker-test")
def docker_test():
    return {'status': 'Docker test successfully passed.'}


# CI/CD Test #

@app.get("/ci-cd")
def ci_cd_test():
    return {"status": "CI/CD is Live"}


# CI/CD + Docker Image Integration Test via Github Workflow

@app.get("/cicd_docker")
def cicd_and_docker_integration():
    return {"status": "E2E success."}


app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(todos.router)
