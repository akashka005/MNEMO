class JudgeAgent:
    @staticmethod
    def decide(
        pro,
        con
    ):
        if len(pro) >= len(con):
            return "accepted"
        return "rejected"