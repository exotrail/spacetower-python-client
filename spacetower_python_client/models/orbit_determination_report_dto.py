# coding: utf-8

"""
    FDS API

    API for Flight Dynamics System

    The version of the OpenAPI document: 1.1.0
    Contact: contact@exotrail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from spacetower_python_client.models.orbit_determination_residual_statistics_dto import OrbitDeterminationResidualStatisticsDto
from typing import Optional, Set
from typing_extensions import Self

class OrbitDeterminationReportDto(BaseModel):
    """
    OrbitDeterminationReportDto
    """ # noqa: E501
    number_of_rejected_measurements: Optional[StrictInt] = Field(default=None, alias="numberOfRejectedMeasurements")
    number_of_used_measurements: Optional[StrictInt] = Field(default=None, alias="numberOfUsedMeasurements")
    residuals_statistics: Optional[List[OrbitDeterminationResidualStatisticsDto]] = Field(default=None, alias="residualsStatistics")
    __properties: ClassVar[List[str]] = ["numberOfRejectedMeasurements", "numberOfUsedMeasurements", "residualsStatistics"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrbitDeterminationReportDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in residuals_statistics (list)
        _items = []
        if self.residuals_statistics:
            for _item in self.residuals_statistics:
                if _item:
                    _items.append(_item.to_dict())
            _dict['residualsStatistics'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrbitDeterminationReportDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numberOfRejectedMeasurements": obj.get("numberOfRejectedMeasurements"),
            "numberOfUsedMeasurements": obj.get("numberOfUsedMeasurements"),
            "residualsStatistics": [OrbitDeterminationResidualStatisticsDto.from_dict(_item) for _item in obj["residualsStatistics"]] if obj.get("residualsStatistics") is not None else None
        })
        return _obj


