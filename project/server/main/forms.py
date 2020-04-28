# project/server/user/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, IntegerField
from wtforms.validators import DataRequired, Optional


class HodlForm(FlaskForm):
    ticker = StringField("Stock tracker", [DataRequired()])
    from_date = DateField("From", format="%d/%m/%Y", validators=[Optional()])
    to_date = DateField("Till", format="%d/%m/%Y", validators=[Optional()])
    smoothing = IntegerField()
    starting_acceleration = IntegerField()
    acceleration_chance = FloatField()
    y_scale = FloatField()
    x_scale = FloatField()