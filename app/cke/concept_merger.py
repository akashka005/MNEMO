from collections import defaultdict

class ConceptMerger:
    @staticmethod
    def merge(concepts):
        groups = defaultdict(list)
        for concept in concepts:
            key = (
                concept.lower()
                .replace("-", "")
                .replace(" ", "")
            )
            groups[key].append(concept)
        merged = {}
        for _, values in groups.items():
            canonical = max(
                values,
                key=len
            )
            merged[canonical] = values
        return merged