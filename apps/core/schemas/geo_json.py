import abc
from typing import Any, List, Tuple, Union

from pydantic import BaseModel, Field

NumType = Union[float, int]
Position = Union[Tuple[NumType, NumType], Tuple[NumType, NumType, NumType]]


class _GeometryBase(BaseModel, abc.ABC):
    """Base class for geometry models"""

    coordinates: Any  # will be constrained in child classes

    @property
    def __geo_interface__(self):
        return self.dict()


class Point(_GeometryBase):
    """Point Model"""

    type: str = Field("Point", const=True)
    coordinates: Position


class MultiPolygon(_GeometryBase):
    """MultiPolygon Model"""

    type: str = Field("MultiPolygon", const=True)
    coordinates: List[List[List[Position]]]
