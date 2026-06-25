import sqlite3
class PostgresClient:
    def __init__(
        self,
        db="menmo.db"
    ):
        self.conn = sqlite3.connect(
            db,
            check_same_thread=False
        )
    def execute(
        self,
        query,
        params=()
    ):
        cur = self.conn.cursor()
        cur.execute(
            query,
            params
        )
        self.conn.commit()
        return cur
postgres_client = (
    PostgresClient()
)