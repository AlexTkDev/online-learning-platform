## A platform for organizing and conducting online courses on Django 📚.
> The "Online Learning Platform" project is currently under development.

## Project Description
The "Online Learning Platform" project consists of two separate Django projects:

1. **ProjectA - LMS_online_school**: A platform for organizing and conducting online courses. The main functions include creating courses, assessing student results, conducting webinars and video lessons using ZOOM, and providing individual consultations for students. Platform users can have different roles, such as student or teacher, depending on the role, access rights to the admin panel and the general functionality of the platform change.

2. **ProjectB - Blog**: A blog for publishing articles and news related to the educational platform, only the administrator and a user with the role of teacher can post articles in the blog (the full cycle of CRUD operations is organized for them), a user with the role of student can read the blog.

## Project structure and stages

### 1. Creating Django projects
#### ProjectA (LMS_online_school)
- **Technologies**: Django, Django REST Framework (DRF)
- **Functionality**:
- Creating and delivering online courses.
- Assessing student results.
- Webinars and video lessons in real time.
- Individual consultations.
- User role (student/teacher).

#### ProjectB (Blog)
- **Technologies**: Django, Django REST Framework (DRF)
- **Functionality**:
- Blog for publishing articles.

### 2. REST API
#### ProjectA
- **Technologies used**: Django REST Framework
- **API functionality**:
- Course management (creation, update, deletion, retrieval).
- User registration and management.
- Test and grade management.
- Interface for webinars and video lessons (using: [ZOOM API](https://github.com/JoeyAlpha5/django-zoom-meetings)).

#### ProjectB
- **Technologies used**: Django REST Framework
- **API functionality**:
- Blog management.

### 3. API interaction
- Setting up authentication and authorization using tokens.
- Setting up API requests and responses to transfer data between projects.

### 4. Docker
- **Containerization of ProjectA and ProjectB**:
- Writing a Dockerfile for each project.
- Creating `docker-compose.yml` to manage containers and networks between them.

### 5. Testing
- **Blog**: To test the creation of a blog post, we use django.test, the test_views.py file in the blog/tests/ directory. Run with the command:
```sh
docker-compose exec api python manage.py test blog.tests.test_views
```

- **Online School**: To test whether an authorized user with the teacher or administrator role can successfully create a course. Test using **APITestCase from rest_framework.test.**. Run with the command:
```sh
docker-compose exec api_online_school python manage.py test tests.test
```

### Explanation:
- **`setUp`**: Creates users (teacher and student) and defines the URL for course creation.
- **`test_create_course_as_teacher`**: Checks that the teacher can successfully create a course and that the course is created in the database.
- **`test_create_course_as_student`**: Checks that a student cannot create a course and that the course is not created in the database.

### 6. Asynchronous tasks with Celery
#### ProjectA
- Email notifications upon registration.
- By default, the user has the status of - Inactive, after sending the user an email with a greeting, his status automatically changes to - Active. A user with the role of - teacher needs to be activated by the admin and he will receive the status of staff and will be able to administer courses and the blog.

### 7. Overriding the user model and permissions
#### ProjectA
- Extending the user model with the addition of new fields.
- Setting up a permissions system for access control.

## Project structure 
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

## Links - GitHub repository: [online-learning-platform](https://github.com/AlexTkDev/online-learning-platform.git)

***

## A platform for organizing and conducting online courses on Django 📚.
> Проект "Online Learning Platform" на данный момент находится на стадии разработки.


## Описание проекта
Проект "Online Learning Platform" состоит из двух отдельных Django-проектов:

1. **ProjectA - LMS_online_school**: Платформа для организации и проведения онлайн-курсов. Основные функции включают создание курсов, оценку результатов студентов, проведение вебинаров и видеоуроков при помощи ZOOM, а также предоставление индивидуальных консультаций для студентов. Пользователи платформы могут иметь разные роли, такие как студент или преподаватель, в зависимости от роли меняются права доступа к админ-панели и общему функционалу платформы.

2. **ProjectB - Blog**: Блог для публикации статей и новостей, связанный с образовательной платформой, постить статьи в блоге могут только администратор и пользователь с ролью - преподаватель (для них организован полный цикл CRUD операций), пользователь с ролью - студент можкт читать блог.

## Структура и этапы выполнения проекта

### 1. Создание Django проектов
#### ProjectA (LMS_online_school)
- **Технологии**: Django, Django REST Framework (DRF)
- **Функциональность**:
  - Создание и проведение онлайн-курсов.
  - Оценка результатов студентов.
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
- Настройка аутентификации и авторизации с использованием токенов.
- Настройка API-запросов и ответов для передачи данных между проектами.


### 4. Docker
- **Контейнеризация ProjectA и ProjectB**:
  - Написание Dockerfile для каждого проекта.
  - Создание `docker-compose.yml` для управления контейнерами и сетями между ними.


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


### 6. Асинхронные задачи с Celery
#### ProjectA
- Email уведомления при регистрации.
- По умолчанию пользователь имеет статус - Не активеня, после отправки пользователю email с приветсвием, его статус автоматически изменяется на - Активен. Пользователю с ролью - преподаватель нужно пройти активацию админом и он получит статус персонала и сможет администрировать курсы и блог.


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




