# project/server/user/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FloatField, IntegerField
from wtforms.validators import DataRequired, Optional


class HodlForm(FlaskForm):
    ticker = StringField("Stock tracker", [DataRequired()])
    from_date = DateField("From", format="%d/%m/%Y", validators=[Optional()])
    to_date = DateField("Till", format="%d/%m/%Y", validators=[Optional()])
    smoothing = IntegerField(validators=[Optional()])
    starting_acceleration = IntegerField(validators=[Optional()])
    acceleration_chance = FloatField(validators=[Optional()])
    y_scale = FloatField(validators=[Optional()])
    x_scale = FloatField(validators=[Optional()])
