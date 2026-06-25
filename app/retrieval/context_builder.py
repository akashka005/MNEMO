class ContextBuilder:

    @staticmethod
    def build(
        question: str,
        nodes: list
    ):

        context = ""

        for i, node in enumerate(nodes):

            context += (
                f"Node {i+1}:\n"
                f"{node['text']}\n\n"
            )

        return context