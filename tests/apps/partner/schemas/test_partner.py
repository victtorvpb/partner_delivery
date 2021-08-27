from typing import Generator

import pytest
from apps.partner.schemas.partner import PartnerSchema
from pydantic.error_wrappers import ValidationError


def test_schema_partner_sucess(faker: Generator) -> None:
    json_schema = {
        "id": 1,
        "tradingName": "Adega da Cerveja - Pinheiros",
        "ownerName": "Zé da Silva",
        "document": "1432132123891/0001",
        "coverageArea": {
            "type": "MultiPolygon",
            "coordinates": [
                [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
            ],
        },
        "address": {"type": "Point", "coordinates": [-46.57421, -21.785741]},
    }

    PartnerSchema.validate(json_schema)


def test_schema_partner_fail(faker: Generator) -> None:
    json_schema = {
        "id": 1,
        "tradingName": "Adega da Cerveja - Pinheiros",
        "ownerName": "Zé da Silva",
        "document": "1432132123891/0001",
        "coverageArea": {
            "type": "MultiPolygon1",
            "coordinates": [
                [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]],
            ],
        },
        "address": {"type": "Point", "coordinates": [-46.57421, -21.785741]},
    }
    with pytest.raises(ValidationError):
        PartnerSchema.validate(json_schema)
