from app.debate.pro_agent import (
    ProAgent
)
from app.debate.con_agent import (
    ConAgent
)
from app.debate.judge_agent import (
    JudgeAgent
)

class DebateEngine:
    @staticmethod
    def debate(
        claim
    ):
        pro = (
            ProAgent.argue(
                claim
            )
        )
        con = (
            ConAgent.argue(
                claim
            )
        )
        verdict = (
            JudgeAgent.decide(
                pro,
                con
            )
        )
        return {
            "claim": claim,
            "pro_evidence": pro,
            "con_evidence": con,
            "verdict": verdict
        }