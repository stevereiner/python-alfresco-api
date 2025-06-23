from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RequestStats")


@_attrs_define
class RequestStats:
    """A list of stats request.

    Attributes:
        cardinality (Union[Unset, bool]): A statistical approximation of the number of distinct values Default: False.
        cardinality_accuracy (Union[Unset, float]): Number between 0.0 and 1.0 indicating how aggressively the algorithm
            should try to be accurate. Used with boolean cardinality flag. Default: 0.3.
        count_distinct (Union[Unset, bool]): The number of distinct values  (This can be very expensive to calculate)
            Default: False.
        count_values (Union[Unset, bool]): The number which have a value for this field Default: True.
        distinct_values (Union[Unset, bool]): The set of all distinct values for the field (This can be very expensive
            to calculate) Default: False.
        exclude_filters (Union[Unset, list[str]]): A list of filters to exclude
        field (Union[Unset, str]): The stats field
        label (Union[Unset, str]): A label to include for reference the stats field
        max_ (Union[Unset, bool]): The maximum value of the field Default: True.
        mean (Union[Unset, bool]): The average Default: True.
        min_ (Union[Unset, bool]): The minimum value of the field Default: True.
        missing (Union[Unset, bool]): The number which do not have a value for this field Default: True.
        percentiles (Union[Unset, list[float]]): A list of percentile values, e.g. "1,99,99.9"
        stddev (Union[Unset, bool]): Standard deviation Default: True.
        sum_ (Union[Unset, bool]): The sum of all values of the field Default: True.
        sum_of_squares (Union[Unset, bool]): Sum of all values squared Default: True.
    """

    cardinality: Union[Unset, bool] = False
    cardinality_accuracy: Union[Unset, float] = 0.3
    count_distinct: Union[Unset, bool] = False
    count_values: Union[Unset, bool] = True
    distinct_values: Union[Unset, bool] = False
    exclude_filters: Union[Unset, list[str]] = UNSET
    field: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    max_: Union[Unset, bool] = True
    mean: Union[Unset, bool] = True
    min_: Union[Unset, bool] = True
    missing: Union[Unset, bool] = True
    percentiles: Union[Unset, list[float]] = UNSET
    stddev: Union[Unset, bool] = True
    sum_: Union[Unset, bool] = True
    sum_of_squares: Union[Unset, bool] = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cardinality = self.cardinality

        cardinality_accuracy = self.cardinality_accuracy

        count_distinct = self.count_distinct

        count_values = self.count_values

        distinct_values = self.distinct_values

        exclude_filters: Union[Unset, list[str]] = UNSET
        if not isinstance(self.exclude_filters, Unset):
            exclude_filters = self.exclude_filters

        field = self.field

        label = self.label

        max_ = self.max_

        mean = self.mean

        min_ = self.min_

        missing = self.missing

        percentiles: Union[Unset, list[float]] = UNSET
        if not isinstance(self.percentiles, Unset):
            percentiles = self.percentiles

        stddev = self.stddev

        sum_ = self.sum_

        sum_of_squares = self.sum_of_squares

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cardinality is not UNSET:
            field_dict["cardinality"] = cardinality
        if cardinality_accuracy is not UNSET:
            field_dict["cardinalityAccuracy"] = cardinality_accuracy
        if count_distinct is not UNSET:
            field_dict["countDistinct"] = count_distinct
        if count_values is not UNSET:
            field_dict["countValues"] = count_values
        if distinct_values is not UNSET:
            field_dict["distinctValues"] = distinct_values
        if exclude_filters is not UNSET:
            field_dict["excludeFilters"] = exclude_filters
        if field is not UNSET:
            field_dict["field"] = field
        if label is not UNSET:
            field_dict["label"] = label
        if max_ is not UNSET:
            field_dict["max"] = max_
        if mean is not UNSET:
            field_dict["mean"] = mean
        if min_ is not UNSET:
            field_dict["min"] = min_
        if missing is not UNSET:
            field_dict["missing"] = missing
        if percentiles is not UNSET:
            field_dict["percentiles"] = percentiles
        if stddev is not UNSET:
            field_dict["stddev"] = stddev
        if sum_ is not UNSET:
            field_dict["sum"] = sum_
        if sum_of_squares is not UNSET:
            field_dict["sumOfSquares"] = sum_of_squares

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cardinality = d.pop("cardinality", UNSET)

        cardinality_accuracy = d.pop("cardinalityAccuracy", UNSET)

        count_distinct = d.pop("countDistinct", UNSET)

        count_values = d.pop("countValues", UNSET)

        distinct_values = d.pop("distinctValues", UNSET)

        exclude_filters = cast(list[str], d.pop("excludeFilters", UNSET))

        field = d.pop("field", UNSET)

        label = d.pop("label", UNSET)

        max_ = d.pop("max", UNSET)

        mean = d.pop("mean", UNSET)

        min_ = d.pop("min", UNSET)

        missing = d.pop("missing", UNSET)

        percentiles = cast(list[float], d.pop("percentiles", UNSET))

        stddev = d.pop("stddev", UNSET)

        sum_ = d.pop("sum", UNSET)

        sum_of_squares = d.pop("sumOfSquares", UNSET)

        request_stats = cls(
            cardinality=cardinality,
            cardinality_accuracy=cardinality_accuracy,
            count_distinct=count_distinct,
            count_values=count_values,
            distinct_values=distinct_values,
            exclude_filters=exclude_filters,
            field=field,
            label=label,
            max_=max_,
            mean=mean,
            min_=min_,
            missing=missing,
            percentiles=percentiles,
            stddev=stddev,
            sum_=sum_,
            sum_of_squares=sum_of_squares,
        )

        request_stats.additional_properties = d
        return request_stats

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
