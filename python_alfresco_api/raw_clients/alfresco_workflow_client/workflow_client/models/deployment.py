import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Deployment")


@_attrs_define
class Deployment:
    """A deployment resource represents one file inside a deployment.

    Process files, forms and perhaps some other files are authored in
    a separate environment. The act of deployment brings them into the runtime
    workflow engine.

    A deployment is a collection of files that include all resources to specify
    one or more process definitions. After deployment, the included process
    definitions are known to the workflow runtime engine and new processes can
    be started.

    Users can then continue to edit the process and other files in their
    authoring environment like e.g. our eclipse based process editor.
    A redeployment will result in a complete separate deployment containing new
    versions of the process definition.

    When a process definition inside a new deployment has the same key as an
    existing process definition, then it is considered a new version of the
    existing process definition.

        Attributes:
            id (str):
            category (Union[Unset, str]):
            deployed_at (Union[Unset, datetime.datetime]):
            name (Union[Unset, str]):
    """

    id: str
    category: Union[Unset, str] = UNSET
    deployed_at: Union[Unset, datetime.datetime] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        deployed_at: Union[Unset, str] = UNSET
        if not isinstance(self.deployed_at, Unset):
            deployed_at = self.deployed_at.isoformat()

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if deployed_at is not UNSET:
            field_dict["deployedAt"] = deployed_at
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        category = d.pop("category", UNSET)

        _deployed_at = d.pop("deployedAt", UNSET)
        deployed_at: Union[Unset, datetime.datetime]
        if isinstance(_deployed_at, Unset):
            deployed_at = UNSET
        else:
            deployed_at = isoparse(_deployed_at)

        name = d.pop("name", UNSET)

        deployment = cls(
            id=id,
            category=category,
            deployed_at=deployed_at,
            name=name,
        )

        deployment.additional_properties = d
        return deployment

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
