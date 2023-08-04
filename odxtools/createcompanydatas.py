# SPDX-License-Identifier: MIT
from typing import List

from .companydata import CompanyData
from .nameditemlist import NamedItemList
from .odxlink import OdxDocFragment
from .utils import short_name_as_id


def create_company_datas_from_et(et_element,
                                 doc_frags: List[OdxDocFragment]) -> NamedItemList[CompanyData]:
    if et_element is None:
        return NamedItemList(short_name_as_id)

    return NamedItemList(
        short_name_as_id,
        [
            CompanyData.from_et(cd_elem, doc_frags)
            for cd_elem in et_element.iterfind("COMPANY-DATA")
        ],
    )
