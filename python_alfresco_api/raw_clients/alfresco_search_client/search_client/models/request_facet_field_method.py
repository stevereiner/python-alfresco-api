from enum import Enum


class RequestFacetFieldMethod(str, Enum):
    ENUM = "ENUM"
    FC = "FC"

    def __str__(self) -> str:
        return str(self.value)
