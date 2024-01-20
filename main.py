import json
from httpservice import *

pairs = ['USD-COP', 'COP-USD']

def main():
	print('Bienvenido al conversor de moneda!!!')
	print('Que desea hacer?')
	print('[0] Convertir USD-COP\n[1] Convertir COP-USD \n[2] Dolar hoy')
	userOption = int(input())
	if userOption == 2:
		response = getCurrencyConversion('USD-COP')['USDCOP']['bid']
		print(f"La TRM de hoy es: {response}");
		return
	amount = int(input("Ingrese la cantidad: "))
	pair = pairs[userOption]
	response = getCurrencyConversion(pair)[pair.replace('-', '')]['bid']
	print(float(response) * amount)
	
main()