import re


class TextUtils:

    @staticmethod
    def clean(text: str) -> str:

        text = text.strip()

        text = re.sub(
            r"\s+",
            " ",
            text
        )

        return text

    @staticmethod
    def word_count(
        text: str
    ) -> int:

        return len(
            text.split()
        )

    @staticmethod
    def sentence_count(
        text: str
    ) -> int:

        sentences = re.split(
            r"[.!?]+",
            text
        )

        return len(
            [
                s
                for s in sentences
                if s.strip()
            ]
        )