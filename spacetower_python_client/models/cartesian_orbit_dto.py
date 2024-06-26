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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CartesianOrbitDto(BaseModel):
    """
    CartesianOrbitDto
    """ # noqa: E501
    var_date: StrictStr = Field(description="UTC date", alias="date")
    frame: StrictStr
    id: Optional[StrictStr] = None
    position_x: Union[StrictFloat, StrictInt] = Field(description="Position X. Units: [km]", alias="positionX")
    position_y: Union[StrictFloat, StrictInt] = Field(description="Position Y. Units: [km]", alias="positionY")
    position_z: Union[StrictFloat, StrictInt] = Field(description="Position Z. Units: [km]", alias="positionZ")
    velocity_x: Union[StrictFloat, StrictInt] = Field(description="Velocity X. Units: [km/s]", alias="velocityX")
    velocity_y: Union[StrictFloat, StrictInt] = Field(description="Velocity Y. Units: [km/s]", alias="velocityY")
    velocity_z: Union[StrictFloat, StrictInt] = Field(description="Velocity Z. Units: [km/s]", alias="velocityZ")
    __properties: ClassVar[List[str]] = ["date", "frame", "id", "positionX", "positionY", "positionZ", "velocityX", "velocityY", "velocityZ"]

    @field_validator('frame')
    def frame_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['EME2000', 'ECI', 'TEME', 'GCRF', 'GTOD', 'ECF', 'TNW', 'QSW']):
            raise ValueError("must be one of enum values ('EME2000', 'ECI', 'TEME', 'GCRF', 'GTOD', 'ECF', 'TNW', 'QSW')")
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
        """Create an instance of CartesianOrbitDto from a JSON string"""
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
        """Create an instance of CartesianOrbitDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "frame": obj.get("frame"),
            "id": obj.get("id"),
            "positionX": obj.get("positionX"),
            "positionY": obj.get("positionY"),
            "positionZ": obj.get("positionZ"),
            "velocityX": obj.get("velocityX"),
            "velocityY": obj.get("velocityY"),
            "velocityZ": obj.get("velocityZ")
        })
        return _obj


