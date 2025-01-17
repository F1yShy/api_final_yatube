# Проект API для сервиса Yatube

### Описание

Проект API для сервиса Yatube предоставляет возможность получения данных о постах, группах, комментариях к постам и подписчиках. Для авторизации пользователей используется технология токенов JWT.

API дает возможность сторонним разработчикам, которые получают данные с сервиса Yatube, создавать свои приложения, которые могут, например, читать и публиковать посты и комментарий, взамодействовать с другими социальными сетями.

API для сервиса Yatube расширяет возможности сервиса, позволяя сделать его более функциональным и удобным, предоставляя возможности для взамодействия.

### Установка

1. Клонировать репозиторий

```
git clone https://github.com/F1yShy/api_final_yatube.git
```

2. Перейти в репозиторий

```
cd api_final_yatube
```

3. Создать виртуальное окружение

```
python3 -m venv venv
```

4. Активировать виртуальное окружение

```
source venv/bin/activate
```

```
python3 -m pip install --upgrade pip
```

5. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

6. Выполнить миграции:

```
python3 manage.py migrate
```

7. Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов к API

_Для небезопасных методов в API требуется авторизация_

Получение списка групп (GET запрос):

_Запрос_

```
http://127.0.0.1:8000/api/v1/groups/
```

_Ответ_

```
{
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
}
```

Получение списка постов (GET запрос):

_Запрос_

```
http://127.0.0.1:8000/api/v1/posts/
```

_Ответ_

```
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
    {}
    ]
}
```

Создание поста (POST запрос):

_Запрос_

```
http://127.0.0.1:8000/api/v1/posts/
```

```

{
    "text": "123123",
    "group": {{group_id}}
}
```

_Ответ_

```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```

_group_ не является обязательным, в случае необходимости указывается id группы

Все методы описаны в документации по ссылке:

```
http://127.0.0.1:8000/redoc/
```

### Используемые технологии

**Python 3.10**

Для реализации API для сервиса Yatube используются следующие технологии:

1. **Django 3.2.16** - фреймворк для создания веб-приложений на языке Python. Он предоставляет множество инструментов для работы с базами данных, шаблонами, формами и многое другое.

2. **Django Rest Framework 3.12.4** - расширение для Django, которое позволяет быстро и удобно создавать RESTful API. Оно предоставляет множество инструментов для сериализации и десериализации данных, авторизации и аутентификации пользователей, обработки ошибок и многое другое.

3. **Djoser 2.1.0** - библиотека для Django, которая предоставляет готовые решения для создания и проверки учетных записей пользователей. Она позволяет управлять процессом регистрации, авторизации, восстановления пароля и многое другое.

4. **Django Filters 23.3** - пакет для Django, который предоставляет инструменты для фильтрации данных в запросах. Он позволяет быстро и удобно создавать фильтры по различным полям моделей.

5. **Pytest 6.2.4** - фреймворк для автоматического тестирования на языке Python. Он предоставляет множество инструментов для написания и запуска тестов, а также для генерации отчетов о результатах тестирования.

### Контактная информация

Для связи со мной в GitHub можно перейти по ссылке https://github.com/F1yShy. Также вы можете написать мне на электронную почту, указанную в профиле на GitHub. Буду рад ответить на ваши вопросы и обсудить возможные совместные проекты.
