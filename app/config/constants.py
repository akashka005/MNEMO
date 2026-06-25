from enum import Enum

class NodeType(str, Enum):
    CONCEPT = "Concept"
    INSIGHT = "Insight"
    QUESTION = "Question"
    PAPER = "Paper"
    SOURCE = "Source"
class RelationType(str, Enum):
    SUPPORTS = "SUPPORTS"
    CONTRADICTS = "CONTRADICTS"
    EXTENDS = "EXTENDS"
    RELATES = "RELATES"
    EMERGES_FROM = "EMERGES_FROM"
class CKEOperation(str, Enum):
    MERGE = "MERGE"
    CONFLICT = "CONFLICT"
    EXTEND = "EXTEND"
    EMERGE = "EMERGE"
    NEW_NODE = "NEW_NODE"