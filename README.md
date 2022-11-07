# Репозиторий с тестовым заданием на позицию Python Developer в Mediasoft

# Трофимов Дмитрий

## HTTP-API для взаимодействия с магазинами(создание, поиск магазинов по фичам)

***

### Установка

Установить Docker и Docker-compose плагин

### Запуск

Запустить команду `docker-compose up` в корне проекта

### Необходимые данные

Зарегистрированный админ-аккаунт:

Login: admin

Email: admin@admin.ru

Password: admin

### Тестирование

Пример создания магазина

POST

http://127.0.0.1:8000/shop/

```json
{
  "shop_name": "My Shop",
  "street": 1,
  "city": 1,
  "home": "1",
  "open_time": "08:00",
  "close_time": "22:00"
}
```

### Список городов

GET

http://127.0.0.1:8000/city/

### Улицы города с ID = 1

GET

http://127.0.0.1:8000/city/1/

### Фильтрация магазинов по фичам

В данном случае ищутся открытые магазины в Городе ульяновск
GET http://127.0.0.1:8000/shop?city=Ульяновск&open=1
