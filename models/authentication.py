from pydantic import BaseModel, Field, model_validator

import sys
import os

# Добавляем корневую папку проекта в PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from settings import base_settings

class AuthUser(BaseModel):
    email: str = Field(default=base_settings.user.login)
    password: str = Field(default=base_settings.user.password)


class Authentication(BaseModel):
    auth_token: str | None = None
    user: AuthUser | None = AuthUser()

    @model_validator(mode='after')
    def validate_root(self) -> 'Authentication':
        if (not self.auth_token) and (not self.user):
            raise ValueError(
                'Please provide "username" and "password" or "auth_token"'
            )

        return self


