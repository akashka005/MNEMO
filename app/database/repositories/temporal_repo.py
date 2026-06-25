from app.database.postgres_client import (
    postgres_client
)

class TemporalRepo:
    @staticmethod
    def save(
        content,
        timestamp
    ):
        postgres_client.execute(
            """
            INSERT INTO temporal_memory(
                content,
                timestamp
            )
            VALUES(?,?)
            """,
            (
                content,
                timestamp
            )
        )