from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SiteMembershipRequestBodyCreate")


@_attrs_define
class SiteMembershipRequestBodyCreate:
    """
    Attributes:
        id (str):
        client (Union[Unset, str]): Optional client name used when sending an email to the end user, defaults to "share"
            if not provided.
            **Note:** The client must be registered before this API can send an email.
            **Note:** This is available in Alfresco 7.0.0 and newer versions.
        message (Union[Unset, str]):
        title (Union[Unset, str]):
    """

    id: str
    client: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        client = self.client

        message = self.message

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if client is not UNSET:
            field_dict["client"] = client
        if message is not UNSET:
            field_dict["message"] = message
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        client = d.pop("client", UNSET)

        message = d.pop("message", UNSET)

        title = d.pop("title", UNSET)

        site_membership_request_body_create = cls(
            id=id,
            client=client,
            message=message,
            title=title,
        )

        site_membership_request_body_create.additional_properties = d
        return site_membership_request_body_create

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
