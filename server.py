import socket
import json
import requests
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройка базы данных
DATABASE_URI = 'postgresql://ria_user:your_password@localhost/ria_db'
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class RiaData(Base):
    __tablename__ = 'ria_data'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    title = Column(String(500))
    description = Column(Text)
    lat = Column(Float)
    lon = Column(Float)
    type = Column(String(100))

# Создание таблицы (если её нет)
Base.metadata.create_all(engine)

def fetch_data():
    api_url = "https://cdndc.img.ria.ru/dc/kay-n/2022/SOP-content/data/points/data-24.04.2025.json?v=1196"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://ria.ru"
    }

    try:
        print("Получение данных с API...")
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        print(f"Получено {len(data)} записей")

        for item in data:
            new_entry = RiaData(
                date=datetime.now(),
                title=item.get('name', 'Без названия'),
                description=item.get('text', ''),
                lat=float(item.get('lat', 0)),
                lon=float(item.get('lng', 0)),
                type=item.get('type', 'неизвестно')
            )
            session.add(new_entry)
        session.commit()
        print(f"Успешно записано {len(data)} записей в таблицу ria_data")
        count = session.query(RiaData).count()
        print(f"Всего записей в таблице: {count}")

    except Exception as e:
        print(f"Ошибка: {str(e)}")
        session.rollback()

def start_server():
    host = '127.0.0.1'
    port = 12346

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключение от {addr}")

        data_entries = session.query(RiaData).all()
        data_list = [{
            'id': entry.id,
            'date': entry.date.strftime("%Y-%m-%d %H:%M:%S"),
            'title': entry.title,
            'description': entry.description,
            'lat': entry.lat,
            'lon': entry.lon,
            'type': entry.type
        } for entry in data_entries]

        # Отправляем JSON с указанием длины сообщения
        json_data = json.dumps(data_list, ensure_ascii=False).encode('utf-8')
        header = f"{len(json_data):<10}".encode('utf-8')
        client_socket.sendall(header + json_data)
        client_socket.close()

if __name__ == '__main__':
    fetch_data()  # Загружаем данные в БД
    start_server()  # Запускаем сервер