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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class BatteryDto(BaseModel):
    """
    BatteryDto
    """ # noqa: E501
    depth_of_discharge: Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="x in (0,1), Units: [-]", alias="depthOfDischarge")
    id: Optional[StrictStr] = None
    initial_charge: Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="x in (0,1], Units: [-]", alias="initialCharge")
    minimum_charge_for_firing: Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]] = Field(description="x in (0,1), Units: [-]", alias="minimumChargeForFiring")
    nominal_capacity: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="Units: [Wh]", alias="nominalCapacity")
    __properties: ClassVar[List[str]] = ["depthOfDischarge", "id", "initialCharge", "minimumChargeForFiring", "nominalCapacity"]

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
        """Create an instance of BatteryDto from a JSON string"""
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
        """Create an instance of BatteryDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "depthOfDischarge": obj.get("depthOfDischarge"),
            "id": obj.get("id"),
            "initialCharge": obj.get("initialCharge"),
            "minimumChargeForFiring": obj.get("minimumChargeForFiring"),
            "nominalCapacity": obj.get("nominalCapacity")
        })
        return _obj


