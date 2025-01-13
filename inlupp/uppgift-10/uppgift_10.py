# Uppgift 10
# Skapa en funktion celsius_to_fahrenheit(celsius) som konverterar en temperatur
# från Celsius till Fahrenheit.
 
 
 
def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = celsius * 9 / 5 + 32     
    return fahrenheit
 
 #Multiplicera celcius med värdet 9/5 och addera med 35 för att få fahrenheit
 
print(celsius_to_fahrenheit(0))    
print(celsius_to_fahrenheit(100))    
print(celsius_to_fahrenheit(-40))