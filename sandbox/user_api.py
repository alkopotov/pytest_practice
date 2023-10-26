import allure
from httpx import Response

from users import DefaultUser
from client import APIClient
from routes import APIRoutes


class UsersClient(APIClient):
    @allure.step('Creating user')
    def create_user_api(self, payload: DefaultUser) -> Response:
        return self.client.post(APIRoutes.USER, json=payload.model_dump(by_alias=True))

    @allure.step('Getting user by user name')
    def get_user_api(self, payload: str) -> Response:
        return self.client.get(
            f'{APIRoutes.USER}{payload}'
        )

    def create_user(self) -> DefaultUser:
        payload = DefaultUser()
        response = self.create_user_api(payload)
        return DefaultUser(**response.json())

