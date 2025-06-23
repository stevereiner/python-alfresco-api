from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.site_member_paging_list import SiteMemberPagingList


T = TypeVar("T", bound="SiteMemberPaging")


@_attrs_define
class SiteMemberPaging:
    """
    Attributes:
        list_ (SiteMemberPagingList):
    """

    list_: "SiteMemberPagingList"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_ = self.list_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "list": list_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.site_member_paging_list import SiteMemberPagingList

        d = dict(src_dict)
        list_ = SiteMemberPagingList.from_dict(d.pop("list"))

        site_member_paging = cls(
            list_=list_,
        )

        site_member_paging.additional_properties = d
        return site_member_paging

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
