from app.database.postgres_client import (
    postgres_client
)

class IngestionRepo:
    @staticmethod
    def save(source):
        postgres_client.execute(
            """
            INSERT INTO ingestions(source)
            VALUES(?)
            """,
            (source,)
        )