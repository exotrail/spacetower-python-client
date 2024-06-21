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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class OrbitalEventsRequestDto(BaseModel):
    """
    OrbitalEventsRequestDto
    """ # noqa: E501
    events_type: List[StrictStr] = Field(alias="eventsType")
    id: Optional[StrictStr] = None
    start_date: Optional[StrictStr] = Field(default=None, description="UTC date", alias="startDate")
    __properties: ClassVar[List[str]] = ["eventsType", "id", "startDate"]

    @field_validator('events_type')
    def events_type_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['NODE', 'ECLIPSE', 'ORBITAL_6AMPM', 'ORBITAL_NOON_MIDNIGHT', 'APSIDE']):
                raise ValueError("each list item must be one of ('NODE', 'ECLIPSE', 'ORBITAL_6AMPM', 'ORBITAL_NOON_MIDNIGHT', 'APSIDE')")
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
        """Create an instance of OrbitalEventsRequestDto from a JSON string"""
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
        """Create an instance of OrbitalEventsRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eventsType": obj.get("eventsType"),
            "id": obj.get("id"),
            "startDate": obj.get("startDate")
        })
        return _obj


