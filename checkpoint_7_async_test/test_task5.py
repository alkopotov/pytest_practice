import pytest
import asyncio
import allure


async def run_in_loop(function, *args):
    task = asyncio.create_task(function(*args))
    return await task


async def get_abbreviation(name):
    await asyncio.sleep(3)
    return ''.join([e[0].upper() for e in (name.split())])


@allure.story('Задача 5. Асинхронный тест функции, запускающей другую функцию')
@pytest.mark.asyncio
async def test_run_in_loop():
    coro = run_in_loop(get_abbreviation, 'Копотов Алексей Владимирович')
    task = asyncio.create_task(coro)
    res = await task
    assert res == 'КАВ'
