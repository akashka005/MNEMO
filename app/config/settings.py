from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    GROQ_API_KEY: str
    GROQ_MODEL: str = "llama-3.1-8b-instant"
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = "password"
    EMBED_MODEL: str = "BAAI/bge-small-en-v1.5"
    MERGE_THRESHOLD: float = 0.88
    EXTEND_THRESHOLD: float = 0.70
    CONFLICT_THRESHOLD: float = 0.72
    EMERGE_THRESHOLD: float = 0.50
    DECAY_DAYS: int = 30
    EMBED_DIMENSION: int = 384
    class Config:
        env_file = ".env"
settings = Settings()