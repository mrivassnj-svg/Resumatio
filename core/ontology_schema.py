from enum import Enum
from typing import TypedDict, List

class EntityType(Enum):
    IDENTITY = "identity"
    SKILL = "skill"
    EXPERIENCE = "experience"
    EDUCATION = "education"

class Relationship(Enum):
    PROFICIENT_IN = "proficient_in"
    EMPLOYED_AS = "employed_as"
    CONTRIBUTED_TO = "contributed_to"

class OntologySchema:
    """Defines the structure for the Resolution Engine."""
    SCHEMA_VERSION = "2.0.0"
    
    COMPONENTS = {
        EntityType.SKILL: ["id", "name", "category", "years"],
        EntityType.EXPERIENCE: ["organization", "role", "duration", "impact"],
    }
