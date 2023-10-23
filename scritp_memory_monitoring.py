import psutil
import requests
import time

# адрес вашего API
api_url = 'https://example.com/api'

# Установите порог потребления памяти, при котором будет генерироваться alarm
memory_threshold = 80  # Пример: 80% используемой памяти

while True:
    memory_percent = psutil.virtual_memory().percent

    if memory_percent > memory_threshold:
        # Сообщение, которое вы хотите отправить на API
        data = {
            'message': 'Потребление памяти выше порога',
            'memory_percent': memory_percent
        }

        try:
            response = requests.post(api_url, json=data)

            if response.status_code == 200:
                print('Успешно отправлен запрос на API')
            else:
                print('Ошибка при отправке запроса на API:', response.status_code)

        except requests.exceptions.RequestException as e:
            print('Ошибка при отправке запроса на API:', e)

    time.sleep(60)  # Проверяйть каждую минуту
