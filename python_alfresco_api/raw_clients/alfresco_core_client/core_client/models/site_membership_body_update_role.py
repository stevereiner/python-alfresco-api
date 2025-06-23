from enum import Enum


class SiteMembershipBodyUpdateRole(str, Enum):
    SITECOLLABORATOR = "SiteCollaborator"
    SITECONSUMER = "SiteConsumer"
    SITECONTRIBUTOR = "SiteContributor"
    SITEMANAGER = "SiteManager"

    def __str__(self) -> str:
        return str(self.value)
