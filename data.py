from models import db, Goal, Client

have_time = {"1-2": "1-2 часа в неделю",
             "3-5": "3-5 часов в неделю",
             "5-7": "5-7 часов в неделю",
             "7-10": "7-10 часов в неделю"}

days = {"mon": "Понедельник",
        "tue": "Вторник",
        "wed": "Среда",
        "thu": "Четверг",
        "fri": "Пятница",
        "sat": "Суббота",
        "sun": "Воскресенье"}


def get_goals():
    return db.session.query(Goal).all()


def check_client(phone, name):
    existing_client = Client.query.filter(Client.phone == phone).first()
    if existing_client is None:
        new_client = Client(name=name, phone=phone)
        db.session.add(new_client)
        return new_client.id
    else:
        return existing_client.id
