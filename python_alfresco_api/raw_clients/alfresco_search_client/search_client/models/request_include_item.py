from enum import Enum


class RequestIncludeItem(str, Enum):
    ALLOWABLEOPERATIONS = "allowableOperations"
    ASPECTNAMES = "aspectNames"
    ISLINK = "isLink"
    ISLOCKED = "isLocked"
    PATH = "path"
    PROPERTIES = "properties"

    def __str__(self) -> str:
        return str(self.value)
