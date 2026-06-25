class GraphRefiner:
    @staticmethod
    def refine(nodes):
        unique = {}
        for node in nodes:
            text = (
                node["text"]
                .strip()
                .lower()
            )
            if text not in unique:
                unique[text] = node
        return list(
            unique.values()
        )