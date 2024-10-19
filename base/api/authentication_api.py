from httpx import Response, BasicAuth
from models.authentication import AuthUser
from utils.clients.http.client import APIClient
from utils.constants.routes import APIRoutes


class AuthenticationClient(APIClient):
    def get_auth_token_api(self, auth: AuthUser) -> Response:
        """
        Выполняет запрос на получение токена через BasicAuth.
        """
        return self.client.get(f'{APIRoutes.AUTH_TOKEN}', auth=BasicAuth(auth.email, auth.password))

    def get_auth_token(self, auth: AuthUser) -> str:
        """
        Получает токен из ответа API.
        """
        # Отправляем запрос для получения токена
        response = self.get_auth_token_api(auth)
        
        # Проверяем успешность запроса
        if response.status_code == 200:
            # Предполагаем, что токен возвращается в теле ответа в виде текста
            return response.text.strip()  # Убираем лишние пробелы/символы новой строки
        else:
            raise ValueError(f"Failed to get token, status code: {response.status_code}, response: {response.text}")
