import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.capabilities import Capabilities
    from ..models.company import Company
    from ..models.person_properties import PersonProperties


T = TypeVar("T", bound="Person")


@_attrs_define
class Person:
    """
    Attributes:
        email (str):
        enabled (bool):  Default: True.
        first_name (str):
        id (str):
        aspect_names (Union[Unset, list[str]]):
        avatar_id (Union[Unset, str]):
        capabilities (Union[Unset, Capabilities]):
        company (Union[Unset, Company]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        email_notifications_enabled (Union[Unset, bool]):  Default: True.
        google_id (Union[Unset, str]):
        instant_message_id (Union[Unset, str]):
        job_title (Union[Unset, str]):
        last_name (Union[Unset, str]):
        location (Union[Unset, str]):
        mobile (Union[Unset, str]):
        properties (Union[Unset, PersonProperties]):
        skype_id (Union[Unset, str]):
        status_updated_at (Union[Unset, datetime.datetime]):
        telephone (Union[Unset, str]):
        user_status (Union[Unset, str]):
    """

    email: str
    first_name: str
    id: str
    enabled: bool = True
    aspect_names: Union[Unset, list[str]] = UNSET
    avatar_id: Union[Unset, str] = UNSET
    capabilities: Union[Unset, "Capabilities"] = UNSET
    company: Union[Unset, "Company"] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    email_notifications_enabled: Union[Unset, bool] = True
    google_id: Union[Unset, str] = UNSET
    instant_message_id: Union[Unset, str] = UNSET
    job_title: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    mobile: Union[Unset, str] = UNSET
    properties: Union[Unset, "PersonProperties"] = UNSET
    skype_id: Union[Unset, str] = UNSET
    status_updated_at: Union[Unset, datetime.datetime] = UNSET
    telephone: Union[Unset, str] = UNSET
    user_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        enabled = self.enabled

        first_name = self.first_name

        id = self.id

        aspect_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aspect_names, Unset):
            aspect_names = self.aspect_names

        avatar_id = self.avatar_id

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        company: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        description = self.description

        display_name = self.display_name

        email_notifications_enabled = self.email_notifications_enabled

        google_id = self.google_id

        instant_message_id = self.instant_message_id

        job_title = self.job_title

        last_name = self.last_name

        location = self.location

        mobile = self.mobile

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        skype_id = self.skype_id

        status_updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.status_updated_at, Unset):
            status_updated_at = self.status_updated_at.isoformat()

        telephone = self.telephone

        user_status = self.user_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "enabled": enabled,
                "firstName": first_name,
                "id": id,
            }
        )
        if aspect_names is not UNSET:
            field_dict["aspectNames"] = aspect_names
        if avatar_id is not UNSET:
            field_dict["avatarId"] = avatar_id
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if company is not UNSET:
            field_dict["company"] = company
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if email_notifications_enabled is not UNSET:
            field_dict["emailNotificationsEnabled"] = email_notifications_enabled
        if google_id is not UNSET:
            field_dict["googleId"] = google_id
        if instant_message_id is not UNSET:
            field_dict["instantMessageId"] = instant_message_id
        if job_title is not UNSET:
            field_dict["jobTitle"] = job_title
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if location is not UNSET:
            field_dict["location"] = location
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if properties is not UNSET:
            field_dict["properties"] = properties
        if skype_id is not UNSET:
            field_dict["skypeId"] = skype_id
        if status_updated_at is not UNSET:
            field_dict["statusUpdatedAt"] = status_updated_at
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if user_status is not UNSET:
            field_dict["userStatus"] = user_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capabilities import Capabilities
        from ..models.company import Company
        from ..models.person_properties import PersonProperties

        d = dict(src_dict)
        email = d.pop("email")

        enabled = d.pop("enabled")

        first_name = d.pop("firstName")

        id = d.pop("id")

        aspect_names = cast(list[str], d.pop("aspectNames", UNSET))

        avatar_id = d.pop("avatarId", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, Capabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = Capabilities.from_dict(_capabilities)

        _company = d.pop("company", UNSET)
        company: Union[Unset, Company]
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = Company.from_dict(_company)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        email_notifications_enabled = d.pop("emailNotificationsEnabled", UNSET)

        google_id = d.pop("googleId", UNSET)

        instant_message_id = d.pop("instantMessageId", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        last_name = d.pop("lastName", UNSET)

        location = d.pop("location", UNSET)

        mobile = d.pop("mobile", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, PersonProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = PersonProperties.from_dict(_properties)

        skype_id = d.pop("skypeId", UNSET)

        _status_updated_at = d.pop("statusUpdatedAt", UNSET)
        status_updated_at: Union[Unset, datetime.datetime]
        if isinstance(_status_updated_at, Unset):
            status_updated_at = UNSET
        else:
            status_updated_at = isoparse(_status_updated_at)

        telephone = d.pop("telephone", UNSET)

        user_status = d.pop("userStatus", UNSET)

        person = cls(
            email=email,
            enabled=enabled,
            first_name=first_name,
            id=id,
            aspect_names=aspect_names,
            avatar_id=avatar_id,
            capabilities=capabilities,
            company=company,
            description=description,
            display_name=display_name,
            email_notifications_enabled=email_notifications_enabled,
            google_id=google_id,
            instant_message_id=instant_message_id,
            job_title=job_title,
            last_name=last_name,
            location=location,
            mobile=mobile,
            properties=properties,
            skype_id=skype_id,
            status_updated_at=status_updated_at,
            telephone=telephone,
            user_status=user_status,
        )

        person.additional_properties = d
        return person

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
