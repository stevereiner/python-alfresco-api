from enum import Enum


class CandidateCandidateType(str, Enum):
    GROUP = "group"
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
