from enum import Enum


class RequestSortDefinitionItemType(str, Enum):
    DOCUMENT = "DOCUMENT"
    FIELD = "FIELD"
    SCORE = "SCORE"

    def __str__(self) -> str:
        return str(self.value)
