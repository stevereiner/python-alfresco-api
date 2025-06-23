from enum import Enum


class DownloadStatus(str, Enum):
    CANCELLED = "CANCELLED"
    DONE = "DONE"
    IN_PROGRESS = "IN_PROGRESS"
    MAX_CONTENT_SIZE_EXCEEDED = "MAX_CONTENT_SIZE_EXCEEDED"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
