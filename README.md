## A platform for organizing and conducting online courses on Django 📚.
> on development stage
---

# Документация к проекту "Online Learning Platform"

## Описание проекта

Проект "Online Learning Platform" состоит из двух отдельных Django-проектов:

1. **ProjectA - LMS_online_school**: Платформа для организации и проведения онлайн-курсов. Основные функции включают создание курсов, автоматическую оценку результатов студентов, проведение вебинаров и видеоуроков, а также предоставление индивидуальных консультаций для студентов. Пользователи платформы могут иметь разные роли, такие как студент или преподаватель.

2. **ProjectB - Blog**: Блог для публикации статей и новостей, связанный с основной образовательной платформой.

Проект находится на стадии разработки.

## Структура и этапы выполнения проекта

### 1. Создание Django проектов

#### ProjectA (LMS_online_school)
- **Технологии**: Django, Django REST Framework (DRF)
- **Функциональность**:
  - Создание и проведение онлайн-курсов.
  - Автоматическая оценка результатов студентов.
  - Вебинары и видеоуроки в реальном времени.
  - Индивидуальные консультации.
  - Роль пользователей (студент/преподаватель).

#### ProjectB (Blog)
- **Технологии**: Django, Django REST Framework (DRF)
- **Функциональность**:
  - Блог для публикации статей.

### 2. REST API

#### ProjectA
- **Используемые технологии**: Django REST Framework
- **Функциональность API**:
  - Управление курсами (создание, обновление, удаление, получение).
  - Регистрация и управление пользователями.
  - Управление тестами и оценками.
  - Интерфейс для вебинаров и видеоуроков(при помощи: [ZOOM API](https://github.com/JoeyAlpha5/django-zoom-meetings)).

#### ProjectB
- **Используемые технологии**: Django REST Framework
- **Функциональность API**:
  - Управление блогом.

### 3. Взаимодействие через API
- Настройка аутентификации и авторизации с использованием токенов или OAuth.
- Настройка API-запросов и ответов для передачи данных между проектами.

### 4. Docker
- **Контейнеризация ProjectA и ProjectB**:
  - Написание Dockerfile для каждого проекта.
  - Создание `docker-compose.yml` для управления контейнерами и сетями между ними.
  - Настройка контейнеров для взаимодействия через общую сеть.

### 5. Тестирование

- **Blog**: Для проверки создания записи в блоге используем django.test, файл test_views.py в директории blog/tests/. Запускается командой:
```sh
  docker-compose exec api python manage.py test blog.tests.test_views
```

- **Online School**: Для проверки, может ли авторизованный пользователь с ролью преподавателя или администратора успешно создать курс. Теста с использованием **APITestCase из rest_framework.test.**. Запускается командой:
```sh
docker-compose exec api_online_school python manage.py test tests.test
```

### Объяснение:

- **`setUp`**: Создает пользователей (преподавателя и студента) и определяет URL для создания курса.
- **`test_create_course_as_teacher`**: Проверяет, что преподаватель может успешно создать курс и что курс создается в базе данных.
- **`test_create_course_as_student`**: Проверяет, что студент не может создать курс и что курс не создается в базе данных.


#### ProjectA
- **Online-school**:


### 6. Асинхронные задачи с Celery

#### ProjectA
- Email уведомления при регистрации.

#### ProjectB
- Поддержка взаимодействия с ProjectA.


### 7. Переопределение модели пользователя и разрешения

#### ProjectA
- Расширение модели пользователя с добавлением новых полей.
- Настройка системы разрешений для управления доступом.


## Структура проекта

### ProjectA LMS_online_school/
```
├── online_school/
│    ├── .gitignore
│    └── school/
│        ├── blog_posts/
│        ├── config/
│        ├── courses/
│        ├── tests_and_grade/
│        ├── templates/
│        │   ├── online-school/
│        │   ├── videolessons/
│        │   └── users/
│        │
│        │
│        ├── static/
│        ├── users/
│        ├── video_lessons/
│        └── tests/
│           └──ttest.py
│           
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── redis.conf
└── manage.py
```

### ProjectB Blog/
```
├── blog_school/
│   ├── .gitignore
│   └──  blog_data/
│       ├── config/
│       ├── blog/
│       └──  tests/
│             └── test_views.py
│      
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── manage.py
```

## Ссылки
- GitHub репозиторий: [online-learning-platform](https://github.com/AlexTkDev/online-learning-platform.git)

Проект "Online Learning Platform" на данный момент находится на стадии разработки.




