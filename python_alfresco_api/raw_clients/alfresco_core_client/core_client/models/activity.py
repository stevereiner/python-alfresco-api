import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.activity_activity_summary import ActivityActivitySummary


T = TypeVar("T", bound="Activity")


@_attrs_define
class Activity:
    """Activities describe any past activity in a site,
    for example creating an item of content, commenting on a node,
    liking an item of content.

        Attributes:
            activity_type (str): The type of the activity posted
            feed_person_id (str): The feed on which this activity was posted
            id (int): The unique id of the activity
            post_person_id (str): The id of the person who performed the activity
            activity_summary (Union[Unset, ActivityActivitySummary]): An object summarizing the activity
            posted_at (Union[Unset, datetime.datetime]): The date time at which the activity was performed
            site_id (Union[Unset, str]): The unique id of the site on which the activity was performed
    """

    activity_type: str
    feed_person_id: str
    id: int
    post_person_id: str
    activity_summary: Union[Unset, "ActivityActivitySummary"] = UNSET
    posted_at: Union[Unset, datetime.datetime] = UNSET
    site_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        activity_type = self.activity_type

        feed_person_id = self.feed_person_id

        id = self.id

        post_person_id = self.post_person_id

        activity_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.activity_summary, Unset):
            activity_summary = self.activity_summary.to_dict()

        posted_at: Union[Unset, str] = UNSET
        if not isinstance(self.posted_at, Unset):
            posted_at = self.posted_at.isoformat()

        site_id = self.site_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "activityType": activity_type,
                "feedPersonId": feed_person_id,
                "id": id,
                "postPersonId": post_person_id,
            }
        )
        if activity_summary is not UNSET:
            field_dict["activitySummary"] = activity_summary
        if posted_at is not UNSET:
            field_dict["postedAt"] = posted_at
        if site_id is not UNSET:
            field_dict["siteId"] = site_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.activity_activity_summary import ActivityActivitySummary

        d = dict(src_dict)
        activity_type = d.pop("activityType")

        feed_person_id = d.pop("feedPersonId")

        id = d.pop("id")

        post_person_id = d.pop("postPersonId")

        _activity_summary = d.pop("activitySummary", UNSET)
        activity_summary: Union[Unset, ActivityActivitySummary]
        if isinstance(_activity_summary, Unset):
            activity_summary = UNSET
        else:
            activity_summary = ActivityActivitySummary.from_dict(_activity_summary)

        _posted_at = d.pop("postedAt", UNSET)
        posted_at: Union[Unset, datetime.datetime]
        if isinstance(_posted_at, Unset):
            posted_at = UNSET
        else:
            posted_at = isoparse(_posted_at)

        site_id = d.pop("siteId", UNSET)

        activity = cls(
            activity_type=activity_type,
            feed_person_id=feed_person_id,
            id=id,
            post_person_id=post_person_id,
            activity_summary=activity_summary,
            posted_at=posted_at,
            site_id=site_id,
        )

        activity.additional_properties = d
        return activity

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
