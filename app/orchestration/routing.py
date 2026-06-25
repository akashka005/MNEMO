from enum import Enum

class RouteType(str, Enum):
    INGEST = "INGEST"
    RETRIEVE = "RETRIEVE"
    INSIGHT = "INSIGHT"
    DIALOGUE = "DIALOGUE"

class Router:
    @staticmethod
    def route(query: str):
        query = query.lower()
        if (
            "insight" in query or
            "summary" in query
        ):
            return RouteType.INSIGHT
        if (
            "find" in query or
            "search" in query
        ):
            return RouteType.RETRIEVE
        if (
            "remember" in query or
            "store" in query
        ):
            return RouteType.INGEST
        return RouteType.DIALOGUE