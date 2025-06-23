from enum import Enum


class PersonNetworkSubscriptionLevel(str, Enum):
    ENTERPRISE = "Enterprise"
    FREE = "Free"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
