from enum import Enum


class GroupMembershipBodyCreateMemberType(str, Enum):
    GROUP = "GROUP"
    PERSON = "PERSON"

    def __str__(self) -> str:
        return str(self.value)
