import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Author(sdRDM.DataModel):

    """This is another object that represents the author of the dataset. Please note, that the options here contain all required fields but also custom ones. In this example, the ```Dataverse``` option specifies where each field should be mapped, when exported to a Dataverse format. Hence, these options allow you to link your dataset towards any other data model without writing code by yourself."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("authorINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Full name including given and family name",
        dataverse="pyDaRUS.Citation.author.name",
    )

    affiliation: Optional[str] = Field(
        default=None,
        description="To which organization the author is affiliated to",
        dataverse="pyDaRUS.Citation.author.affiliation",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/sdrdm-template.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="eb358c3b18505f376431248b5e0fba84f6b802ce"
    )
