from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.candidate_candidate_type import CandidateCandidateType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Candidate")


@_attrs_define
class Candidate:
    """A candidate item.

    Attributes:
        candidate_id (Union[Unset, str]):
        candidate_type (Union[Unset, CandidateCandidateType]):
    """

    candidate_id: Union[Unset, str] = UNSET
    candidate_type: Union[Unset, CandidateCandidateType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidate_id = self.candidate_id

        candidate_type: Union[Unset, str] = UNSET
        if not isinstance(self.candidate_type, Unset):
            candidate_type = self.candidate_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if candidate_id is not UNSET:
            field_dict["candidateId"] = candidate_id
        if candidate_type is not UNSET:
            field_dict["candidateType"] = candidate_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        candidate_id = d.pop("candidateId", UNSET)

        _candidate_type = d.pop("candidateType", UNSET)
        candidate_type: Union[Unset, CandidateCandidateType]
        if isinstance(_candidate_type, Unset):
            candidate_type = UNSET
        else:
            candidate_type = CandidateCandidateType(_candidate_type)

        candidate = cls(
            candidate_id=candidate_id,
            candidate_type=candidate_type,
        )

        candidate.additional_properties = d
        return candidate

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
