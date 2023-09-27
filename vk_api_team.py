import requests
import vk_api
import json
import random
import json

with open ('VK_token.txt', 'r') as file:
    vk_token = file.readline()
with open ('service_toke.txt', 'r') as file:
    service_token = file.readline()

plack_list = []

def get_bot_user_info(token: str) -> dict:
    try:
        params = {
            'fields': 'city,sex,bdate',
            'access_token': token,
            'v': '5.131',
        }
        response = requests.get('https://api.vk.com/method/users.get', params=params)

        if response.status_code == 200:
            data = response.json()

            user_info = data.get('response', [])[0]

            city = user_info.get('city', {}).get('title', 'Город не указан')
            sex = user_info.get('sex', 0)  # 1 - женский, 2 - мужской
            bdate = user_info.get('bdate', 'Дата рождения не указана')

            return {
                'city': city,
                'sex': 'Женский' if sex == 1 else 'Мужской',
                'bdate': bdate,
            }
        else:
            print(f"Ошибка при выполнении запроса: {response.status_code}")
    except Exception as e:
        print(f"Ошибка при получении информации о пользователе: {e}")
        return e

def get_vk_top_liked_photo_urls(user_id: int, vk_token: str, count=4):

    response = requests.get(
        f"https://api.vk.com/method/photos.get?owner_id={user_id}&album_id=profile&count={count}&access_token={vk_token}&v=5.131&sort=likes&photo_sizes=1"
    )
    data = response.json()

    if "error" in data:
        error_msg = data["error"]["error_msg"]
        print(f"Ошибка при получении фотографий с профиля VK: {error_msg}")
        return None

    photos = data["response"]["items"]
    
    photo_urls = []
    for photo in photos:
        sizes = photo.get("sizes", [])

        for size in sizes:
            if size["type"] in ("w", "z"):
                photo_urls.append(size["url"])
                break

    return photo_urls

def search_users(min_age: int, max_age: int, city: int, sex: int) -> str:
    user_list = []
    params = {
        'age_from': min_age,
        'age_to': max_age,
        'city': city,
        'sex': sex,
        'access_token': vk_token,
        'v': '5.131',
        'count': 1,
    }
    response = requests.get('https://api.vk.com/method/users.search', params=params)
    if response.status_code == 200:
        data = response.json()
        users = data['response']['items']
        for user in users:
            user_info = {
                'id': user['id'],
                'first_name': user['first_name'],
                'last_name': user['last_name'],
            }
            user_list.append(user_info)

    else:
        print("Ошибка при выполнении запроса")

    return user_list

def random_users(min_age: int = random.randint(18, 30), max_age: int = random.randint(31, 60), city: int = random.randint(1, 7), sex: int = random.randint(1, 2)) -> list:
    user_list = []
    params = {
        'age_from': min_age,
        'age_to': max_age,
        'city': city,
        'sex': sex,
        'access_token': vk_token,
        'v': '5.131',
        'count': 1,
    }

    response = requests.get('https://api.vk.com/method/users.search', params=params)

    if response.status_code == 200:
        data = response.json()
        users = data['response']['items']
        for user in users:
            user_info = {
                'id': user['id'],
                'first_name': user['first_name'],
                'last_name': user['last_name'],
            }
            user_list.append(user_info)

    else:
        return response.status_code

    return user_list

def black_list(id_user: int):
    plack_list.append(id_user)

def like_external_photo(photo_url, vk_token):
    api_url = 'https://api.vk.com/method/likes.add'

    params = {
        'type': 'photo',
        'item_id': photo_url,
        'access_token': vk_token,
        'v': '5.131'
    }

    try:
        response = requests.post(api_url, params=params)
        data = response.json()

        if 'response' in data:
            print("Лайк успешно поставлен!")
        else:
            print(f"Ошибка при постановке лайка: {data.get('error', {}).get('error_msg', 'Неизвестная ошибка')}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")