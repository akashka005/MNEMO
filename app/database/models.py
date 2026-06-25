from app.database.postgres_client import (
    postgres_client
)

def create_tables():
    postgres_client.execute(
        """
        CREATE TABLE IF NOT EXISTS episodic_memory(
            id INTEGER PRIMARY KEY,
            content TEXT
        )
        """
    )
    postgres_client.execute(
        """
        CREATE TABLE IF NOT EXISTS temporal_memory(
            id INTEGER PRIMARY KEY,
            content TEXT,
            timestamp TEXT
        )
        """
    )
    postgres_client.execute(
        """
        CREATE TABLE IF NOT EXISTS ingestions(
            id INTEGER PRIMARY KEY,
            source TEXT
        )
        """
    )
    postgres_client.execute(
        """
        CREATE TABLE IF NOT EXISTS insights(
            id INTEGER PRIMARY KEY,
            content TEXT
        )
        """
    )