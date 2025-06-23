import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person import Person


T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """A process item.

    Attributes:
        created_at (Union[Unset, datetime.datetime]):
        created_by (Union[Unset, Person]):
        description (Union[Unset, str]):
        edited (Union[Unset, bool]):
        id (Union[Unset, str]):
        mime_type (Union[Unset, str]):
        modified_at (Union[Unset, datetime.datetime]):
        modified_by (Union[Unset, Person]):
        name (Union[Unset, str]):
        size (Union[Unset, int]):
        title (Union[Unset, str]):
        value (Union[Unset, int]):
    """

    created_at: Union[Unset, datetime.datetime] = UNSET
    created_by: Union[Unset, "Person"] = UNSET
    description: Union[Unset, str] = UNSET
    edited: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    modified_at: Union[Unset, datetime.datetime] = UNSET
    modified_by: Union[Unset, "Person"] = UNSET
    name: Union[Unset, str] = UNSET
    size: Union[Unset, int] = UNSET
    title: Union[Unset, str] = UNSET
    value: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        created_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        description = self.description

        edited = self.edited

        id = self.id

        mime_type = self.mime_type

        modified_at: Union[Unset, str] = UNSET
        if not isinstance(self.modified_at, Unset):
            modified_at = self.modified_at.isoformat()

        modified_by: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.modified_by, Unset):
            modified_by = self.modified_by.to_dict()

        name = self.name

        size = self.size

        title = self.title

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if edited is not UNSET:
            field_dict["edited"] = edited
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if modified_at is not UNSET:
            field_dict["modifiedAt"] = modified_at
        if modified_by is not UNSET:
            field_dict["modifiedBy"] = modified_by
        if name is not UNSET:
            field_dict["name"] = name
        if size is not UNSET:
            field_dict["size"] = size
        if title is not UNSET:
            field_dict["title"] = title
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person import Person

        d = dict(src_dict)
        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, Person]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = Person.from_dict(_created_by)

        description = d.pop("description", UNSET)

        edited = d.pop("edited", UNSET)

        id = d.pop("id", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        _modified_at = d.pop("modifiedAt", UNSET)
        modified_at: Union[Unset, datetime.datetime]
        if isinstance(_modified_at, Unset):
            modified_at = UNSET
        else:
            modified_at = isoparse(_modified_at)

        _modified_by = d.pop("modifiedBy", UNSET)
        modified_by: Union[Unset, Person]
        if isinstance(_modified_by, Unset):
            modified_by = UNSET
        else:
            modified_by = Person.from_dict(_modified_by)

        name = d.pop("name", UNSET)

        size = d.pop("size", UNSET)

        title = d.pop("title", UNSET)

        value = d.pop("value", UNSET)

        item = cls(
            created_at=created_at,
            created_by=created_by,
            description=description,
            edited=edited,
            id=id,
            mime_type=mime_type,
            modified_at=modified_at,
            modified_by=modified_by,
            name=name,
            size=size,
            title=title,
            value=value,
        )

        item.additional_properties = d
        return item

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
