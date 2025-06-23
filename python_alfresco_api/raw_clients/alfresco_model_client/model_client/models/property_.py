from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constraint import Constraint


T = TypeVar("T", bound="Property")


@_attrs_define
class Property:
    """
    Attributes:
        id (str):
        constraints (Union[Unset, list['Constraint']]): list of constraints defined for the property
        data_type (Union[Unset, str]): the name of the property type (e.g. d:text)
        default_value (Union[Unset, str]): the default value
        description (Union[Unset, str]): the human-readable description
        is_mandatory (Union[Unset, bool]): define if the property is mandatory
        is_mandatory_enforced (Union[Unset, bool]): define if the presence of mandatory properties is enforced
        is_multi_valued (Union[Unset, bool]): define if the property is multi-valued
        is_protected (Union[Unset, bool]): define if the property is system maintained
        title (Union[Unset, str]): the human-readable title
    """

    id: str
    constraints: Union[Unset, list["Constraint"]] = UNSET
    data_type: Union[Unset, str] = UNSET
    default_value: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_mandatory: Union[Unset, bool] = UNSET
    is_mandatory_enforced: Union[Unset, bool] = UNSET
    is_multi_valued: Union[Unset, bool] = UNSET
    is_protected: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        constraints: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.constraints, Unset):
            constraints = []
            for constraints_item_data in self.constraints:
                constraints_item = constraints_item_data.to_dict()
                constraints.append(constraints_item)

        data_type = self.data_type

        default_value = self.default_value

        description = self.description

        is_mandatory = self.is_mandatory

        is_mandatory_enforced = self.is_mandatory_enforced

        is_multi_valued = self.is_multi_valued

        is_protected = self.is_protected

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if constraints is not UNSET:
            field_dict["constraints"] = constraints
        if data_type is not UNSET:
            field_dict["dataType"] = data_type
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if description is not UNSET:
            field_dict["description"] = description
        if is_mandatory is not UNSET:
            field_dict["isMandatory"] = is_mandatory
        if is_mandatory_enforced is not UNSET:
            field_dict["isMandatoryEnforced"] = is_mandatory_enforced
        if is_multi_valued is not UNSET:
            field_dict["isMultiValued"] = is_multi_valued
        if is_protected is not UNSET:
            field_dict["isProtected"] = is_protected
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraint import Constraint

        d = dict(src_dict)
        id = d.pop("id")

        constraints = []
        _constraints = d.pop("constraints", UNSET)
        for constraints_item_data in _constraints or []:
            constraints_item = Constraint.from_dict(constraints_item_data)

            constraints.append(constraints_item)

        data_type = d.pop("dataType", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        description = d.pop("description", UNSET)

        is_mandatory = d.pop("isMandatory", UNSET)

        is_mandatory_enforced = d.pop("isMandatoryEnforced", UNSET)

        is_multi_valued = d.pop("isMultiValued", UNSET)

        is_protected = d.pop("isProtected", UNSET)

        title = d.pop("title", UNSET)

        property_ = cls(
            id=id,
            constraints=constraints,
            data_type=data_type,
            default_value=default_value,
            description=description,
            is_mandatory=is_mandatory,
            is_mandatory_enforced=is_mandatory_enforced,
            is_multi_valued=is_multi_valued,
            is_protected=is_protected,
            title=title,
        )

        property_.additional_properties = d
        return property_

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
