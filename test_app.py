from app import app, form
from unittest import TestCase
import forex_functions

class ConversionTestCase(TestCase):
    """Testing forex_functions.conversion()
    Because rates change daily, we will test that 1 USD converts to 1 USD"""
    def test_conversion(self):
        self.assertEqual(forex_functions.conversion('USD', 'USD', 1), 1)

class SymbolTestCase(TestCase):
    """Testing forex_functions.get_symbol()"""
    def test_get_symbol(self):
        self.assertEqual(forex_functions.get_symbol('USD'), '$')
        self.assertEqual(forex_functions.get_symbol('GBP'), '\xa3')
        self.assertEqual(forex_functions.get_symbol('GBP'), '£')

class FormTestCase(TestCase):
    """Testing that the form appears on the homepage"""
    def test_homepage(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
        
        self.assertEqual(res.status_code, 200)
        self.assertIn('<label for="curr-from">', html)
    
class FormSubmitTestCase(TestCase):
    def test_form_submit(self):
        """Testing that the form submits properly"""
        with app.test_client() as client:
            res = client.get('/convert', query_string = {'curr-from': 'USD', 'curr-to': 'USD', 'amount': 1})
            html = res.get_data(as_text=True)
        
            self.assertEqual(res.status_code, 200)
            self.assertIn('1', html)
            self.assertIn('$', html)
    
    def test_form_redirection(self):
        """Testing that the form redirects properly"""
        with app.test_client() as client:
            res = client.get('/convert', query_string = {'curr-from': 'USD', 'curr-to': 'USD', 'amount': '2,000'})
        
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')
    
    def test_form_redirection_followed(self):
        """Testing that the form redirects properly when amount is a string"""
        with app.test_client() as client:
            res = client.get('/convert', query_string = {'curr-from': 'USD', 'curr-to': 'USD', 'amount': '2,000'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p>Invalid amount, must be a number!</p>', html)



