# API для YaЕube домашнее задание на Я.Практикум.

Домашнее задание по созданию API для обработка запросов от клиентов.

## Функционал API:

1. Обращение к API YaTube для CRUD операций.
2. Просмотр, создание, редактирование и удаление постов и комментариев постам.
3. Пользователь должен быть зарегистрирован и получить личный токен.

## Порядок запуска API-сервиса:

Клонируйте репозиторий себе на компьютер/сервер:

```bash
git clone git@github.com:user_name/api_yatube.git
```

Создайте виртуальное окружение:

```bash
python3 -m venv venv
```

Активируйте виртуальное окружение:

*Windows:*
```bash
source venv/Scripts/activate
```
*Linux & MacOS:*
```bash
source venv/Bin/activate
```

Установите зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

## Примеры запросов к API:

1. **Путь к эндпоинтам API.** 
[Link](http://127.0.0.1:8000/api/v1/) - стандартный путь к API
[Link](http://127.0.0.1:8000/api/v1/groups/) - GET получение всех групп
[Link](http://127.0.0.1:8000/api/v1/posts/) - GET получение всех постов
[Link](http://127.0.0.1:8000/api/v1/posts/{post_id}/comment) - GET получение всех комментариев к посту
Ко всем эндпоинтам можно обратиться за детальной информацией, указав в конце id.
2. **Получение токена.**
Убедитесь, что пользователь создан для выполнения запроса.
Метод - POST
[Link](http://127.0.0.1:8000/api/v1/api-token-auth/) -
```json
{
    "username": "regular_user",
    "password": "iWannaBeAdmin"
}
```
Полученный токен необходимо использовать при любых запросах к API.
3. **CRUD операции.**
К эндпоинтам: */api/v1/posts/* и */api/v1/posts/{post_id}/comment* можно отправить запросы POST, PATCH, PUT и DELETE. Примеры запросов к */api/v1/posts/*:
```json
{
    "text": "Пост с группой", - обязательное поле
    "group": {{group_id}} - необязательное поле
}
```
```json
{
    "text": "Пост с группой", - обязательное поле
    "group": {{group_id}} - необязательное поле
}
```
Пример запроса к */api/v1/posts/{post_id}/comment*:
```json
{
    "text": "Тестовый комментарий"
}
```
Любые операции с */api/v1/groups/* доступны только из администраторской панели, доступно только чтение.