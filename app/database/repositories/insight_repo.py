from app.database.postgres_client import (
    postgres_client
)

class InsightRepo:
    @staticmethod
    def save(content):
        postgres_client.execute(
            """
            INSERT INTO insights(content)
            VALUES(?)
            """,
            (content,)
        )