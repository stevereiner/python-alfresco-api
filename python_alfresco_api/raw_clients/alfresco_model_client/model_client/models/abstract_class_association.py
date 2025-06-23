from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_class_association_source import AbstractClassAssociationSource


T = TypeVar("T", bound="AbstractClassAssociation")


@_attrs_define
class AbstractClassAssociation:
    """
    Attributes:
        id (str):
        description (Union[Unset, str]):
        is_child (Union[Unset, bool]):
        is_protected (Union[Unset, bool]):
        source (Union[Unset, AbstractClassAssociationSource]):
        target (Union[Unset, AbstractClassAssociationSource]):
        title (Union[Unset, str]):
    """

    id: str
    description: Union[Unset, str] = UNSET
    is_child: Union[Unset, bool] = UNSET
    is_protected: Union[Unset, bool] = UNSET
    source: Union[Unset, "AbstractClassAssociationSource"] = UNSET
    target: Union[Unset, "AbstractClassAssociationSource"] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        is_child = self.is_child

        is_protected = self.is_protected

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        target: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if is_child is not UNSET:
            field_dict["isChild"] = is_child
        if is_protected is not UNSET:
            field_dict["isProtected"] = is_protected
        if source is not UNSET:
            field_dict["source"] = source
        if target is not UNSET:
            field_dict["target"] = target
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_class_association_source import AbstractClassAssociationSource

        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description", UNSET)

        is_child = d.pop("isChild", UNSET)

        is_protected = d.pop("isProtected", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, AbstractClassAssociationSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = AbstractClassAssociationSource.from_dict(_source)

        _target = d.pop("target", UNSET)
        target: Union[Unset, AbstractClassAssociationSource]
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = AbstractClassAssociationSource.from_dict(_target)

        title = d.pop("title", UNSET)

        abstract_class_association = cls(
            id=id,
            description=description,
            is_child=is_child,
            is_protected=is_protected,
            source=source,
            target=target,
            title=title,
        )

        abstract_class_association.additional_properties = d
        return abstract_class_association

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
