from enum import Enum


class RenditionStatus(str, Enum):
    CREATED = "CREATED"
    NOT_CREATED = "NOT_CREATED"

    def __str__(self) -> str:
        return str(self.value)
