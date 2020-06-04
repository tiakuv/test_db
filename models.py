from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.sqlite import JSON

db = SQLAlchemy()

goals_teachers = db.Table('goals_teachers', db.metadata,
                          db.Column('goal_id', db.Integer, db.ForeignKey('goals.id')),
                          db.Column('teacher_id', db.Integer, db.ForeignKey('teachers.id'))
                          )


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    about = db.Column(db.Text())
    picture = db.Column(db.String(50), unique=True)
    rating = db.Column(db.Float)
    price = db.Column(db.Integer, nullable=False)
    schedule = db.Column(JSON)

    goals = db.relationship('Goal', secondary=goals_teachers, back_populates="teachers")  # many to many
    booking = db.relationship('Booking', back_populates="teacher")


class Goal(db.Model):
    __tablename__ = "goals"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False, unique=True)
    icon = db.Column(db.String(40), nullable=False, unique=True)

    teachers = db.relationship('Teacher', secondary=goals_teachers, back_populates="goals")
    request = db.relationship('Request')  # у одной цели м.б. много заявок


class Client(db.Model):
    __tablename__ = "clients"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(11), nullable=False)

    request = db.relationship('Request', back_populates="client")
    booking = db.relationship('Booking', back_populates="client")


class Request(db.Model):
    __tablename__ = "requests"
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String)

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship('Client', back_populates="request")

    goal_id = db.Column(db.Integer, db.ForeignKey('goals.id'))
    goal = db.relationship('Goal')


class Booking(db.Model):
    __tablename__ = "bookings"
    id = db.Column(db.Integer, primary_key=True)

    day = db.Column(db.String)
    time = db.Column(db.String)

    client_id = db.Column(db.Integer, db.ForeignKey('clients.id'))
    client = db.relationship('Client')

    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'))
    teacher = db.relationship('Teacher')
