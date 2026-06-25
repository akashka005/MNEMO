from fastapi import APIRouter

router = APIRouter()
@router.get("/graph")
def graph():
    return {
        "graph":
        [
            {
                "source":
                "Transformer",

                "target":
                "Long Context"
            }
        ]
    }
@router.get("/hypotheses")
def hypotheses():
    return {
        "hypotheses":
        [
            {
                "text":
                "Sparse Attention may improve Long Context"
            }
        ]
    }
@router.get("/contradictions")
def contradictions():
    return {
        "contradictions":
        [
            {
                "a":
                "Attention",

                "b":
                "No Attention"
            }
        ]
    }
@router.get("/evolution")
def evolution():
    return {
        "timeline":
        [
            {
                "concept":
                "Transformer",

                "event":
                "evolved"
            }
        ]
    }