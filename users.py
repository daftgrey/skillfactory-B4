import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
    __tablename__ = 'user'
    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.Float)


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def request_data():
    """
    Запрашивает у пользователя данные и добавляет их в список users
    """
    print("Привет! Я запишу твои данные!")
    first_name = input("Введи своё имя: ")
    last_name = input("А теперь фамилию: ")
    gender = input("Укажи свой пол (Male // Female): ")
    email = input("Мне еще понадобится адрес твоей электронной почты: ")
    birthdate = input("Дата рождения (в формате ГГГГ-ММ-ДД): ")
    height = input("Какой у тебя рост?: ")
    user = User(
        first_name=first_name,
        last_name=last_name,
        gender=gender,
        email=email,
        birthdate=birthdate,
        height=height
    )
    return user

def main():
    session = connect_db()
    user = request_data()
    session.add(user)
    session.commit()
    print("Спасибо, данные сохранены!")

if __name__ == "__main__":
    main()
