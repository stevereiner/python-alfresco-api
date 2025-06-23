from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.abstract_class_association import AbstractClassAssociation
    from ..models.model import Model
    from ..models.property_ import Property


T = TypeVar("T", bound="AbstractClass")


@_attrs_define
class AbstractClass:
    """
    Attributes:
        id (str):
        title (str):
        associations (Union[Unset, list['AbstractClassAssociation']]):
        description (Union[Unset, str]):
        included_in_supertype_query (Union[Unset, bool]):
        is_archive (Union[Unset, bool]):
        is_container (Union[Unset, bool]):
        mandatory_aspects (Union[Unset, list[str]]):
        model (Union[Unset, Model]):
        parent_id (Union[Unset, str]):
        properties (Union[Unset, list['Property']]):
    """

    id: str
    title: str
    associations: Union[Unset, list["AbstractClassAssociation"]] = UNSET
    description: Union[Unset, str] = UNSET
    included_in_supertype_query: Union[Unset, bool] = UNSET
    is_archive: Union[Unset, bool] = UNSET
    is_container: Union[Unset, bool] = UNSET
    mandatory_aspects: Union[Unset, list[str]] = UNSET
    model: Union[Unset, "Model"] = UNSET
    parent_id: Union[Unset, str] = UNSET
    properties: Union[Unset, list["Property"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        associations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.associations, Unset):
            associations = []
            for associations_item_data in self.associations:
                associations_item = associations_item_data.to_dict()
                associations.append(associations_item)

        description = self.description

        included_in_supertype_query = self.included_in_supertype_query

        is_archive = self.is_archive

        is_container = self.is_container

        mandatory_aspects: Union[Unset, list[str]] = UNSET
        if not isinstance(self.mandatory_aspects, Unset):
            mandatory_aspects = self.mandatory_aspects

        model: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.model, Unset):
            model = self.model.to_dict()

        parent_id = self.parent_id

        properties: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
            }
        )
        if associations is not UNSET:
            field_dict["associations"] = associations
        if description is not UNSET:
            field_dict["description"] = description
        if included_in_supertype_query is not UNSET:
            field_dict["includedInSupertypeQuery"] = included_in_supertype_query
        if is_archive is not UNSET:
            field_dict["isArchive"] = is_archive
        if is_container is not UNSET:
            field_dict["isContainer"] = is_container
        if mandatory_aspects is not UNSET:
            field_dict["mandatoryAspects"] = mandatory_aspects
        if model is not UNSET:
            field_dict["model"] = model
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if properties is not UNSET:
            field_dict["properties"] = properties

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.abstract_class_association import AbstractClassAssociation
        from ..models.model import Model
        from ..models.property_ import Property

        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        associations = []
        _associations = d.pop("associations", UNSET)
        for associations_item_data in _associations or []:
            associations_item = AbstractClassAssociation.from_dict(associations_item_data)

            associations.append(associations_item)

        description = d.pop("description", UNSET)

        included_in_supertype_query = d.pop("includedInSupertypeQuery", UNSET)

        is_archive = d.pop("isArchive", UNSET)

        is_container = d.pop("isContainer", UNSET)

        mandatory_aspects = cast(list[str], d.pop("mandatoryAspects", UNSET))

        _model = d.pop("model", UNSET)
        model: Union[Unset, Model]
        if isinstance(_model, Unset):
            model = UNSET
        else:
            model = Model.from_dict(_model)

        parent_id = d.pop("parentId", UNSET)

        properties = []
        _properties = d.pop("properties", UNSET)
        for properties_item_data in _properties or []:
            properties_item = Property.from_dict(properties_item_data)

            properties.append(properties_item)

        abstract_class = cls(
            id=id,
            title=title,
            associations=associations,
            description=description,
            included_in_supertype_query=included_in_supertype_query,
            is_archive=is_archive,
            is_container=is_container,
            mandatory_aspects=mandatory_aspects,
            model=model,
            parent_id=parent_id,
            properties=properties,
        )

        abstract_class.additional_properties = d
        return abstract_class

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
