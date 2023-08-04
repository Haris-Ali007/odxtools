# SPDX-License-Identifier: MIT
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Dict, List, Optional
from xml.etree import ElementTree

from .exceptions import odxrequire
from .odxlink import OdxDocFragment, OdxLinkDatabase, OdxLinkId
from .utils import create_description_from_et

if TYPE_CHECKING:
    from .diaglayer import DiagLayer


@dataclass
class TeamMember:
    odx_id: OdxLinkId
    short_name: str
    long_name: Optional[str]
    description: Optional[str]
    roles: List[str]
    department: Optional[str]
    address: Optional[str]
    zip: Optional[str]
    city: Optional[str]
    phone: Optional[str]
    fax: Optional[str]
    email: Optional[str]

    @staticmethod
    def from_et(et_element: ElementTree.Element, doc_frags: List[OdxDocFragment]) -> "TeamMember":
        odx_id = odxrequire(OdxLinkId.from_et(et_element, doc_frags))
        short_name = odxrequire(et_element.findtext("SHORT-NAME"))
        long_name = et_element.findtext("LONG-NAME")
        description = create_description_from_et(et_element.find("DESC"))

        roles = [odxrequire(role_elem.text) for role_elem in et_element.iterfind("ROLES/ROLE")]

        department = et_element.findtext("DEPARTMENT")
        address = et_element.findtext("ADDRESS")
        zip = et_element.findtext("ZIP")
        city = et_element.findtext("CITY")
        phone = et_element.findtext("PHONE")
        fax = et_element.findtext("FAX")
        email = et_element.findtext("EMAIL")

        return TeamMember(
            odx_id=odx_id,
            short_name=short_name,
            long_name=long_name,
            description=description,
            roles=roles,
            department=department,
            address=address,
            zip=zip,
            city=city,
            phone=phone,
            fax=fax,
            email=email,
        )

    def _build_odxlinks(self) -> Dict[OdxLinkId, Any]:
        result = {self.odx_id: self}

        return result

    def _resolve_odxlinks(self, odxlinks: OdxLinkDatabase) -> None:
        pass

    def _resolve_snrefs(self, diag_layer: "DiagLayer") -> None:
        pass
