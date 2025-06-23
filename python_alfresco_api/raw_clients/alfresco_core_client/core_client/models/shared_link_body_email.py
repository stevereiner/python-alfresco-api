from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedLinkBodyEmail")


@_attrs_define
class SharedLinkBodyEmail:
    """
    Attributes:
        client (Union[Unset, str]):
        locale (Union[Unset, str]):
        message (Union[Unset, str]):
        recipient_emails (Union[Unset, list[str]]):
    """

    client: Union[Unset, str] = UNSET
    locale: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    recipient_emails: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client = self.client

        locale = self.locale

        message = self.message

        recipient_emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.recipient_emails, Unset):
            recipient_emails = self.recipient_emails

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if client is not UNSET:
            field_dict["client"] = client
        if locale is not UNSET:
            field_dict["locale"] = locale
        if message is not UNSET:
            field_dict["message"] = message
        if recipient_emails is not UNSET:
            field_dict["recipientEmails"] = recipient_emails

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        client = d.pop("client", UNSET)

        locale = d.pop("locale", UNSET)

        message = d.pop("message", UNSET)

        recipient_emails = cast(list[str], d.pop("recipientEmails", UNSET))

        shared_link_body_email = cls(
            client=client,
            locale=locale,
            message=message,
            recipient_emails=recipient_emails,
        )

        shared_link_body_email.additional_properties = d
        return shared_link_body_email

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
