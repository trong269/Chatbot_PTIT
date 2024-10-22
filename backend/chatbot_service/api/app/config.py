from pydantic_settings import BaseSettings, SettingsConfigDict
import os



class Settings(BaseSettings):
    DATABASE_HOSTNAME : str
    DATABASE_PORT : str
    DATABASE_PASSWORD : str
    DATABASE_NAME : str
    DATABASE_USERNAME : str
    SECRET_KEY : str
    ALGORITHM : str
    ACCESS_TOKEN_EXPIRE_MINUTES : int

    # model_config = SettingsConfigDict(env_file=".env") 
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), '.env'))


    # class Config:
    #     env_file = ".env_var"
settings = Settings()