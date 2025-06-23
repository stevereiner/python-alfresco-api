from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment_paging_list import DeploymentPagingList


T = TypeVar("T", bound="DeploymentPaging")


@_attrs_define
class DeploymentPaging:
    """
    Attributes:
        list_ (Union[Unset, DeploymentPagingList]):
    """

    list_: Union[Unset, "DeploymentPagingList"] = UNSET
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
        from ..models.deployment_paging_list import DeploymentPagingList

        d = dict(src_dict)
        _list_ = d.pop("list", UNSET)
        list_: Union[Unset, DeploymentPagingList]
        if isinstance(_list_, Unset):
            list_ = UNSET
        else:
            list_ = DeploymentPagingList.from_dict(_list_)

        deployment_paging = cls(
            list_=list_,
        )

        deployment_paging.additional_properties = d
        return deployment_paging

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
