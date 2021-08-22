from apps.core.schemas.base import PydanticBase


class ResponseMessage(PydanticBase):
    status: str
