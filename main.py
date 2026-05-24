from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import SessionLocal, engine, Base
from models import Resource
from cost_engine import detect_waste

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database session
db: Session = SessionLocal()

# Seed sample data
if db.query(Resource).count() == 0:
    sample_resources = [
        Resource(
            name="EC2-prod",
            type="EC2",
            cpu_utilization=5,
            cost_per_month=120
        ),
        Resource(
            name="EC2-dev",
            type="EC2",
            cpu_utilization=20,
            cost_per_month=80
        ),
        Resource(
            name="RDS-db",
            type="RDS",
            cpu_utilization=70,
            cost_per_month=300
        )
    ]

    db.add_all(sample_resources)
    db.commit()


# API: Get all resources
@app.get("/resources")
def get_resources():
    return db.query(Resource).all()


# API: Detect cloud waste
@app.get("/waste")
def get_waste():
    return detect_waste(db)