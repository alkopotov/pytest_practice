import aiomysql
import pytest
import allure

DB_CONFIG = {
    'user': 'administrator',
    'password': 'Pa$$w0rd',
    'host': '127.0.0.1',
    'db': 'computer_shop_db'
}

TEST_DATA = {
    'name_manufacturer': 'Samsung',
    'country_id': 4
}


async def insert_manufacturer(name: str, country_id: int):
    async with aiomysql.connect(**DB_CONFIG) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("INSERT into manufacturer (name_manufacturer, country_id) VALUES (%s, %s)",
                                 (name, country_id))
            await connection.commit()
        await cursor.close()
    connection.close()


@allure.story('Задача 4. Асинхронный тест функции, добавляющей запись в таблицу БД')
@pytest.mark.asyncio
async def test_insert_manufacturer(event_loop):
    await insert_manufacturer(TEST_DATA['name_manufacturer'], TEST_DATA['country_id'])
    async with aiomysql.connect(**DB_CONFIG) as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("SELECT * from manufacturer where name_manufacturer = %s", (TEST_DATA['name_manufacturer'],))
            id_n, name, country = await cursor.fetchone()
            assert country == TEST_DATA['country_id']
        await cursor.close()
    connection.close()

