class NoveltyGenerator:
    @staticmethod
    def generate(edges):
        novel_links = []
        for src1, dst1 in edges:
            for src2, dst2 in edges:
                if dst1 == src2:
                    candidate = (
                        src1,
                        dst2
                    )
                    if (
                        src1 != dst2
                        and candidate not in edges
                    ):
                        novel_links.append(
                            candidate
                        )
        return list(
            set(novel_links)
        )