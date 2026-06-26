from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    APP_NAME: str = "Blog API"
    DATABASE_URL: str = "sqlite:///./blog.db"

settings = Settings()