from models.authentication import Authentication
from utils.clients.http.client import HTTPClient
from base.api.authentication_api import AuthenticationClient
from settings import base_settings
from httpx import BasicAuth

# вариант с токеном 
def get_http_client_with_token(
    auth: Authentication | None = None,
    base_url: str = base_settings.api_url
) -> HTTPClient:
    if auth is None:
        return HTTPClient(base_url=base_url, trust_env=True)

    headers: dict[str, str] = {}
    client = HTTPClient(base_url=base_settings.api_url)
    authentication_client = AuthenticationClient(client=client)

    # Если токен не указан, получаем его с помощью данных пользователя
    if (not auth.auth_token) and auth.user:
        token = authentication_client.get_auth_token(auth.user)
        headers = {**headers, 'X-TC-CSRF-Token': token}

    # Если указан токен, используем его
    if auth.auth_token:
        headers = {**headers, 'X-TC-CSRF-Token': token}

    return HTTPClient(base_url=base_url, headers=headers, trust_env=True)



# вариант без использования токена , 
# почему то не хочет работать тим сити с токеном ...
def get_http_client_with_auth(
    auth: Authentication | None = None,
    base_url: str = base_settings.api_url
) -> HTTPClient:
    if auth is None:
        return HTTPClient(base_url=base_url, trust_env=True)

    # Создаем клиента с авторизацией
    return HTTPClient(
        base_url=base_url, 
        trust_env=True,
        auth=BasicAuth(auth.user.email, auth.user.password)  # Передаем авторизацию корректно
    )


