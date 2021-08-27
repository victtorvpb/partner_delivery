from commons.db.base_class import SQLAlchemyBaseModel
from geoalchemy2 import Geometry
from sqlalchemy import Column, String


class Partner(SQLAlchemyBaseModel):

    external_id = Column(String, nullable=False, unique=True, index=True)
    owner_name = Column(String, nullable=False)
    document = Column(String, nullable=False, unique=True)

    address = Column(Geometry("POINT"))
    coordinates = Column(Geometry("MULTIPOLYGON"))
