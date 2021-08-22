from datetime import datetime
from typing import Optional
from uuid import UUID

from apps.core.utils.format import to_camel_case
from pydantic import BaseModel


class PydanticBase(BaseModel):
    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True


class SchemaBase(PydanticBase):
    ...


class SchemaInDBBase(SchemaBase):
    uuid: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        alias_generator = to_camel_case
        allow_population_by_field_name = True
