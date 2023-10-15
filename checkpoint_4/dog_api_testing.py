import pprint
import requests
import pytest
import random


@pytest.fixture()
def base_url():
    return 'https://dog.ceo/api'


# @pytest.fixture()
def get_random_pictures():
    return [requests.get('https://dog.ceo/api/breeds/image/random').json()['message'] for _ in range(20)]


def get_random_sub_breeds():
    breeds = requests.get('https://dog.ceo/api/breeds/list/all').json()['message']
    breeds_with_sub = [[e, breeds[e]] for e in breeds.keys() if breeds[e] != []]
    breeds_with_sub = [(elem[0], sub) for elem in breeds_with_sub for sub in elem[1]]
    return random.sample(breeds_with_sub, 20), random.sample(breeds.keys(), 20)


@pytest.fixture(params=get_random_pictures())
def get_url(request):
    return request.param


# Тест 1 Проверка типа отдаваемых данных по ссылке случайного изображения
@pytest.mark.parametrize('type_content', ['image', 'video'])
def test_content_type(get_url, type_content):
    random_pict = requests.get(get_url)
    assert random_pict.headers['Content-Type'].startswith(type_content)


# Тест 2 Проверка формата файлов по ссылкам случайного изображения
@pytest.mark.parametrize('file_format', ['jpeg'])
def test_file_format(get_url, file_format):
    random_pict = requests.get(get_url)
    assert random_pict.headers['Content-Type'].endswith(file_format)

# Тест 3 Проверка качества изображений по ссылкам случайных изображений
@pytest.mark.parametrize('size', [15000])
def test_file_quality(get_url, size):
    random_pict = requests.get(get_url)
    assert int(random_pict.headers['Content-length']) > size


# Тест 4 Проверка наличия изображений по породам
@pytest.mark.parametrize('breed', get_random_sub_breeds()[1])
def test_breeds(base_url, breed):
    pict_list = requests.get(base_url + '/breed/' + breed + '/images').json()['message']
    assert len(pict_list) == 0


# Тест 5 Проверка наличия изображений по подвидам пород
@pytest.mark.parametrize('sub_breed', get_random_sub_breeds()[0])
def test_sub_breeds(base_url, sub_breed):
    pict_list = requests.get(base_url + '/breed/' + sub_breed[0] + '/' + sub_breed[1] + '/images').json()['message']
    assert len(pict_list) == 0