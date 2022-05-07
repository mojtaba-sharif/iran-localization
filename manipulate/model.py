from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Province(Base):
    __tablename__ = "province"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    local_id = Column(String)
    code_rec = Column(String)

    counties = relationship("County", back_populates="province")


class County(Base):
    __tablename__ = "county"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    local_id = Column(String)
    code_rec = Column(String)

    province_id = Column(Integer, ForeignKey("province.id"), nullable=False)
    province = relationship("Province", back_populates="counties")

    areas = relationship("Area", back_populates="county")


class Area(Base):
    __tablename__ = "area"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    local_id = Column(String)
    code_rec = Column(String)

    county_id = Column(Integer, ForeignKey("county.id"), nullable=False)
    county = relationship("County", back_populates="areas")

    villages = relationship("Village", back_populates="area")


class Village(Base):
    __tablename__ = "village"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    local_id = Column(String)
    code_rec = Column(String)

    area_id = Column(Integer, ForeignKey("area.id"), nullable=False)
    area = relationship("Area", back_populates="villages")

    littleVillages = relationship("LittleVillage", back_populates="village")


class LittleVillage(Base):
    __tablename__ = "little_village"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    local_id = Column(String)
    code_rec = Column(String)
    diag = Column(String)

    village_id = Column(Integer, ForeignKey("village.id"), nullable=False)
    village = relationship("Village", back_populates="littleVillages")


def engine():
    engine = create_engine("postgresql://localization:localization94622@localhost:5433/localization", echo=True,
                           future=True)
    Base.metadata.create_all(engine)
    return engine
