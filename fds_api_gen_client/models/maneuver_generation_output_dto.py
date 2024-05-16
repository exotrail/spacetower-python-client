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
from fds_api_gen_client.models.maneuver_strategy_dto import ManeuverStrategyDto
from fds_api_gen_client.models.orbital_state_dto import OrbitalStateDto
from typing import Optional, Set
from typing_extensions import Self

class ManeuverGenerationOutputDto(BaseModel):
    """
    ManeuverGenerationOutputDto
    """ # noqa: E501
    delta_eccentricity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="deltaEccentricity")
    delta_inclination: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="deltaInclination")
    delta_semi_major_axis: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="deltaSemiMajorAxis")
    id: Optional[StrictStr] = None
    initial_orbital_state: Optional[OrbitalStateDto] = Field(default=None, alias="initialOrbitalState")
    maximum_duration: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maximumDuration")
    quaternion_step: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="quaternionStep")
    required_output_orbital_states: Optional[StrictStr] = Field(default=None, alias="requiredOutputOrbitalStates")
    strategy: Optional[ManeuverStrategyDto] = None
    __properties: ClassVar[List[str]] = ["deltaEccentricity", "deltaInclination", "deltaSemiMajorAxis", "id", "initialOrbitalState", "maximumDuration", "quaternionStep", "requiredOutputOrbitalStates", "strategy"]

    @field_validator('required_output_orbital_states')
    def required_output_orbital_states_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ALL', 'LAST']):
            raise ValueError("must be one of enum values ('ALL', 'LAST')")
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
        """Create an instance of ManeuverGenerationOutputDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of initial_orbital_state
        if self.initial_orbital_state:
            _dict['initialOrbitalState'] = self.initial_orbital_state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of strategy
        if self.strategy:
            _dict['strategy'] = self.strategy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ManeuverGenerationOutputDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deltaEccentricity": obj.get("deltaEccentricity"),
            "deltaInclination": obj.get("deltaInclination"),
            "deltaSemiMajorAxis": obj.get("deltaSemiMajorAxis"),
            "id": obj.get("id"),
            "initialOrbitalState": OrbitalStateDto.from_dict(obj["initialOrbitalState"]) if obj.get("initialOrbitalState") is not None else None,
            "maximumDuration": obj.get("maximumDuration"),
            "quaternionStep": obj.get("quaternionStep"),
            "requiredOutputOrbitalStates": obj.get("requiredOutputOrbitalStates"),
            "strategy": ManeuverStrategyDto.from_dict(obj["strategy"]) if obj.get("strategy") is not None else None
        })
        return _obj


