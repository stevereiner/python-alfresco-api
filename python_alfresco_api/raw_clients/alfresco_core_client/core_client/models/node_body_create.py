import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.association_body import AssociationBody
    from ..models.child_association_body import ChildAssociationBody
    from ..models.definition import Definition
    from ..models.node_body_create_association import NodeBodyCreateAssociation
    from ..models.node_body_create_properties import NodeBodyCreateProperties
    from ..models.permissions_body import PermissionsBody


T = TypeVar("T", bound="NodeBodyCreate")


@_attrs_define
class NodeBodyCreate:
    r"""
    Attributes:
        name (str): The name must not contain spaces or the following special characters: * " < > \ / ? : and |.
            The character . must not be used at the end of the name.
        node_type (str):
        aspect_names (Union[Unset, list[str]]):
        association (Union[Unset, NodeBodyCreateAssociation]):
        definition (Union[Unset, Definition]):
        permissions (Union[Unset, PermissionsBody]):
        properties (Union[Unset, NodeBodyCreateProperties]):
        relative_path (Union[Unset, str]):
        secondary_children (Union[Unset, list['ChildAssociationBody']]):
        targets (Union[Unset, list['AssociationBody']]):
    """

    name: str
    node_type: str
    aspect_names: Union[Unset, list[str]] = UNSET
    association: Union[Unset, "NodeBodyCreateAssociation"] = UNSET
    definition: Union[Unset, "Definition"] = UNSET
    permissions: Union[Unset, "PermissionsBody"] = UNSET
    properties: Union[Unset, "NodeBodyCreateProperties"] = UNSET
    relative_path: Union[Unset, str] = UNSET
    secondary_children: Union[Unset, list["ChildAssociationBody"]] = UNSET
    targets: Union[Unset, list["AssociationBody"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        node_type = self.node_type

        aspect_names: Union[Unset, list[str]] = UNSET
        if not isinstance(self.aspect_names, Unset):
            aspect_names = self.aspect_names

        association: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.association, Unset):
            association = self.association.to_dict()

        definition: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.definition, Unset):
            definition = self.definition.to_dict()

        permissions: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        properties: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = self.properties.to_dict()

        relative_path = self.relative_path

        secondary_children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.secondary_children, Unset):
            secondary_children = []
            for secondary_children_item_data in self.secondary_children:
                secondary_children_item = secondary_children_item_data.to_dict()
                secondary_children.append(secondary_children_item)

        targets: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.targets, Unset):
            targets = []
            for targets_item_data in self.targets:
                targets_item = targets_item_data.to_dict()
                targets.append(targets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "nodeType": node_type,
            }
        )
        if aspect_names is not UNSET:
            field_dict["aspectNames"] = aspect_names
        if association is not UNSET:
            field_dict["association"] = association
        if definition is not UNSET:
            field_dict["definition"] = definition
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if properties is not UNSET:
            field_dict["properties"] = properties
        if relative_path is not UNSET:
            field_dict["relativePath"] = relative_path
        if secondary_children is not UNSET:
            field_dict["secondaryChildren"] = secondary_children
        if targets is not UNSET:
            field_dict["targets"] = targets

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("nodeType", (None, str(self.node_type).encode(), "text/plain")))

        if not isinstance(self.aspect_names, Unset):
            for aspect_names_item_element in self.aspect_names:
                files.append(("aspectNames", (None, str(aspect_names_item_element).encode(), "text/plain")))

        if not isinstance(self.association, Unset):
            files.append(("association", (None, json.dumps(self.association.to_dict()).encode(), "application/json")))

        if not isinstance(self.definition, Unset):
            files.append(("definition", (None, json.dumps(self.definition.to_dict()).encode(), "application/json")))

        if not isinstance(self.permissions, Unset):
            files.append(("permissions", (None, json.dumps(self.permissions.to_dict()).encode(), "application/json")))

        if not isinstance(self.properties, Unset):
            files.append(("properties", (None, json.dumps(self.properties.to_dict()).encode(), "application/json")))

        if not isinstance(self.relative_path, Unset):
            files.append(("relativePath", (None, str(self.relative_path).encode(), "text/plain")))

        if not isinstance(self.secondary_children, Unset):
            for secondary_children_item_element in self.secondary_children:
                files.append(
                    (
                        "secondaryChildren",
                        (None, json.dumps(secondary_children_item_element.to_dict()).encode(), "application/json"),
                    )
                )

        if not isinstance(self.targets, Unset):
            for targets_item_element in self.targets:
                files.append(
                    ("targets", (None, json.dumps(targets_item_element.to_dict()).encode(), "application/json"))
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.association_body import AssociationBody
        from ..models.child_association_body import ChildAssociationBody
        from ..models.definition import Definition
        from ..models.node_body_create_association import NodeBodyCreateAssociation
        from ..models.node_body_create_properties import NodeBodyCreateProperties
        from ..models.permissions_body import PermissionsBody

        d = dict(src_dict)
        name = d.pop("name")

        node_type = d.pop("nodeType")

        aspect_names = cast(list[str], d.pop("aspectNames", UNSET))

        _association = d.pop("association", UNSET)
        association: Union[Unset, NodeBodyCreateAssociation]
        if isinstance(_association, Unset):
            association = UNSET
        else:
            association = NodeBodyCreateAssociation.from_dict(_association)

        _definition = d.pop("definition", UNSET)
        definition: Union[Unset, Definition]
        if isinstance(_definition, Unset):
            definition = UNSET
        else:
            definition = Definition.from_dict(_definition)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, PermissionsBody]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = PermissionsBody.from_dict(_permissions)

        _properties = d.pop("properties", UNSET)
        properties: Union[Unset, NodeBodyCreateProperties]
        if isinstance(_properties, Unset):
            properties = UNSET
        else:
            properties = NodeBodyCreateProperties.from_dict(_properties)

        relative_path = d.pop("relativePath", UNSET)

        secondary_children = []
        _secondary_children = d.pop("secondaryChildren", UNSET)
        for secondary_children_item_data in _secondary_children or []:
            secondary_children_item = ChildAssociationBody.from_dict(secondary_children_item_data)

            secondary_children.append(secondary_children_item)

        targets = []
        _targets = d.pop("targets", UNSET)
        for targets_item_data in _targets or []:
            targets_item = AssociationBody.from_dict(targets_item_data)

            targets.append(targets_item)

        node_body_create = cls(
            name=name,
            node_type=node_type,
            aspect_names=aspect_names,
            association=association,
            definition=definition,
            permissions=permissions,
            properties=properties,
            relative_path=relative_path,
            secondary_children=secondary_children,
            targets=targets,
        )

        node_body_create.additional_properties = d
        return node_body_create

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
