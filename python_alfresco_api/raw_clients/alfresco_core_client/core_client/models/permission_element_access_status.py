from enum import Enum


class PermissionElementAccessStatus(str, Enum):
    ALLOWED = "ALLOWED"
    DENIED = "DENIED"

    def __str__(self) -> str:
        return str(self.value)
