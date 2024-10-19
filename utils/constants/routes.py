from enum import Enum
from settings import base_settings

class APIRoutes(str, Enum):
    AUTH_TOKEN = "/authenticationTest.html?csrf"
    
    def __str__(self) -> str:
        # Добавляем base_settings.api_url к каждому маршруту
        return f"{base_settings.api_url}{self.value}"