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
from spacetower_python_client.models.smoothed_keplerian_elements_dto import SmoothedKeplerianElementsDto
from typing import Optional, Set
from typing_extensions import Self

class FiringAnalysisDto(BaseModel):
    """
    FiringAnalysisDto
    """ # noqa: E501
    argument_of_perigee_delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="argumentOfPerigeeDelta")
    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    eccentricity_delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="eccentricityDelta")
    estimated_acceleration: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="estimatedAcceleration")
    estimated_thrust: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="estimatedThrust")
    estimated_thrust_tnw_direction: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="estimatedThrustTnwDirection")
    id: Optional[StrictStr] = None
    inclination_delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="inclinationDelta")
    raan_delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="raanDelta")
    semi_major_axis_delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="semiMajorAxisDelta")
    smoothed_keplerian_elements_after_firing: Optional[SmoothedKeplerianElementsDto] = Field(default=None, alias="smoothedKeplerianElementsAfterFiring")
    smoothed_keplerian_elements_before_firing: Optional[SmoothedKeplerianElementsDto] = Field(default=None, alias="smoothedKeplerianElementsBeforeFiring")
    status: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["argumentOfPerigeeDelta", "date", "eccentricityDelta", "estimatedAcceleration", "estimatedThrust", "estimatedThrustTnwDirection", "id", "inclinationDelta", "raanDelta", "semiMajorAxisDelta", "smoothedKeplerianElementsAfterFiring", "smoothedKeplerianElementsBeforeFiring", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PROCESSED', 'PENDING', 'FAILED']):
            raise ValueError("must be one of enum values ('PROCESSED', 'PENDING', 'FAILED')")
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
        """Create an instance of FiringAnalysisDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of smoothed_keplerian_elements_after_firing
        if self.smoothed_keplerian_elements_after_firing:
            _dict['smoothedKeplerianElementsAfterFiring'] = self.smoothed_keplerian_elements_after_firing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of smoothed_keplerian_elements_before_firing
        if self.smoothed_keplerian_elements_before_firing:
            _dict['smoothedKeplerianElementsBeforeFiring'] = self.smoothed_keplerian_elements_before_firing.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FiringAnalysisDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "argumentOfPerigeeDelta": obj.get("argumentOfPerigeeDelta"),
            "date": obj.get("date"),
            "eccentricityDelta": obj.get("eccentricityDelta"),
            "estimatedAcceleration": obj.get("estimatedAcceleration"),
            "estimatedThrust": obj.get("estimatedThrust"),
            "estimatedThrustTnwDirection": obj.get("estimatedThrustTnwDirection"),
            "id": obj.get("id"),
            "inclinationDelta": obj.get("inclinationDelta"),
            "raanDelta": obj.get("raanDelta"),
            "semiMajorAxisDelta": obj.get("semiMajorAxisDelta"),
            "smoothedKeplerianElementsAfterFiring": SmoothedKeplerianElementsDto.from_dict(obj["smoothedKeplerianElementsAfterFiring"]) if obj.get("smoothedKeplerianElementsAfterFiring") is not None else None,
            "smoothedKeplerianElementsBeforeFiring": SmoothedKeplerianElementsDto.from_dict(obj["smoothedKeplerianElementsBeforeFiring"]) if obj.get("smoothedKeplerianElementsBeforeFiring") is not None else None,
            "status": obj.get("status")
        })
        return _obj

