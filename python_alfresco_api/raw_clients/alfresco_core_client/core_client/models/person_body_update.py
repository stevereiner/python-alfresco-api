from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company import Company
    from ..models.person_body_update_properties import PersonBodyUpdateProperties


T = TypeVar("T", bound="PersonBodyUpdate")


@_attrs_define
class PersonBodyUpdate:
    """
    Attributes:
        aspect_names (Union[Unset, list[str]]):
        company (Union[Unset, Company]):
        description (Union[Unset, str]):
        email (Union[Unset, str]):
        email_notifications_enabled (Union[Unset, bool]):
        enabled (Union[Unset, bool]):
        first_name (Union[Unset, str]):
        google_id (Union[Unset, str]):
        instant_message_id (Union[Unset, str]):
        job_title (Union[Unset, str]):
        last_name (Union[Unset, str]):
        location (Union[Unset, str]):
        mobile (Union[Unset, str]):
        old_password (Union[Unset, str]):
        password (Union[Unset, str]):
        properties (Union[Unset, PersonBodyUpdateProperties]):
        skype_id (Union[Unset, str]):
        telephone (Union[Unset, str]):
        user_status (Union[Unset, str]):
    """

    aspect_names: Union[Unset, list[str]] = UNSET
    company: Union[Unset, "Company"] = UNSET
    description: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    email_notifications_enabled: Union[Unset, bool] = UNSET
    enabled: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    google_id: Union[Unset, str] = UNSET
    instant_message_id: Union[Unset, str] = UNSET
    job_title: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    location: Union[Unset, str] = UNSET
    mobile: Union[Unset, str] = UNSET
    old_password: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    properties: Union[Unset, "PersonBodyUpdateProperties"] = UNSET
    skype_id: Union[Unset, str] = UNSET
    telephone: Union[Unset, str] = UNSET
    user_status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        aspect_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aspect_names, Unset):
            aspect_names = self.aspect_names

        company: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.company, Unset):
            company = self.company.to_dict()

        description = self.description

        email = self.email

        email_notifications_enabled = self.email_notifications_enabled

        enabled = self.enabled

        first_name = self.first_name

        google_id = self.google_id

        instant_message_id = self.instant_message_id

        job_title = self.job_title

        last_name = self.last_name

        location = self.location

        mobile = self.mobile

        old_password = self.old_password

        password = self.password

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        skype_id = self.skype_id

        telephone = self.telephone

        user_status = self.user_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_names is not UNSET:
            field_dict["aspectNames"] = aspect_names
        if company is not UNSET:
            field_dict["company"] = company
        if description is not UNSET:
            field_dict["description"] = description
        if email is not UNSET:
            field_dict["email"] = email
        if email_notifications_enabled is not UNSET:
            field_dict["emailNotificationsEnabled"] = email_notifications_enabled
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
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
        if old_password is not UNSET:
            field_dict["oldPassword"] = old_password
        if password is not UNSET:
            field_dict["password"] = password
        if properties is not UNSET:
            field_dict["properties"] = properties
        if skype_id is not UNSET:
            field_dict["skypeId"] = skype_id
        if telephone is not UNSET:
            field_dict["telephone"] = telephone
        if user_status is not UNSET:
            field_dict["userStatus"] = user_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company import Company
        from ..models.person_body_update_properties import PersonBodyUpdateProperties

        d = dict(src_dict)
        aspect_names = cast(list[str], d.pop("aspectNames", UNSET))

        _company = d.pop("company", UNSET)
        company: Union[Unset, Company]
        if isinstance(_company, Unset):
            company = UNSET
        else:
            company = Company.from_dict(_company)

        description = d.pop("description", UNSET)

        email = d.pop("email", UNSET)

        email_notifications_enabled = d.pop("emailNotificationsEnabled", UNSET)

        enabled = d.pop("enabled", UNSET)

        first_name = d.pop("firstName", UNSET)

        google_id = d.pop("googleId", UNSET)

        instant_message_id = d.pop("instantMessageId", UNSET)

        job_title = d.pop("jobTitle", UNSET)

        last_name = d.pop("lastName", UNSET)

        location = d.pop("location", UNSET)

        mobile = d.pop("mobile", UNSET)

        old_password = d.pop("oldPassword", UNSET)

        password = d.pop("password", UNSET)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, PersonBodyUpdateProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = PersonBodyUpdateProperties.from_dict(_properties)

        skype_id = d.pop("skypeId", UNSET)

        telephone = d.pop("telephone", UNSET)

        user_status = d.pop("userStatus", UNSET)

        person_body_update = cls(
            aspect_names=aspect_names,
            company=company,
            description=description,
            email=email,
            email_notifications_enabled=email_notifications_enabled,
            enabled=enabled,
            first_name=first_name,
            google_id=google_id,
            instant_message_id=instant_message_id,
            job_title=job_title,
            last_name=last_name,
            location=location,
            mobile=mobile,
            old_password=old_password,
            password=password,
            properties=properties,
            skype_id=skype_id,
            telephone=telephone,
            user_status=user_status,
        )

        person_body_update.additional_properties = d
        return person_body_update

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
