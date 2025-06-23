from enum import Enum


class RatingBodyId(str, Enum):
    FIVESTAR = "fiveStar"
    LIKES = "likes"

    def __str__(self) -> str:
        return str(self.value)
