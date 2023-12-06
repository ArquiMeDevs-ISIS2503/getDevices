from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database import Base

class Site(Base):
    __tablename__ = 'sites'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))

    devices = relationship("Device", back_populates="site")

    def __str__(self):
        return '{}'.format(self.name)
