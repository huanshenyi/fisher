__author__ = "ハリネズミ"
from wtforms import form, StringField, IntegerField
from wtforms.validators import Length, NumberRange


class SearchForm(form):
    q = StringField(validators=[Length(min=1, max=30)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
