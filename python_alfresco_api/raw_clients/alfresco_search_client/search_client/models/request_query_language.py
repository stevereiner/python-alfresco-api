from enum import Enum


class RequestQueryLanguage(str, Enum):
    AFTS = "afts"
    CMIS = "cmis"
    LUCENE = "lucene"

    def __str__(self) -> str:
        return str(self.value)
