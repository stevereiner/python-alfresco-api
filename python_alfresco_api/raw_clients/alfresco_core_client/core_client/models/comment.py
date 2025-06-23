import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.person import Person


T = TypeVar("T", bound="Comment")


@_attrs_define
class Comment:
    """
    Attributes:
        can_delete (bool):
        can_edit (bool):
        content (str):
        created_at (datetime.datetime):
        created_by (Person):
        edited (bool):
        id (str):
        modified_at (datetime.datetime):
        modified_by (Person):
        title (str):
    """

    can_delete: bool
    can_edit: bool
    content: str
    created_at: datetime.datetime
    created_by: "Person"
    edited: bool
    id: str
    modified_at: datetime.datetime
    modified_by: "Person"
    title: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        can_delete = self.can_delete

        can_edit = self.can_edit

        content = self.content

        created_at = self.created_at.isoformat()

        created_by = self.created_by.to_dict()

        edited = self.edited

        id = self.id

        modified_at = self.modified_at.isoformat()

        modified_by = self.modified_by.to_dict()

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "canDelete": can_delete,
                "canEdit": can_edit,
                "content": content,
                "createdAt": created_at,
                "createdBy": created_by,
                "edited": edited,
                "id": id,
                "modifiedAt": modified_at,
                "modifiedBy": modified_by,
                "title": title,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.person import Person

        d = dict(src_dict)
        can_delete = d.pop("canDelete")

        can_edit = d.pop("canEdit")

        content = d.pop("content")

        created_at = isoparse(d.pop("createdAt"))

        created_by = Person.from_dict(d.pop("createdBy"))

        edited = d.pop("edited")

        id = d.pop("id")

        modified_at = isoparse(d.pop("modifiedAt"))

        modified_by = Person.from_dict(d.pop("modifiedBy"))

        title = d.pop("title")

        comment = cls(
            can_delete=can_delete,
            can_edit=can_edit,
            content=content,
            created_at=created_at,
            created_by=created_by,
            edited=edited,
            id=id,
            modified_at=modified_at,
            modified_by=modified_by,
            title=title,
        )

        comment.additional_properties = d
        return comment

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
