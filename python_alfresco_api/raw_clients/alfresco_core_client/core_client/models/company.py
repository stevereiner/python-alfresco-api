from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Company")


@_attrs_define
class Company:
    """
    Attributes:
        address1 (Union[Unset, str]):
        address2 (Union[Unset, str]):
        address3 (Union[Unset, str]):
        email (Union[Unset, str]):
        fax (Union[Unset, str]):
        organization (Union[Unset, str]):
        postcode (Union[Unset, str]):
        telephone (Union[Unset, str]):
    """

    address1: Union[Unset, str] = UNSET
    address2: Union[Unset, str] = UNSET
    address3: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    fax: Union[Unset, str] = UNSET
    organization: Union[Unset, str] = UNSET
    postcode: Union[Unset, str] = UNSET
    telephone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address1 = self.address1

        address2 = self.address2

        address3 = self.address3

        email = self.email

        fax = self.fax

        organization = self.organization

        postcode = self.postcode

        telephone = self.telephone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if address2 is not UNSET:
            field_dict["address2"] = address2
        if address3 is not UNSET:
            field_dict["address3"] = address3
        if email is not UNSET:
            field_dict["email"] = email
        if fax is not UNSET:
            field_dict["fax"] = fax
        if organization is not UNSET:
            field_dict["organization"] = organization
        if postcode is not UNSET:
            field_dict["postcode"] = postcode
        if telephone is not UNSET:
            field_dict["telephone"] = telephone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        address1 = d.pop("address1", UNSET)

        address2 = d.pop("address2", UNSET)

        address3 = d.pop("address3", UNSET)

        email = d.pop("email", UNSET)

        fax = d.pop("fax", UNSET)

        organization = d.pop("organization", UNSET)

        postcode = d.pop("postcode", UNSET)

        telephone = d.pop("telephone", UNSET)

        company = cls(
            address1=address1,
            address2=address2,
            address3=address3,
            email=email,
            fax=fax,
            organization=organization,
            postcode=postcode,
            telephone=telephone,
        )

        company.additional_properties = d
        return company

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
