from pydantic_settings import SettingsConfigDict, BaseSettings


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    TG_BOT_API_TOKEN: str
    STRAPI_API_TOKEN: str
