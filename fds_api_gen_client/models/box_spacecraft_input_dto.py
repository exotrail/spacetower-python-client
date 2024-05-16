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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BoxSpacecraftInputDto(BaseModel):
    """
    BoxSpacecraftInputDto
    """ # noqa: E501
    battery_id: StrictStr = Field(alias="batteryId")
    drag_coefficient: Union[StrictFloat, StrictInt] = Field(description="Units: [-]", alias="dragCoefficient")
    id: Optional[StrictStr] = None
    max_angular_acceleration: Union[StrictFloat, StrictInt] = Field(description="Units: [deg/s²]", alias="maxAngularAcceleration")
    max_angular_velocity: Union[StrictFloat, StrictInt] = Field(description="Units: [deg/s]", alias="maxAngularVelocity")
    platform_mass: Union[StrictFloat, StrictInt] = Field(alias="platformMass")
    reflection_coefficient: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Units: [-]", alias="reflectionCoefficient")
    solar_array_id: StrictStr = Field(alias="solarArrayId")
    spacecraft_length_x: Union[StrictFloat, StrictInt] = Field(description="Units: [m]", alias="spacecraftLengthX")
    spacecraft_length_y: Union[StrictFloat, StrictInt] = Field(description="Units: [m]", alias="spacecraftLengthY")
    spacecraft_length_z: Union[StrictFloat, StrictInt] = Field(description="Units: [m]", alias="spacecraftLengthZ")
    thruster_id: StrictStr = Field(alias="thrusterId")
    __properties: ClassVar[List[str]] = ["batteryId", "dragCoefficient", "id", "maxAngularAcceleration", "maxAngularVelocity", "platformMass", "reflectionCoefficient", "solarArrayId", "spacecraftLengthX", "spacecraftLengthY", "spacecraftLengthZ", "thrusterId"]

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
        """Create an instance of BoxSpacecraftInputDto from a JSON string"""
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
        """Create an instance of BoxSpacecraftInputDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "batteryId": obj.get("batteryId"),
            "dragCoefficient": obj.get("dragCoefficient"),
            "id": obj.get("id"),
            "maxAngularAcceleration": obj.get("maxAngularAcceleration"),
            "maxAngularVelocity": obj.get("maxAngularVelocity"),
            "platformMass": obj.get("platformMass"),
            "reflectionCoefficient": obj.get("reflectionCoefficient"),
            "solarArrayId": obj.get("solarArrayId"),
            "spacecraftLengthX": obj.get("spacecraftLengthX"),
            "spacecraftLengthY": obj.get("spacecraftLengthY"),
            "spacecraftLengthZ": obj.get("spacecraftLengthZ"),
            "thrusterId": obj.get("thrusterId")
        })
        return _obj


