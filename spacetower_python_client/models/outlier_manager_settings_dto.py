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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class OutlierManagerSettingsDto(BaseModel):
    """
    OutlierManagerSettingsDto
    """ # noqa: E501
    max_number_of_consecutive_outliers: Optional[StrictInt] = Field(default=None, description="Maximum number of consecutive outliers", alias="maxNumberOfConsecutiveOutliers")
    outlier_max_scale: Union[StrictFloat, StrictInt] = Field(description="Number of standard deviations for outlier detection", alias="outlierMaxScale")
    outlier_warmup_iterations: StrictInt = Field(description="Number of warmup iterations or number of measurement without outlier rejection", alias="outlierWarmupIterations")
    __properties: ClassVar[List[str]] = ["maxNumberOfConsecutiveOutliers", "outlierMaxScale", "outlierWarmupIterations"]

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
        """Create an instance of OutlierManagerSettingsDto from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OutlierManagerSettingsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxNumberOfConsecutiveOutliers": obj.get("maxNumberOfConsecutiveOutliers"),
            "outlierMaxScale": obj.get("outlierMaxScale"),
            "outlierWarmupIterations": obj.get("outlierWarmupIterations")
        })
        return _obj


