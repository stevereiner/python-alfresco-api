from enum import Enum


class ResultSetContextSpellcheckItemType(str, Enum):
    DIDYOUMEAN = "didYouMean"
    SEARCHINSTEADFOR = "searchInsteadFor"

    def __str__(self) -> str:
        return str(self.value)
