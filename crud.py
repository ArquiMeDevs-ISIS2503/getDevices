# crud.py
from sqlalchemy.orm import Session
from devices import Device

def get_devices(db: Session):
    return db.query(Device).filter(Device.active == True).all()

def get_devices_by_sede(db: Session, sede: str):
    return db.query(Device).filter(Device.active == True, Device.site.has(name=sede)).all()
