from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base

class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, ForeignKey('sites.id'), index=True)
    active = Column(Boolean)
    code = Column(Integer, nullable=True, default=None)
    builder = Column(String(length=50))
    name = Column(String(length=50))
    amount = Column(Integer, nullable=True, default=None)
    type = Column(String(length=50))
    date_maintenance = Column(DateTime, server_default=func.now(), nullable=True)

    site = relationship("Site", back_populates="devices")

    def __str__(self):
        return '%s %s' % (self.name, self.type)