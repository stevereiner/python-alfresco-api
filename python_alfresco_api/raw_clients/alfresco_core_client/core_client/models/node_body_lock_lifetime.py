from enum import Enum


class NodeBodyLockLifetime(str, Enum):
    EPHEMERAL = "EPHEMERAL"
    PERSISTENT = "PERSISTENT"

    def __str__(self) -> str:
        return str(self.value)
