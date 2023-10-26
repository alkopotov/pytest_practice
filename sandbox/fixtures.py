import pytest
from user_api import UsersClient
from users import DefaultUser
from builder import get_http_client


@pytest.fixture(scope='class')
def class_users_client() -> UsersClient:
    client = get_http_client()

    return UsersClient(client=client)


@pytest.fixture(scope='function')
def function_user(class_users_client: UsersClient) -> DefaultUser:
    user = class_users_client.create_user()
    yield user
