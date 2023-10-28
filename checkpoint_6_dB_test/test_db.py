import pytest
import allure
import mysql.connector

DB_CONFIG = {
    'user': 'administrator',
    'password': 'Pa$$w0rd',
    'host': '127.0.0.1',
    'database': 'computer_shop_db',
    'raise_on_warnings': True
}


@pytest.fixture(scope='session')
def db_connection():
    connection = mysql.connector.connect(**DB_CONFIG)
    yield connection
    connection.close()


def select_manufacturer(db_connection, name_manufacturer):
    with db_connection as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * from manufacturer WHERE name_manufacturer = %s", (name_manufacturer,))
        assert cursor.fetchone() is not None


def valid_password(password: str):
    if len(password) < 8:
        return False
    count = 0
    for e in password:
        if e in '!&$%@':
            count += 1
    return count > 1


@allure.story('Тестирование таблицы')
def test_table(db_connection):
    with db_connection.cursor() as cursor:
        with allure.step('INSERT в таблицу Manufacturer'):
            cursor.execute('INSERT INTO manufacturer (name_manufacturer, country_id ) VALUES("Apple", 1)')
            db_connection.commit()
            assert cursor.fetchone() is None

        with allure.step('Проверка результата INSERT'):
            cursor.execute('SELECT * from manufacturer where name_manufacturer = %s', ('Apple',))
            assert cursor.fetchone() is not None

        with allure.step('UPDATE в таблице Manufacturer'):
            cursor.execute('UPDATE manufacturer SET country_id = %s WHERE name_manufacturer = %s', (2, 'Apple'))
            assert cursor.fetchone() is None

        with allure.step("Проверка результата UPDATE в таблице Manufacturer"):
            cursor.execute('SELECT country_id from manufacturer where name_manufacturer = %s', ('Apple',))
            assert cursor.fetchone()[0] == 2

        with allure.step('DELETE из таблицы Manufacturer'):
            cursor.execute('DELETE from manufacturer where name_manufacturer = %s', ('Apple',))
            db_connection.commit()

        with allure.step("Проверка результата DELETE в таблице Manufacturer"):
            cursor.execute('SELECT * from manufacturer where name_manufacturer = %s', ('Apple',))
            assert cursor.fetchone() is None


@allure.story('Проверка целостности данных при вводе через процедуру Manufacturer_Insert, отрицательное тестирование')
def test_integrity_procedure_manufacturer_insert(db_connection):
    with allure.step('Проверка обеспечения целостности данных при добавлении данных через процедуру'):
        with db_connection as connection:
            cursor = connection.cursor()
            cursor.execute("call Manufacturer_insert(%s, %s)", ('Fake', 4))
            assert cursor.fetchone() is None


@allure.story('Проверка надежности паролей пользователей')
def test_passwords(db_connection):
    with allure.step('Проверка длины пароля и наличия специальных символов'):
        with db_connection as connection:
            cursor = connection.cursor()
            cursor.execute('select password_buyer from buyer')
            res = cursor.fetchall()
            for e in res:
                assert valid_password(e[0])


@allure.story('Проверка целостности данных - наличие связанных записей в родительской таблице')
def test_relation_with_parent(db_connection):
    with db_connection as connection:
        cursor = connection.cursor()
        cursor.execute('select country_id from manufacturer')
        countries_in_manufacturers = {e[0] for e in cursor.fetchall()}
        cursor.execute('select id_country from country')
        countries_in_countries = {e[0] for e in cursor.fetchall()}
        assert (countries_in_manufacturers - countries_in_countries) == set()
