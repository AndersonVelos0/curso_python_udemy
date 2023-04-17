'''
na classe a seguir, implemente o método `get_weather`, receba como parâmetro a 
temperatura do local em graus Fahrenheit, imprima `O clima é ideal para sair sem casaco` 
se a temperatura for maior ou igual a 65 graus Fahrenheit , 
caso contrário, imprima `Fique em casa, está frio lá fora`, 
antes de usar as condicionais converta esse valor para graus Celsius.
'''


class WeatherMachine:
    def get_weather(self, temperature):
        celsius_temp = (temperature - 32) * 5/9  
        if celsius_temp >= 18.3:
            print("O clima é ideal para sair sem casaco")
        else:
            print("Fique em casa, está frio lá fora")
weather_machine = WeatherMachine()
weather_machine.get_weather(100)