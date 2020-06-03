from flask import render_template, redirect, request
from sqlalchemy.orm.attributes import flag_modified

from app import app
from forms import RequestForm, BookingForm
from models import db, Goal, Teacher, Request, Booking
from data import get_goals, check_client, days, have_time


@app.route('/')
def main():
    teachers = Teacher.query.order_by(Teacher.rating.desc()).limit(6).all()
    return render_template("index.html", goals=get_goals(), teachers=teachers)


@app.route('/goals/<int:goal_id>')
def show_goal(goal_id):
    goal = Goal.query.filter(Goal.id == goal_id).first()
    teachers_by_goal = goal.teachers
    return render_template("goal.html", teachers=teachers_by_goal, goal=goal)


@app.route('/profiles/<int:id>')
def show_profile(id):
    teacher = Teacher.query.get_or_404(id)
    return render_template("profile.html", teacher=teacher, days=days)


@app.route('/request/', methods=["POST", "GET"])
def show_request():

    form = RequestForm()

    if request.method == 'POST' and form.validate_on_submit():

        goal = form.goal.data
        time = form.time.data
        name = form.name.data
        phone = form.phone.data

        new_request = Request(time=time, client_id=check_client(name, phone), goal_id=goal)
        goal_name = form.goal.choices[int(goal) - 1][1]
        db.session.add(new_request)
        db.session.commit()

        return render_template("request_done.html",
                               goal=goal_name, time=have_time[time], name=name, phone=phone)

    print(form.validate_on_submit())
    print(form.validate())
    print(form.is_submitted())
    return render_template("request.html", form=form)


@app.route('/booking/<int:id>/<day>/<time>/')
def book_form(id, day, time):
    form = BookingForm()
    teacher = Teacher.query.get_or_404(id)
    return render_template("booking.html",
                           form=form, teacher=teacher,
                           day=day, day_name=days[day], time=time)


@app.route('/booking_done/', methods=["POST"])
def res_book():
    form = BookingForm()
    name = form.name.data
    phone = form.phone.data
    day = form.day.data
    time = form.time.data
    id = form.id.data
    print(time, id)

    teacher = db.session.query(Teacher).filter(Teacher.id == id).one()
    teacher.schedule[day][time] = False
    flag_modified(teacher, "schedule")

    new_booking = Booking(day=day, time=time, client_id=check_client(name, phone), teacher_id=id)
    db.session.add(new_booking)

    db.session.commit()
    print(teacher.schedule)

    return render_template("booking_done.html",
                           name=name, phone=phone,
                           day_name=days[day], time=time)
