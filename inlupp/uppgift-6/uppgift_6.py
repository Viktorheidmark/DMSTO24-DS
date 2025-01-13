
# Uppgift 6
# Skapa en funktion multiplication_table(n, limit) som returnerar multiplikationstabellen
# för n upp till limit i en lista.
 
 
 
def multiplication_table(n: int, limit: int) -> list:
    return [n * i for i in range(1, limit + 1)]  
#ista med multipler av n skapas
 
print(multiplication_table(2, 3))
print(multiplication_table(3, 5))