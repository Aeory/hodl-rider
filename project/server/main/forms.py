# project/server/user/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class HodlForm(FlaskForm):
    tracker = StringField("Stock tracker", [DataRequired()])


