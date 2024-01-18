#https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL

import requests
import json

def quotes():
    """
    Query a quote API and return a string with the dollar, euro and bitcoin quotes
    """
    request_quotes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    prices = json.loads(request_quotes.text)
    
    quotes_log = "QUOTES\n"
    quotes_log += "\n"
    quotes_log += "dollar: " + prices["USDBRL"]["ask"] + "\n"
    quotes_log += "BTC: " + prices["BTCBRL"]["ask"] + "\n"
    quotes_log += "Eur:  " + prices["EURBRL"]["ask"]
    
    return quotes_log
 
def climate(local):
    """
    query a climate API and returns a string with climate and temperature of a local.
    """
    request_climate = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=30bc4efcb11c829301b50208ea6aca20")
    
    climate = json.loads(request_climate.text)
    
    climate_log = "CLIMATE: \n\n"
    
    climate_log += local+"\n"
    climate_log += climate["weather"][0]["main"] + ": " + climate["weather"][0]["description"] + "\n"
    climate_log += "temperature: \n"
    
    min_temp = float(climate['main']['temp_min'] -32) / 1.8
    max_temp = float(climate['main']['temp_max'] -32) / 1.8
    climate_log += f"\tMin: {min_temp:.2f}\n"
    climate_log += f"\tMin: {max_temp:.2f}\n"
    
    return climate_log

print(quotes())
print("-"*50 )
print(climate("sao paulo"))