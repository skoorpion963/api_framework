from pydantic_settings import BaseSettings, SettingsConfigDict



class User(BaseSettings):
    login: str = ""
    password: str = ""


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    base_url: str
    user: User = User()

    @property
    def api_url(self) -> str:
        return f'{self.base_url}'


base_settings = Settings()

