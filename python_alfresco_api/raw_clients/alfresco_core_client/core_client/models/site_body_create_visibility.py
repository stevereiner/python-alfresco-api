from enum import Enum


class SiteBodyCreateVisibility(str, Enum):
    MODERATED = "MODERATED"
    PRIVATE = "PRIVATE"
    PUBLIC = "PUBLIC"

    def __str__(self) -> str:
        return str(self.value)
