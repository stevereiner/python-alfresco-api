from enum import Enum


class RequestScopeLocations(str, Enum):
    DELETED_NODES = "deleted-nodes"
    NODES = "nodes"
    VERSIONS = "versions"

    def __str__(self) -> str:
        return str(self.value)
