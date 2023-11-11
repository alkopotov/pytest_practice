import asyncio
import pytest
import allure


async def get_abbreviation(name):
    await asyncio.sleep(2)
    return ''.join([e[0].upper() for e in (name.split())])


@allure.story('Задача 1. Асинхронный тест функции, возвращающей промис')
@pytest.mark.asyncio
async def test_get_abbreviation(event_loop):
    res = await get_abbreviation('Копотов Алексей Владимирович')
    assert res == 'КАВ'


