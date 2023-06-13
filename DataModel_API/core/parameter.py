import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


from .units import Units


@forge_signature
class Parameter(sdRDM.DataModel):

    """This is another object used to describe the parameters of given dataset. As a final note, it is important to use the description of an object to its fullest. As you might noticed, the space in between the object definition ```###``` can be freely used to describe what this object is actually about. Ultimately, this gives you the opportunity to ensure users completely understand what the intention and use case of this object is in a readable way."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("parameterINDEX"),
        xml="@id",
    )

    key: Optional[str] = Field(
        default=None,
        description="Name of the parameter",
        dataverse="pyDaRUS.Process.method_parameters.name",
    )

    value: Optional[float] = Field(
        default=None,
        description="Respective value of a parameter",
        dataverse="pyDaRUS.Process.method_parameters.value",
    )

    unit: Optional[Units] = Field(
        default=None,
        description="Unit of the parameter",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/sdrdm-template.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="eb358c3b18505f376431248b5e0fba84f6b802ce"
    )
