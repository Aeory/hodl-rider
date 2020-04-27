# project/server/user/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import DataRequired


class HodlForm(FlaskForm):
    ticker = StringField("Stock tracker", [DataRequired()])
    from_date = DateField("From")
    to_date = DateField("Till")
