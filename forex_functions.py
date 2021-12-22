from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError

c = CurrencyRates()
s = CurrencyCodes()

def conversion(curr_from, curr_to, amount):
    """Converts a given amount from one currency to another"""
    floated_amount = float(amount)
    new_amount = round(c.convert(curr_from, curr_to, floated_amount), 2)
    return new_amount

def get_symbol(curr_to):
    """Gets the currecy symbol for the new currency"""
    new_symbol = s.get_symbol(curr_to)
    return new_symbol

currency_codes = ['EUR', 'IDR', 'BGN', 'ILS',
'GBP','DKK','CAD','JPY','HUF','RON','MYR',
'SEK','SGD','HKD','AUD','CHF','KRW','CNY',
'TRY','HRK','NZD','THB','USD','NOK','RUB','INR',
'MXN','CZK','BRL','PLN','PHP','ZAR']