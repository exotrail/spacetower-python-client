# coding: utf-8

"""
    FDS API

    API for Flight Dynamics System

    The version of the OpenAPI document: 1.0.0
    Contact: contact@exotrail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class FiringActionDto(BaseModel):
    """
    FiringActionDto
    """ # noqa: E501
    firing_attitude: StrictStr = Field(alias="firingAttitude")
    firing_duration: Union[StrictFloat, StrictInt] = Field(description="Units: [s]", alias="firingDuration")
    id: Optional[StrictStr] = None
    post_firing_attitude: StrictStr = Field(alias="postFiringAttitude")
    start_firing: StrictStr = Field(description="UTC date", alias="startFiring")
    warm_up_attitude: Optional[StrictStr] = Field(default=None, alias="warmUpAttitude")
    warm_up_duration: Union[StrictFloat, StrictInt] = Field(description="Units: [s]", alias="warmUpDuration")
    __properties: ClassVar[List[str]] = ["firingAttitude", "firingDuration", "id", "postFiringAttitude", "startFiring", "warmUpAttitude", "warmUpDuration"]

    @field_validator('firing_attitude')
    def firing_attitude_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PROGRADE', 'RETROGRADE', 'NORMAL', 'ANTI_NORMAL', 'RADIAL', 'ANTI_RADIAL', 'QUATERNION', 'NONE', 'SUN_POINTING', 'TELECOM', 'PAYLOAD', 'TRANSITIONAL', 'LOF_ALIGNED_LVLH_CCSDS', 'RETROGRADE_NADIR']):
            raise ValueError("must be one of enum values ('PROGRADE', 'RETROGRADE', 'NORMAL', 'ANTI_NORMAL', 'RADIAL', 'ANTI_RADIAL', 'QUATERNION', 'NONE', 'SUN_POINTING', 'TELECOM', 'PAYLOAD', 'TRANSITIONAL', 'LOF_ALIGNED_LVLH_CCSDS', 'RETROGRADE_NADIR')")
        return value

    @field_validator('post_firing_attitude')
    def post_firing_attitude_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PROGRADE', 'RETROGRADE', 'NORMAL', 'ANTI_NORMAL', 'RADIAL', 'ANTI_RADIAL', 'QUATERNION', 'NONE', 'SUN_POINTING', 'TELECOM', 'PAYLOAD', 'TRANSITIONAL', 'LOF_ALIGNED_LVLH_CCSDS', 'RETROGRADE_NADIR']):
            raise ValueError("must be one of enum values ('PROGRADE', 'RETROGRADE', 'NORMAL', 'ANTI_NORMAL', 'RADIAL', 'ANTI_RADIAL', 'QUATERNION', 'NONE', 'SUN_POINTING', 'TELECOM', 'PAYLOAD', 'TRANSITIONAL', 'LOF_ALIGNED_LVLH_CCSDS', 'RETROGRADE_NADIR')")
        return value

    @field_validator('warm_up_attitude')
    def warm_up_attitude_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PROGRADE', 'RETROGRADE', 'NORMAL', 'ANTI_NORMAL', 'RADIAL', 'ANTI_RADIAL', 'QUATERNION', 'NONE', 'SUN_POINTING', 'TELECOM', 'PAYLOAD', 'TRANSITIONAL', 'LOF_ALIGNED_LVLH_CCSDS', 'RETROGRADE_NADIR']):
            raise ValueError("must be one of enum values ('PROGRADE', 'RETROGRADE', 'NORMAL', 'ANTI_NORMAL', 'RADIAL', 'ANTI_RADIAL', 'QUATERNION', 'NONE', 'SUN_POINTING', 'TELECOM', 'PAYLOAD', 'TRANSITIONAL', 'LOF_ALIGNED_LVLH_CCSDS', 'RETROGRADE_NADIR')")
        return value

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
        """Create an instance of FiringActionDto from a JSON string"""
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
        """Create an instance of FiringActionDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "firingAttitude": obj.get("firingAttitude"),
            "firingDuration": obj.get("firingDuration"),
            "id": obj.get("id"),
            "postFiringAttitude": obj.get("postFiringAttitude"),
            "startFiring": obj.get("startFiring"),
            "warmUpAttitude": obj.get("warmUpAttitude"),
            "warmUpDuration": obj.get("warmUpDuration")
        })
        return _obj


