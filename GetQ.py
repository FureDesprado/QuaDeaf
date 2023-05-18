import requests


class CurrencyConverter:
    def __init__(self):
        self.currency_rates = {}
        self.get_currency_rates()

    def get_currency_rates(self):
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.currency_rates = data['rates']

    def convert(self, amount, from_currency, to_currency):
        try:
            if from_currency not in self.currency_rates or to_currency not in self.currency_rates:
                raise KeyError
            rate = self.currency_rates[to_currency] / self.currency_rates[from_currency]
            result = round(amount * rate, 2)
            return result
        except KeyError:
            print("Invalid currency code!")
            return None

def convert_currency():
    converter = CurrencyConverter()
    amount = float(input("Enter the amount of currency: "))
    from_currency = input("Enter the currency code you have: ").upper()
    to_currency = "USD"
    if from_currency not in converter.currency_rates:
        print("Invalid currency code.")
        return
    result = converter.convert(amount, from_currency, to_currency)
    if result is not None:
        print(f"{amount} {from_currency} is equal to {result} USD")

convert_currency()
