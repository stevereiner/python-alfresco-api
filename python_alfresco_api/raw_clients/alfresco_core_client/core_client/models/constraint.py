from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constraint_parameters import ConstraintParameters


T = TypeVar("T", bound="Constraint")


@_attrs_define
class Constraint:
    """
    Attributes:
        id (str):
        description (Union[Unset, str]): the human-readable constraint description
        parameters (Union[Unset, ConstraintParameters]):
        title (Union[Unset, str]): the human-readable constraint title
        type_ (Union[Unset, str]): the type of the constraint
    """

    id: str
    description: Union[Unset, str] = UNSET
    parameters: Union[Unset, "ConstraintParameters"] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        parameters: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        title = self.title

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraint_parameters import ConstraintParameters

        d = dict(src_dict)
        id = d.pop("id")

        description = d.pop("description", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, ConstraintParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ConstraintParameters.from_dict(_parameters)

        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        constraint = cls(
            id=id,
            description=description,
            parameters=parameters,
            title=title,
            type_=type_,
        )

        constraint.additional_properties = d
        return constraint

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
