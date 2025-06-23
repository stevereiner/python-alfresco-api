from enum import Enum


class RequestFacetFieldSort(str, Enum):
    COUNT = "COUNT"
    INDEX = "INDEX"

    def __str__(self) -> str:
        return str(self.value)
