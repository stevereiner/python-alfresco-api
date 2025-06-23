from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_member_paging_list import GroupMemberPagingList


T = TypeVar("T", bound="GroupMemberPaging")


@_attrs_define
class GroupMemberPaging:
    """
    Attributes:
        list_ (Union[Unset, GroupMemberPagingList]):
    """

    list_: Union[Unset, "GroupMemberPagingList"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        list_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.list_, Unset):
            list_ = self.list_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if list_ is not UNSET:
            field_dict["list"] = list_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_member_paging_list import GroupMemberPagingList

        d = dict(src_dict)
        _list_ = d.pop("list", UNSET)
        list_: Union[Unset, GroupMemberPagingList]
        if isinstance(_list_, Unset):
            list_ = UNSET
        else:
            list_ = GroupMemberPagingList.from_dict(_list_)

        group_member_paging = cls(
            list_=list_,
        )

        group_member_paging.additional_properties = d
        return group_member_paging

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
