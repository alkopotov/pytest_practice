import pytest
import asyncio
import allure

async def get_degree(base, degree):
    await asyncio.sleep(2)
    return base ** degree


@allure.story('Задача 2. Асинхронный тест функции, возвращающей промис с ожидаемым исключением')
@pytest.mark.asyncio
async def test_get_degree(event_loop):
    with pytest.raises(TypeError):
        result = await get_degree(25, 'abc')