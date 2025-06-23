from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deployment import Deployment


T = TypeVar("T", bound="DeploymentEntry")


@_attrs_define
class DeploymentEntry:
    """
    Attributes:
        entry (Union[Unset, Deployment]): A deployment resource represents one file inside a deployment.

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
    """

    entry: Union[Unset, "Deployment"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entry: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.entry, Unset):
            entry = self.entry.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entry is not UNSET:
            field_dict["entry"] = entry

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment import Deployment

        d = dict(src_dict)
        _entry = d.pop("entry", UNSET)
        entry: Union[Unset, Deployment]
        if isinstance(_entry, Unset):
            entry = UNSET
        else:
            entry = Deployment.from_dict(_entry)

        deployment_entry = cls(
            entry=entry,
        )

        deployment_entry.additional_properties = d
        return deployment_entry

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
