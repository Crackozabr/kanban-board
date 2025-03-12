# Проект Kanban Board

## Описание проекта

Kanban Board — это веб-приложение для управления задачами и отслеживания их выполнения. Оно разработано с использованием Flask (Python) и Bootstrap. Функциональность включает:

- Создание и управление пользователями.
- Создание, редактирование и архивирование задач.
- Назначение задач пользователям.
- Управление сроками выполнения задач.
- Визуализация задач на доске Канбан.

## Скриншоты

![Kanban Board Screenshot](/screenshots/screenshot.png)

## Требования

- Python 3.8+
- Flask
- SQLite (используется в качестве базы данных)
- Bootstrap (для визуализации)

## Установка

### Установка Python

Для работы приложения достаточно установить приложение Python на компьютер.
[Download Python | Python.org](https://www.python.org/downloads/)

Для написания и отладки кода можно использовать редактор VS Code.
[Visual Studio Code on Windows](https://code.visualstudio.com/docs/setup/windows#_use-the-windows-installer)

### Создание папки проекта

#### Клонирование репозитория

Склонируйте репозиторий на ваш компьютер:

```bash
git clone https://github.com/Crackozabra/kanban-board.git
cd kanban-board
```

#### Копирование файлов проекта

Расположите папку с файлами проекта на компьютере.
К примеру, папка проекта расположена в директории ``C:\Projects\`` тогда общий путь к папке с проектом будет ``C:\Projects\kanban_app\``
Общая структура каталогов и файлов проекта

```bash
kanban_app/
│
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── index.html
│   ├── edit_task.html
│   └── archive.html
├── app.py
├── README.md
└── requirements.txt
```

После этого перейдите к папке проекта в командной строке

```bash
cd C:\Projects\kanban_app
```

### Создаем виртуальное окружение и устанавливаем зависимости

Создаем виртуальное окружение ``env``

```bash
python -m venv env
```

Активируем виртуальное окружение

- Для Windows:

  ```bash
  env\Scripts\activate
  ```
- Для macOS/Linux:

  ```bash
  source env/bin/activate
  ```

Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

### **Запуск проекта**

Запускаем приложение, выполнив следующую команду в терминале:

```bash
python app.py
```

Открываем браузер и переходим по адресу [http://127.0.0.1:5000/](http://127.0.0.1:5000/) для просмотра доски Канбан.

После первого запуска программа в директории проекта создаст директорию ``instance`` и поместит в неё файл ``kanban.db``.
Итоговый вид директории проекта к этому времени будет выглядеть следующим образом:

```bash
kanban_app/
│
├── env/..
├── instance/
│   └── kanban.db
├── static/
│   └── css/
│       └── style.css
├── templates/
│   ├── index.html
│   ├── edit_task.html
│   └── archive.html
├── app.py
├── README.md
└── requirements.txt
```

---

## Использование

### Создание пользователя

1. Перейдите на вкладку "Add User".
2. Введите имя пользователя и нажмите "Add User".

### Создание задачи

1. Перейдите на вкладку "Add Task".
2. Введите название задачи, описание и выберите пользователей для задачи.
3. Нажмите "Add Task".

### Редактирование задачи

1. Нажмите на кнопку "Edit" рядом с задачей.
2. Измените название, описание, даты или назначенных пользователей.
3. Нажмите "Save Changes".

### Подсветка задач

1. Перейдите на вкладку "Users".
2. Нажмите на имя пользователя для подсветки его задач.
3. Нажмите "Reset Highlights", чтобы сбросить подсветку.

## Дополнительные функции

- **Управление сроками выполнения**: Укажите дату начала и дату окончания задачи при создании или редактировании.
- **Архивирование задач**: Переместите выполненные задачи в архив.
- **Подсветка просроченных задач**: Задачи с просроченными датами будут подсвечены красным цветом.

---

## Оценка S.M.A.R.T.

### 1. Specific (Специфичность)

**Цель проекта**: Создать веб-приложение в виде доски Канбан для управления задачами с возможностью добавления пользователей, назначения задач, отслеживания выполнения и архивирования.

- **Оценка**: **Высокая**
  Цель проекта была сформулирована конкретно и ясно. Все функции, такие как добавление пользователей, задач, архивирование и подсветка карточек, были реализованы и соответствуют изначальной цели.

---

### 2. Measurable (Измеримость)

**Критерии успеха**:

1. Возможность добавления и удаления пользователей.
2. Возможность создания, редактирования и архивирования задач.
3. Подсветка задач без назначенных пользователей.
4. Управление сроками выполнения задач.
5. Визуализация задач в виде карточек на доске Канбан.

- **Оценка**: **Высокая**
  Все критерии успеха были реализованы и можно легко проверить их наличие и функциональность. Проект соответствует измеримым критериям.

---

### 3. Achievable (Достижимость)

**Ресурсы и сложность**:

- Использование Flask и Bootstrap для создания веб-приложения.
- База данных SQLite для хранения данных.
- Реализация функций через HTML, CSS и JavaScript.
- **Оценка**: **Средняя**
  Проект был реализован с использованием доступных ресурсов и технологий. Однако, для более сложных или масштабируемых проектов, может потребоваться использование более мощных инструментов и архитектуры (например, использование PostgreSQL вместо SQLite, или добавление аутентификации пользователей). В текущем виде проект достижим и функционален.

---

### 4. Relevant (Актуальность)

**Целевая аудитория и применение**:

- Проект предназначен для команд, которые хотят визуализировать и управлять своими задачами.
- Он может использоваться в малых и средних проектах для отслеживания выполнения задач.
- **Оценка**: **Высокая**
  Проект актуален для целевой аудитории и решает реальные проблемы управления задачами. Он может быть легко адаптирован для разных команд и проектов.

---

### 5. Time-bound (Ограниченность во времени)

**Временные рамки и этапы**:

- Проект был разработан в несколько этапов: создание базовой структуры, добавление функций, улучшение визуализации и добавление новых возможностей (например, даты выполнения).
- Каждый этап был реализован в разумные сроки.
- **Оценка**: **Высокая**
  Проект был реализован в рамках разумных временных рамок. Все функции были добавлены постепенно, и проект был завершен в соответствии с запланированными этапами.

---

### Общая оценка

Проект "Kanban Board" с использованием Flask и Bootstrap является **успешным** и соответствует критериям S.M.A.R.T.:

- Цель была конкретной и ясной.
- Проект легко измерим и проверяем.
- Он был реализован с использованием доступных ресурсов и технологий.
- Проект актуален для целевой аудитории и решает реальные проблемы.
- Временные рамки были соблюдены, и проект был завершен в разумные сроки.

**Рекомендации для дальнейшего улучшения**:

1. Добавить аутентификацию пользователей для более безопасного управления задачами.
2. Перейти на более мощную базу данных (например, PostgreSQL) для масштабирования.
3. Добавить дополнительные функции, такие как уведомления о просроченных задачах или статистика выполнения.

В целом, проект является хорошим примером функционального и полезного веб-приложения.

## Лицензия

MIT License

## Автор

[Crackozabra]
[GitHub](https://github.com/Crackozabr "GitHub")
