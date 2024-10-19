# from utils.clients.http.client import APIClient , HTTPClient
# from httpx import Client, Response , BasicAuth

# # Пример использования APIClient и HTTPClient для выполнения GET-запроса

# # Инициализация клиента
# client = HTTPClient()

# # Создание экземпляра APIClient
# api_client = APIClient(HTTPClient())

# # Выполнение GET-запроса
# response = api_client.client.get(url = "http://localhost:8111/authenticationTest.html?csrf", auth=BasicAuth('admin','admin1'))

# # Вывод статуса и данных ответа
# print(f"Status code: {response.status_code}")
# print(f"Response body: {response.text}")



from models.authentication import Authentication
from utils.clients.http.bilder import get_http_client_with_auth



# Получение  и настройка HTTP-клиента
http_client = get_http_client_with_auth(auth=Authentication())

# Теперь вы можете использовать http_client для авторизованных запросов
response = http_client.get("http://localhost:8111/app/tabs?editBuildTypeId=a223")

print(f"Status code: {response.status_code}")
print(f"Response body: {response.text}")
print('new commit')



