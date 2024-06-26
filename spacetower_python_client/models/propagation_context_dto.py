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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PropagationContextDto(BaseModel):
    """
    PropagationContextDto
    """ # noqa: E501
    atmosphere_type: Optional[StrictStr] = Field(default=None, description="Required if perturbations include DRAG", alias="atmosphereType")
    earth_potential_deg: Optional[Annotated[int, Field(strict=True, ge=2)]] = Field(default=None, description="Required if perturbations include EARTH_POTENTIAL. Value must be earthPotentialDeg > 2. Units: [-]", alias="earthPotentialDeg")
    earth_potential_ord: Optional[StrictInt] = Field(default=None, description="Required if perturbations include EARTH_POTENTIAL. Value must be 0 <= earthPotentialOrd <= earthPotentialDeg. Units: [-]", alias="earthPotentialOrd")
    id: Optional[StrictStr] = None
    integrator_max_step: Optional[Union[Annotated[float, Field(le=86400.0, strict=True, ge=0.001)], Annotated[int, Field(le=86400, strict=True, ge=1)]]] = Field(default=100, description="Units: [s]. Default 100 s. Must be integratorMaxStep > integratorMinStep.", alias="integratorMaxStep")
    integrator_min_step: Optional[Union[Annotated[float, Field(le=86400.0, strict=True, ge=0.001)], Annotated[int, Field(le=86400, strict=True, ge=1)]]] = Field(default=0.01, description="Units: [s]. Default 0.01 s. Must be integratorMinStep > 0.001 s.", alias="integratorMinStep")
    integrator_type: Optional[StrictStr] = Field(default=None, alias="integratorType")
    perturbations: Optional[List[StrictStr]] = Field(default=None, description="Default to DORMAND_PRINCE_853.")
    solar_flux: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Required if perturbations include DRAG. Units: [sfu]", alias="solarFlux")
    __properties: ClassVar[List[str]] = ["atmosphereType", "earthPotentialDeg", "earthPotentialOrd", "id", "integratorMaxStep", "integratorMinStep", "integratorType", "perturbations", "solarFlux"]

    @field_validator('atmosphere_type')
    def atmosphere_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['HARRIS_PRIESTER', 'NRL_MSISE00']):
            raise ValueError("must be one of enum values ('HARRIS_PRIESTER', 'NRL_MSISE00')")
        return value

    @field_validator('integrator_type')
    def integrator_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DORMAND_PRINCE_853', 'DORMAND_PRINCE_54', 'ADAMS_MOULTON', 'RUNGE_KUTTA']):
            raise ValueError("must be one of enum values ('DORMAND_PRINCE_853', 'DORMAND_PRINCE_54', 'ADAMS_MOULTON', 'RUNGE_KUTTA')")
        return value

    @field_validator('perturbations')
    def perturbations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['EARTH_POTENTIAL', 'SRP', 'THIRD_BODY', 'DRAG', 'CONSTANT_THRUST', 'IMPULSIVE_THRUST']):
                raise ValueError("each list item must be one of ('EARTH_POTENTIAL', 'SRP', 'THIRD_BODY', 'DRAG', 'CONSTANT_THRUST', 'IMPULSIVE_THRUST')")
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
        """Create an instance of PropagationContextDto from a JSON string"""
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
        """Create an instance of PropagationContextDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "atmosphereType": obj.get("atmosphereType"),
            "earthPotentialDeg": obj.get("earthPotentialDeg"),
            "earthPotentialOrd": obj.get("earthPotentialOrd"),
            "id": obj.get("id"),
            "integratorMaxStep": obj.get("integratorMaxStep") if obj.get("integratorMaxStep") is not None else 100,
            "integratorMinStep": obj.get("integratorMinStep") if obj.get("integratorMinStep") is not None else 0.01,
            "integratorType": obj.get("integratorType"),
            "perturbations": obj.get("perturbations"),
            "solarFlux": obj.get("solarFlux")
        })
        return _obj


