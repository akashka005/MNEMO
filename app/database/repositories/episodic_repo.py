from app.database.postgres_client import (
    postgres_client
)

class EpisodicRepo:
    @staticmethod
    def save(content):
        postgres_client.execute(
            """
            INSERT INTO episodic_memory(content)
            VALUES(?)
            """,
            (content,)
        )