from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from devices import Device
from sites import Site
from database import SessionLocal, engine
import crud

app = FastAPI()

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/prueba")
def read_root():
    return {"message": "Hola, mundo"}

@app.get("/devices")
def read_devices(db: Session = Depends(get_db)):
    return crud.get_devices(db)

@app.get("/devices/sede/{sede}")
def read_devices_by_sede(sede: str, db: Session = Depends(get_db)):
    return crud.get_devices_by_sede(db, sede)
