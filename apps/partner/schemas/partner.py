from apps.core.schemas.base import SchemaBase
from apps.core.schemas.geo_json import MultiPolygon, Point


class PartnerSchema(SchemaBase):
    id: str
    tradingName: str
    ownerName: str
    document: str
    coverageArea: MultiPolygon
    address: Point
