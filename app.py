from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_functions import conversion, get_symbol, check_currency_code
import forex_python.converter

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def form():
    return render_template('form.html')


@app.route('/convert')
def convert():
    curr_from = request.args["curr-from"]
    curr_to = request.args["curr-to"]
    amount = request.args["amount"]
    try:
        new_amount = conversion(curr_from, curr_to, amount)
        symbol = get_symbol(curr_to)
        return render_template("result.html", new_amount=new_amount, symbol=symbol)
    except ValueError:
        flash(f"Invalid Amount: {amount}")
    except forex_python.converter.RatesNotAvailableError:
        if (check_currency_code(curr_from) == False):
            flash(f"Invalid Currency Code: {curr_from}")
        if (check_currency_code(curr_to) == False):
            flash(f"Invalid Currency Code: {curr_to}")
    return redirect('/')
    