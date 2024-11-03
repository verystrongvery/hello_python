from fastapi import FastAPI

from domain.student import student_router

app = FastAPI()

app.include_router(student_router.router)