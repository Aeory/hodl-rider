# project/server/main/views.py
from api import hodl as api

from flask import render_template, Blueprint, request, jsonify, url_for, redirect

from .forms import HodlForm

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=['GET'])
def home():
    form = HodlForm()
    return render_template("main/home.html", form=form)


@main_blueprint.route('/hodl', methods=['POST'])
def hodl():
    form = HodlForm()
    if form.validate_on_submit():
        ticker = request.form.get('ticker')
        from_date = request.form.get('from')
        to_date = request.form.get('from')
        data = api(ticker, from_date, to_date)
        return jsonify(data)
    return redirect('home')

# ticker = input("What ticker symbol do you want to track? (Default $SPY)") or "SPY"
# start_date = input("What date would you like the track to start at? (Default - earliest available)") or '1900-01-01'
# end_date = input("What date would you like the track to end at? (Default - latest available)") or str(date.today())
# SCALES = {
#     'btcusd': (0.1, -8),
#     'googl': (0.1, -2),
#     'aapl': (0.1, -0.4),
#     'nflx': (0.1, -0.3)
# }
# x_scale, y_scale = SCALES.get(ticker.lower(), (0.1, -0.4))
# print(f'Scales X:{x_scale} Y:{y_scale}')