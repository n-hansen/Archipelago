import itertools
import json
import math
import pkgutil
from typing import Dict, Iterable, NamedTuple, Optional

from BaseClasses import Location

from . import Options, Quests


class CoQLocation(Location):
    game: str = "Caves of Qud"


class CoQLocationData(NamedTuple):
    name: str
    region: str
    min_level: int
    type: str


location_data = pkgutil.get_data(__name__, "data/Locations.json")
assert location_data is not None
static_locations: Dict[str, CoQLocationData] = {
    name: CoQLocationData(
        name=name,
        region=loc["region"] if "region" in loc else "Joppa",
        min_level=loc["minLevel"] if "minLevel" in loc else 1,
        type=loc["type"],
    )
    for name, loc in json.loads(location_data).items()
}

def xp_location_name(lvl: int, step: int):
    return f"Level {lvl}.{step}"

def xp_locations(frm: int, to: int, per_level: int) -> Iterable[str]:
    assert frm >= 1
    assert to <= Options.MAX_MAX_LEVEL
    assert per_level <= Options.MAX_LOCATIONS_PER_LEVEL

    for level in range(frm, to):
        for step in range(0, per_level):
            # We start at level 1.0, so skip first element
            if level == 1 and step == 0:
                continue
            yield xp_location_name(level,step)

def sultan_secret_locations(opts: Optional[Options.CoQOptions]) -> Iterable[tuple[str,int]]:
    req_secrets = opts.sultan_secrets_required if opts is not None else Options.MAX_SULTAN_SECRETS
    secrets_per_loc = opts.sultan_secrets_per_location if opts is not None else 1
    for i in range(1,req_secrets+1):
        if i%secrets_per_loc==0:
            yield (f"{i} Sultan Lore", math.ceil(i*4/5))
    req_secrets = opts.period_sultan_secrets_required if opts is not None else Options.MAX_SECRETS_PER_SULTANATE
    secrets_per_loc = opts.period_sultan_secrets_per_location if opts is not None else 1
    for p in ["First","Second","Third","Fourth","Fifth"]:
        yield (f"Lore from the {p} Sultanate", 4)
        for i in range(1,req_secrets+1):
            if i%secrets_per_loc==0:
                count = f"{i} " if i>1 else ""
                yield (f"{count}Lore from the {p} Sultanate", i*5-1)
    if opts is not None and opts.resheph_secrets_required>0:
        req_secrets = opts.resheph_secrets_required
        secrets_per_loc = opts.resheph_secrets_per_location
    elif opts is None:
        req_secrets = 16
    for i in range(1,req_secrets+1):
        if i%secrets_per_loc==0:
            yield (f"{i} Resheph Lore", i*5-1)


all_locations: Iterable[str] = itertools.chain(
    Quests.quest_locations.keys(),
    [name for name, data in static_locations.items()],
    xp_locations(1, Options.MAX_MAX_LEVEL, Options.MAX_LOCATIONS_PER_LEVEL),
    [name for name, _expected_lvl in sultan_secret_locations(None)],
)
