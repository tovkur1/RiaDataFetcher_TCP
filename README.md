# **RIA Data Fetcher**  

🚀 **Client-Server Application** for parsing, storing, and displaying data from [RIA.ru](https://ria.ru) (Russian News Agency).  

🔹 **Server (Python)** — парсит данные с RIA.ru, сохраняет в **PostgreSQL** и отправляет клиенту по TCP.  
🔹 **Client (Qt/C++)** — подключается к серверу и отображает данные в удобном интерфейсе.  

---

## **📌 Содержание**  
1. [Функционал](#-функционал)  
2. [Технологии](#-технологии)  
3. [Установка и запуск](#-установка-и-запуск)  
   - [Сервер (Python)](#сервер-python)  
   - [Клиент (Qt/C++)](#клиент-qtc)  
4. [Структура проекта](#-структура-проекта)  
5. [Скриншоты](#-скриншоты)  
6. [Лицензия](#-лицензия)  

---

## **🎯 Функционал**  
✅ **Серверная часть:**  
- Парсинг данных с API RIA.ru.  
- Сохранение в **PostgreSQL** (дата, заголовок, описание, координаты).  
- Отправка данных клиенту через **TCP-сокет**.  

✅ **Клиентская часть:**  
- Подключение к серверу по **TCP (127.0.0.1:12346)**.  
- Отображение данных в **QTextEdit**.  
- Обработка ошибок соединения.  

---

## **⚙ Технологии**  
| **Сервер** (Python)       | **Клиент** (C++/Qt)       |
|---------------------------|---------------------------|
| `Python 3.9+`             | `Qt 5.15+`                |
| `SQLAlchemy` (ORM)        | `QTcpSocket` (сетевое взаимодействие) |
| `PostgreSQL` (БД)         | `QJsonDocument` (парсинг JSON) |
| `requests` (HTTP-запросы) | `QTextEdit` (вывод данных) |

---

## **🚀 Установка и запуск**  

### **Сервер (Python)**  

#### **1. Установка зависимостей**  
```bash
pip install -r server/requirements.txt
```  
(Файл `requirements.txt` уже содержит `sqlalchemy`, `psycopg2-binary`, `requests`.)  

#### **2. Настройка PostgreSQL**  
- Установите PostgreSQL:  
  ```bash
  sudo apt install postgresql postgresql-contrib  # Linux
  ```
- Создайте БД и пользователя:  
  ```sql
  CREATE DATABASE ria_db;
  CREATE USER ria_user WITH PASSWORD 'your_password';
  GRANT ALL PRIVILEGES ON DATABASE ria_db TO ria_user;
  ```

#### **3. Запуск сервера**  
```bash
python server/server.py
```  
➡ **Сервер запустится на `127.0.0.1:12346`.**  

---

### **Клиент (Qt/C++)**  

#### **1. Сборка (через Qt Creator)**  
1. Откройте проект `client/` в **Qt Creator**.  
2. Настройте **компилятор (MinGW/MSVC)**.  
3. Нажмите **"Собрать" → "Запустить"**.  

#### **2. Или сборка через CMake**  
```bash
cd client/
mkdir build && cd build
cmake ..
make
./RiaDataFetcher
```  

➡ **Клиент подключится к серверу автоматически.**  

---

## **📂 Структура проекта**  
```
RiaDataFetcher/
├── server/                  # Сервер (Python)
│   ├── server.py            # Основной скрипт
│   └── requirements.txt     # Зависимости
├── client/                  # Клиент (Qt/C++)
│   ├── mainwindow.h         # Заголовочный файл
│   ├── mainwindow.cpp       # Логика клиента
│   └── CMakeLists.txt       # Файл сборки (опционально)
└── README.md                # Документация
```

---

## **🖼 Скриншоты**  
### **1. Клиент (Qt)**  
![Клиентское приложение](https://via.placeholder.com/600x400/555555/FFFFFF?text=Qt+Client+Preview)  

### **2. Данные в PostgreSQL**  
```sql
SELECT * FROM ria_data;
```
![Данные в БД](https://via.placeholder.com/600x200/555555/FFFFFF?text=PostgreSQL+Output)  

---

## **📜 Лицензия**  
**MIT License** — свободное использование с указанием авторства.  

---

## **📌 Итог**  
✔ **Сервер** парсит RIA.ru → **PostgreSQL** → отправляет клиенту.  
✔ **Клиент** подключается и показывает данные.  
✔ **Готово к расширению** (можно добавить графики, фильтры и т.д.).  

🚀 **Старт:**  
```bash
# Сервер
python server/server.py

# Клиент
./client/build/RiaDataFetcher
```  


