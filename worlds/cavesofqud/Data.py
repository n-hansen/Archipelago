from dataclasses import dataclass
import json
import pkgutil
from typing import List


@dataclass
class HistoricSiteData:
    name: str
    visit_level: int
    explore_level: int
    region_name: str

_historic_site_data = pkgutil.get_data(__name__, "data/HistoricSites.json")
assert _historic_site_data is not None
historic_site_data: List[HistoricSiteData] = sorted([
    HistoricSiteData(s["name"], s["visit"], s["explore"], s["region"])
    for s in json.loads(_historic_site_data)
], key=lambda s: s.visit_level)
