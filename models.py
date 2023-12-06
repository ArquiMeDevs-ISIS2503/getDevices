from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Device(Base):
    __tablename__ = 'devices_device' 

    id = Column(Integer, primary_key=True, index=True)
    site_id = Column(Integer, ForeignKey('sites_site.id'), index=True)
    site = relationship("Site", back_populates="devices")
    active = Column(Boolean)
    code = Column(Integer, nullable=True, default=None)
    builder = Column(String(length=50))
    name = Column(String(length=50))
    amount = Column(Integer, nullable=True, default=None)
    type = Column(String(length=50))
    date_maintenance = Column(DateTime, server_default='now()', nullable=True)

    def __str__(self):
        return '%s %s' % (self.name, self.type)

class Site(Base):
    __tablename__ = 'sites_site' 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    devices = relationship("Device", back_populates="site")

    def __str__(self):
        return '{}'.format(self.name)
