from dataclasses import dataclass

from Options import Choice, PerGameCommonOptions, Range, Toggle

MAX_MAX_LEVEL = 50
MAX_LOCATIONS_PER_LEVEL = 10
MAX_SECRETS_PER_SULTANATE = 10 # usually higher, but this is the minimum guaranteed
MAX_SULTAN_SECRETS = 5*MAX_SECRETS_PER_SULTANATE+16

class Goal(Choice):
    """
    Determines the win condition
    """

    display_name = "Goal"
    option_quest_weirdwire_conduit = 0
    option_quest_more_than_a_willing_spirit = 1
    option_quest_decoding_the_signal = 2
    option_quest_the_earl_of_omonporch = 3
    option_quest_a_call_to_arms = 4
    default = 2

class Genotype(Choice):
    """
    Sets whether your character receives Mutation Points and Rapid Mutations (Mutant),
    or License Points and Implants (True Kin).
    """
    display_name = "Genotype"
    option_mutant = 0
    option_true_kin = 1
    default = 0

class LocationsPerLevel(Range):
    """
    Determines the number of locations to check when gaining XP.
    Each level contains the number of locations chosen here,
    distributed across the XP range between current and next level.
    Including the level up itself.
    """

    display_name = "Extra locations per level"
    range_start = 4
    range_end = MAX_LOCATIONS_PER_LEVEL
    default = 5

class ExtraLocationLevels(Range):
    """
    Determines the number of extra levels with locations beyond the in-logic level for the final
    goal quest step (selected by the goal option). This also controls the extra amount of stat ups
    that are in the item pool.
    """

    display_name = "Extra levels beyond the final quest"
    range_start = 0
    range_end = 20
    default = 5

class SultanSecretsRequired(Range):
    """
    Determines the number of sultan secrets needed to be found.
    """

    display_name = "Number of sultan secrets needed"
    range_start = 0
    range_end = MAX_SULTAN_SECRETS
    default = 30

class SultanSecretsPerLocation(Range):
    """
    Determines how many secrets need to be found per location.
    """

    display_name = "Sultan secrets per location"
    range_start = 1
    range_end = MAX_SECRETS_PER_SULTANATE
    default = 5

class PeriodSultanSecretsRequired(Range):
    """
    Determines the number of sultan secrets needed to be found per period.
    """

    display_name = "Number of secrets needed per sultanate"
    range_start = 0
    range_end = MAX_SECRETS_PER_SULTANATE
    default = 1

class PeriodSultanSecretsPerLocation(Range):
    """
    Determines the number of period-specific sultan secrets needed to be found per location.
    """

    display_name = "Number of sultanate secrets per location"
    range_start = 1
    range_end = MAX_SECRETS_PER_SULTANATE
    default = 1

class ReshephSecretsRequired(Range):
    """
    Determines the number of Resheph secrets needed to be found.
    Setting to zero falls back to the per-period sultan lore setting.
    """

    display_name = "Number of Resheph secrets needed"
    range_start = 0
    range_end = 16
    default = 6

class ReshephSecretsPerLocation(Range):
    """
    Determines the number of Resheph secrets needed to be found per location.
    """

    display_name = "Number of Resheph secrets per location"
    range_start = 1
    range_end = 16
    default = 2

class TrapPercentage(Range):
    """
    Determines the percentage of filler items that are replaced by
    traps.
    """

    display_name = "Percentage of filler items replaced with traps"
    range_start = 0
    range_end = 100
    default = 50

class LostArtifacts(Toggle):
    """
    Adds some difficult-to-find named artifacts to the location pool, depending on max level.
    There are semi-reliable methods for locating them, but they require some luck and/or grind!
    """
    display_name = "Lost Artifacts"


@dataclass
class CoQOptions(PerGameCommonOptions):
    goal: Goal
    genotype: Genotype
    locations_per_level: LocationsPerLevel
    extra_location_levels: ExtraLocationLevels
    sultan_secrets_required: SultanSecretsRequired
    sultan_secrets_per_location: SultanSecretsPerLocation
    period_sultan_secrets_required: PeriodSultanSecretsRequired
    period_sultan_secrets_per_location: PeriodSultanSecretsPerLocation
    resheph_secrets_required: ReshephSecretsRequired
    resheph_secrets_per_location: ReshephSecretsPerLocation
    trap_percentage: TrapPercentage
    lost_artifacts: LostArtifacts
    # death_link: DeathLink
