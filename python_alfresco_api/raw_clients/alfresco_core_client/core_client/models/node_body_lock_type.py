from enum import Enum


class NodeBodyLockType(str, Enum):
    ALLOW_OWNER_CHANGES = "ALLOW_OWNER_CHANGES"
    FULL = "FULL"

    def __str__(self) -> str:
        return str(self.value)
