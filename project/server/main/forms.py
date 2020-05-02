# project/server/user/forms.py


from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, DateField, FloatField, IntegerField
from wtforms.validators import DataRequired, Optional


class HodlForm(FlaskForm):
    ticker = StringField(
        label="ticker symbol",
        validators=[DataRequired()],
        default='BTCUSD',
        description="the stock you want to ride"
    )
    from_date = DateField(
        label="from",
        format="%d/%m/%Y",
        validators=[Optional()],
        description="if you leave either of these blank it will take the earliest / latest date available"
    )
    to_date = DateField(
        label="to",
        format="%d/%m/%Y",
        validators=[Optional()]
    )
    smoothing = IntegerField(
        label="track smoothhhhnessss",
        validators=[Optional()],
        description="1 is not an appropriate answer..."
    )
    x_scale = FloatField(
        label="number of days per track piece (x-axis scale)",
        validators=[Optional()],
        description="reducing this makes the ride longer???"
    )
    y_scale = FloatField(
        label="number of dollars per height (y-axis scale)",
        validators=[Optional()],
        description="big numbers for crypto advised.."
    )
    acceleration_chance = FloatField(
        label="minimum acceleration chance",
        validators=[Optional()],
        description="the smallest chance that a piece of track will be an accelerator, results above .4 may result in orbit"
    )
    starting_acceleration = IntegerField(
        label="starting acceleration tracks",
        validators=[Optional()],
        description="started from the bottom now we're here"
    )
    recaptcha = RecaptchaField()


