# project/server/main/views.py
from api import hodl as api

from flask import render_template, Blueprint, request, send_file
from io import BytesIO

from .forms import HodlForm

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=['GET', 'POST'])
def home():
    form = HodlForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        ticker = form.ticker.data
        from_date = form.from_date.data
        to_date = form.to_date.data
        config = {
            'smoothing': form.smoothing.data,
            'starting_acceleration': form.starting_acceleration.data,
            'acceleration_chance': form.acceleration_chance.data,
            'x_scale': form.x_scale.data,
            'y_scale': - form.y_scale.data if form.y_scale.data else None
        }
        data = api(ticker, from_date, to_date, config)
        file_data = BytesIO(data.encode())
        return send_file(
            file_data,
            mimetype='application/json',
            attachment_filename=f"{ticker.upper()}-hodl-rider.track.json",
            as_attachment=True
        )
    return render_template("main/home.html", form=form)
