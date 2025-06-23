from enum import Enum


class GroupMemberMemberType(str, Enum):
    GROUP = "GROUP"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
