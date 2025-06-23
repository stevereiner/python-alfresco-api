import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.person_network_subscription_level import PersonNetworkSubscriptionLevel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_quota import NetworkQuota


T = TypeVar("T", bound="PersonNetwork")


@_attrs_define
class PersonNetwork:
    """A network is the group of users and sites that belong to an organization.
    Networks are organized by email domain. When a user signs up for an
    Alfresco account , their email domain becomes their Home Network.

        Attributes:
            id (str): This network's unique id
            is_enabled (bool):
            created_at (Union[Unset, datetime.datetime]):
            home_network (Union[Unset, bool]): Is this the home network?
            paid_network (Union[Unset, bool]):
            quotas (Union[Unset, list['NetworkQuota']]):
            subscription_level (Union[Unset, PersonNetworkSubscriptionLevel]):
    """

    id: str
    is_enabled: bool
    created_at: Union[Unset, datetime.datetime] = UNSET
    home_network: Union[Unset, bool] = UNSET
    paid_network: Union[Unset, bool] = UNSET
    quotas: Union[Unset, list["NetworkQuota"]] = UNSET
    subscription_level: Union[Unset, PersonNetworkSubscriptionLevel] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        is_enabled = self.is_enabled

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        home_network = self.home_network

        paid_network = self.paid_network

        quotas: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.quotas, Unset):
            quotas = []
            for quotas_item_data in self.quotas:
                quotas_item = quotas_item_data.to_dict()
                quotas.append(quotas_item)

        subscription_level: Union[Unset, str] = UNSET
        if not isinstance(self.subscription_level, Unset):
            subscription_level = self.subscription_level.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "isEnabled": is_enabled,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if home_network is not UNSET:
            field_dict["homeNetwork"] = home_network
        if paid_network is not UNSET:
            field_dict["paidNetwork"] = paid_network
        if quotas is not UNSET:
            field_dict["quotas"] = quotas
        if subscription_level is not UNSET:
            field_dict["subscriptionLevel"] = subscription_level

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_quota import NetworkQuota

        d = dict(src_dict)
        id = d.pop("id")

        is_enabled = d.pop("isEnabled")

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        home_network = d.pop("homeNetwork", UNSET)

        paid_network = d.pop("paidNetwork", UNSET)

        quotas = []
        _quotas = d.pop("quotas", UNSET)
        for quotas_item_data in _quotas or []:
            quotas_item = NetworkQuota.from_dict(quotas_item_data)

            quotas.append(quotas_item)

        _subscription_level = d.pop("subscriptionLevel", UNSET)
        subscription_level: Union[Unset, PersonNetworkSubscriptionLevel]
        if isinstance(_subscription_level, Unset):
            subscription_level = UNSET
        else:
            subscription_level = PersonNetworkSubscriptionLevel(_subscription_level)

        person_network = cls(
            id=id,
            is_enabled=is_enabled,
            created_at=created_at,
            home_network=home_network,
            paid_network=paid_network,
            quotas=quotas,
            subscription_level=subscription_level,
        )

        person_network.additional_properties = d
        return person_network

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
