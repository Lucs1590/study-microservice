from fastapi import FastAPI

from app.api.reports import reports

app = FastAPI()

app.include_router(reports, prefix="/reports", tags=["Reports"])
