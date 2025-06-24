# Дарья Агафонова, 31а когорта - Финальный проект. Инженер по тестированию расширенный

import data
from api_requests import create_order, get_order_info_by_track

def test_get_order_info_by_track():
    # Создание заказа и получение трека
    create_response = create_order(data.order_body)
    track = create_response.json()['track']
    
    # Получение информации о заказе по треку
    response = get_order_info_by_track(track)
    
    # Проверка статус-кода
    assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"
    print(f"Тест пройден. Статус код: {response.status_code}, трек заказа: {track}")
    


