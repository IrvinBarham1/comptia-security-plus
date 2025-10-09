from enum import Enum, unique;


@unique
class Category(Enum):
    TECHNICAL   = "Technical"
    MANAGERIAL  = "Managerial"  
    OPERATIONAL = "Operational"
    PHYSICAL    = "Physical"

@unique
class ControlType(Enum):
    PREVENTIVE    = "Preventive"
    DETERRENT     = "Deterrent"
    DETECTIVE     = "Detective"
    CORRECTIVE    = "Corrective"
    COMPENSATING  = "Compensating"
    DIRECTIVE     = "Directive"