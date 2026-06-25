import json

class ContradictionAccuracy:

    @staticmethod
    def evaluate(
        dataset_path: str
    ):
        with open(
            dataset_path,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        total = len(data)

        if total == 0:
            return 0.0

        correct = 0

        for item in data:

            a = (
                item["statement_a"]
                .lower()
            )

            b = (
                item["statement_b"]
                .lower()
            )

            expected = (
                item["contradiction"]
            )

            predicted = (
                "not" in b
            )

            if predicted == expected:
                correct += 1

        return correct / total