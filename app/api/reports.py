from typing import List
from datetime import datetime

from fastapi import APIRouter, APIRouter, HTTPException, Response

from app.api.models import Report


reports_db = [
    {
        "id": "fc43c30d-61d3-4739-a53d-9ea679c23c91",
        "content": {
            "ph h2o": 5.9,
            "ph CaCL2": 5.1,
            "Al": 0,
            "H+Al": 4.2,
            "Ca": 1.8,
            "Mg": 1.1,
            "Na": 0,
            "CTC a PH7": 7.3,
            "P": 4.7,
            "K": 0.17,
            "S": 6,
            "MO": 26,
            "Areia": "Lucas",
            "Silte": "Matheus",
            "Argila": "José"
        },
        "status": "pending",
        "created_at": "2025-05-10T19:14:03.606753",
        "updated_at": "2025-05-10T19:14:03.606782",
        "user_id": 0
    }
]

reports = movies = APIRouter()


@reports.get("/", response_model=List[Report])
async def read_root():
    return reports_db


@reports.post("/", response_model=Report, status_code=201)
async def create_report(report: Report):
    report.created_at = datetime.now().isoformat()
    report.updated_at = datetime.now().isoformat()
    reports_db.append(report.model_dump())
    return report


@reports.put("/{report_id}")
async def update_report(report_id: str, report: Report):
    for db_report in reports_db:
        if db_report["id"] == report_id:
            db_report.update(report.model_dump(exclude_unset=True))
            db_report["updated_at"] = datetime.now().isoformat()
            return db_report
    raise HTTPException(status_code=404, detail="Report not found")


@reports.delete("/{report_id}", status_code=204)
async def delete_report(report_id: str):
    for db_report in reports_db[:]:
        if db_report["id"] == report_id:
            reports_db.remove(db_report)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail="Report not found")
