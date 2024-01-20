import requests
from config import url

def getCurrencyConversion(pair: str):
	res = requests.get(f"{url}/{pair}")
	return res.json()