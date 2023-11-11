import aiohttp
import asyncio
# import pytest
#
# async def get_exchange_rate(currency):
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://www.cbr-xml-daily.ru/daily_json.js') as response:
#             data = await response.json(content_type='')
#             print(data['Valute'][currency]['Value'])
#
#
# ioloop = asyncio.get_event_loop()
# ioloop.run_until_complete((get_exchange_rate('EUR')))
# ioloop.close()


import aiomysql

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
            await cursor.execute("INSERT into manufacturer(name_manufacturer, country_id) VALUES(%s, %s)",
                                 (name, country_id))
            await connection.commit()
        await cursor.close()
    connection.close()



# async def select_manufacturer(name):
#     async with aiomysql.connect(**DB_CONFIG) as connection:
#         async with connection.cursor() as cursor:
#             await cursor.execute("SELECT * from manufacturer where name_manufacturer = %s", (name,))
#             res = await cursor.fetchone()
#         await cursor.close()
#     connection.close()
#     print(res[2] == 1)

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete((insert_manufacturer('Samsung', 4)))
ioloop.close()