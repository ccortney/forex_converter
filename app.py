from logging import currentframe
from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import RatesNotAvailableError
from forex_functions import conversion, get_symbol, currency_codes

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def form():
    """Returns homepage with the form"""
    return render_template('form.html', currency_code=currency_codes)


@app.route('/convert')
def convert():
    """Returns the converted amount, if success. 
    Otherwise, redirects back to form with an error message."""
    curr_from = request.args["curr-from"]
    curr_to = request.args["curr-to"]
    amount = request.args["amount"]
    try:
        new_amount = conversion(curr_from, curr_to, amount)
        symbol = get_symbol(curr_to)
        return render_template("result.html", new_amount=new_amount, symbol=symbol)
    except ValueError:
        flash(f"Invalid amount, must be a number!")
    except RatesNotAvailableError:
        flash(f"One of your currency codes is currently not available!")
    return redirect('/')
    