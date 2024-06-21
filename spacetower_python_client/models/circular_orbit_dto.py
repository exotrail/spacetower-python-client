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

class CircularOrbitDto(BaseModel):
    """
    CircularOrbitDto
    """ # noqa: E501
    argument_of_latitude: Union[StrictFloat, StrictInt] = Field(description="Units: [deg]", alias="argumentOfLatitude")
    var_date: StrictStr = Field(description="UTC date", alias="date")
    eccentricity_vector_x: Union[StrictFloat, StrictInt] = Field(description="Eccentricity vector X. Units: [-]", alias="eccentricityVectorX")
    eccentricity_vector_y: Union[StrictFloat, StrictInt] = Field(description="Eccentricity vector Y. Units: [-]", alias="eccentricityVectorY")
    frame: StrictStr
    id: Optional[StrictStr] = None
    inclination: Union[StrictFloat, StrictInt] = Field(description="Units: [deg]")
    mean_osc_type: StrictStr = Field(alias="meanOscType")
    position_angle_type: StrictStr = Field(alias="positionAngleType")
    raan: Union[StrictFloat, StrictInt] = Field(description="Units: [deg]")
    semi_major_axis: Union[StrictFloat, StrictInt] = Field(description="Units: [km]", alias="semiMajorAxis")
    __properties: ClassVar[List[str]] = ["argumentOfLatitude", "date", "eccentricityVectorX", "eccentricityVectorY", "frame", "id", "inclination", "meanOscType", "positionAngleType", "raan", "semiMajorAxis"]

    @field_validator('frame')
    def frame_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['EME2000', 'ECI', 'TEME', 'GCRF', 'GTOD', 'ECF', 'TNW', 'QSW']):
            raise ValueError("must be one of enum values ('EME2000', 'ECI', 'TEME', 'GCRF', 'GTOD', 'ECF', 'TNW', 'QSW')")
        return value

    @field_validator('mean_osc_type')
    def mean_osc_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MEAN', 'OSC']):
            raise ValueError("must be one of enum values ('MEAN', 'OSC')")
        return value

    @field_validator('position_angle_type')
    def position_angle_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['TRUE', 'MEAN', 'ECCENTRIC']):
            raise ValueError("must be one of enum values ('TRUE', 'MEAN', 'ECCENTRIC')")
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
        """Create an instance of CircularOrbitDto from a JSON string"""
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
        """Create an instance of CircularOrbitDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "argumentOfLatitude": obj.get("argumentOfLatitude"),
            "date": obj.get("date"),
            "eccentricityVectorX": obj.get("eccentricityVectorX"),
            "eccentricityVectorY": obj.get("eccentricityVectorY"),
            "frame": obj.get("frame"),
            "id": obj.get("id"),
            "inclination": obj.get("inclination"),
            "meanOscType": obj.get("meanOscType"),
            "positionAngleType": obj.get("positionAngleType"),
            "raan": obj.get("raan"),
            "semiMajorAxis": obj.get("semiMajorAxis")
        })
        return _obj


