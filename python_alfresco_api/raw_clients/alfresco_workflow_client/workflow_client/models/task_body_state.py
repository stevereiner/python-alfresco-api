from enum import Enum


class TaskBodyState(str, Enum):
    CLAIMED = "claimed"
    COMPLETED = "completed"
    RESOLVED = "resolved"
    UNCLAIMED = "unclaimed"

    def __str__(self) -> str:
        return str(self.value)
