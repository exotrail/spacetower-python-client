# PropagationContextDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atmosphere_type** | **str** | Required if perturbations include DRAG | [optional] 
**earth_potential_deg** | **int** | Required if perturbations include EARTH_POTENTIAL. Value must be earthPotentialDeg &gt; 2. Units: [-] | [optional] 
**earth_potential_ord** | **int** | Required if perturbations include EARTH_POTENTIAL. Value must be 0 &lt;&#x3D; earthPotentialOrd &lt;&#x3D; earthPotentialDeg. Units: [-] | [optional] 
**id** | **str** |  | [optional] 
**integrator_max_step** | **float** | Units: [s]. Default 100 s. Must be integratorMaxStep &gt; integratorMinStep. | [optional] [default to 100]
**integrator_min_step** | **float** | Units: [s]. Default 0.01 s. Must be integratorMinStep &gt; 0.001 s. | [optional] [default to 0.01]
**integrator_type** | **str** |  | [optional] 
**perturbations** | **List[str]** | Default to DORMAND_PRINCE_853. | [optional] 
**solar_flux** | **float** | Required if perturbations include DRAG. Units: [sfu] | [optional] 

## Example

```python
from spacetower_python_client.models.propagation_context_dto import PropagationContextDto

# TODO update the JSON string below
json = "{}"
# create an instance of PropagationContextDto from a JSON string
propagation_context_dto_instance = PropagationContextDto.from_json(json)
# print the JSON string representation of the object
print(PropagationContextDto.to_json())

# convert the object into a dict
propagation_context_dto_dict = propagation_context_dto_instance.to_dict()
# create an instance of PropagationContextDto from a dict
propagation_context_dto_from_dict = PropagationContextDto.from_dict(propagation_context_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


