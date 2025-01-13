# Uppgift 5
# Skapa en funktion filter_odd(numbers) som returnerar en lista med alla jämna tal från den givna listan.
 
def filter_odd(numbers: list) -> bool:
    return [num for num in numbers if num % 2 == 0]
 
 #returnerar alla jämna tal i listan
print(filter_odd([1, 2, 3, 4]))
print(filter_odd([1, 3, 5]))
print(filter_odd([]))