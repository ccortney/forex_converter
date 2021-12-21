from forex_python.converter import CurrencyRates, CurrencyCodes

c = CurrencyRates()
s = CurrencyCodes()

def conversion(curr_from, curr_to, amount):
    new_amount = round(c.convert(curr_from, curr_to, float(amount)), 2)
    return new_amount

def get_symbol(curr_to):
    new_symbol = s.get_symbol(curr_to)
    return new_symbol

def check_currency_code(currency):
    try: 
        c.get_currency_name(currency)
        return True
    except: 
        return False
    