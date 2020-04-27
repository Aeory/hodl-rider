# project/server/main/views.py
from api import hodl as api

from flask import render_template, Blueprint, request, jsonify, url_for, redirect, send_file
from werkzeug import FileWrapper
from io import BytesIO

from .forms import HodlForm

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=['GET', 'POST'])
def home():
    form = HodlForm(request.form)
    if request.method == "POST" and form.validate_on_submit():
        ticker = request.form.get('ticker')
        from_date = request.form.get('from')
        to_date = request.form.get('from')
        config = {
            'smoothing': request.form.get('smoothing'),
            'starting_acceleration': request.form.get('starting_acceleration'),
            'acceleration_chance': request.form.get('acceleration_chance'),
            'x_scale': request.form.get('x_scale'),
            'y_scale': request.form.get('y_scale')
        }
        data = api(ticker, from_date, to_date, config)
        file_data = BytesIO(data.encode())
        return send_file(
            file_data,
            mimetype='application/json',
            attachment_filename=f"{ticker.upper()}-hodl-rider.json",
            as_attachment=True
        )
    return render_template("main/home.html", form=form)
