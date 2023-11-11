import aiohttp
import pytest
import allure

async def get_exchange_rate(currency):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.cbr-xml-daily.ru/daily_json.js') as response:
            data = await response.json(content_type='')
            return data['Valute'][currency]['Value']


@allure.story('Задача 3. Асинхронный тест функции, выполняющий запрос к внешнему API')
@pytest.mark.asyncio
async def test_get_exchange_rate(event_loop):
    exchange_rate = await get_exchange_rate('USD')
    assert 91 <= exchange_rate <= 93



