import re

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, SubmitField, validators
from wtforms.validators import InputRequired, Regexp, ValidationError

from data import have_time, get_goals


def check(form, field):
    if not re.match("((8)[0-9]{10})$", field.data):
        raise ValidationError(field.gettext("Номер телефона должен соответствовать шаблону"))


class RequestForm(FlaskForm):
    goal = RadioField('goal', choices=[(str(i.id), i.name) for i in get_goals()], default=1)
    time = RadioField('time', choices=have_time.items(), default="1-2")
    name = StringField('Вас зовут', [InputRequired()])
    phone = StringField('Ваш телефон', [InputRequired(), check])
    submit = SubmitField("Найдите мне преподавателя")


class BookingForm(FlaskForm):
    time = HiddenField()
    day = HiddenField()
    id = HiddenField()
    name = StringField('Вас зовут', [InputRequired()])
    phone = StringField('Ваш телефон', [InputRequired(), check])
    submit = SubmitField("Найдите мне преподавателя")