import json

import requests


def verify(request) -> dict:
    error_message_dict = {
        'Ошибка': 'Некорректный формат данных',
        'Корректный формат': ["Каховская", "Баррикадная", "Пиковая", ]

    }
    try:
        stations_list = json.loads(request.data['stations'])
    except (json.JSONDecodeError, TypeError):

        return error_message_dict

    if stations_list is None:
        return error_message_dict

    fetched_stations_data = fetch_moscow_stations_data()
    hh_stations = get_stations(fetched_stations_data)

    return verify_stations(set(stations_list), hh_stations)


def fetch_moscow_stations_data() -> dict:
    response = requests.get('https://api.hh.ru/metro/1')
    response.raise_for_status()

    return response.json()


def get_stations(stations_data) -> set:
    stations = set()

    for line in stations_data['lines']:
        for station in line['stations']:
            stations.add(station['name'])

    return stations


def verify_stations(requested_stations: set, real_stations: set) -> dict:
    return {'unchanged': requested_stations & real_stations,
            'updated': requested_stations - real_stations,
            'deleted': real_stations - requested_stations}
