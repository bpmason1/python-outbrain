from enum import Enum


class BudgetType(Enum):
    CAMPAIGN = 'CAMPAIGN'
    MONTHLY = 'MONTHLY'
    DAILY = 'DAILY'


class PacingType(Enum):
    ASAP = 'SPEND_ASAP'
    AUTOMATIC = 'AUTOMATIC'
    DAILY = 'DAILY_TARGET'
