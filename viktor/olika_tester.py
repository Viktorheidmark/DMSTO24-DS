'''
import csv

data = [
   ["Name", "Age", "City"],
   ["Anna", 25, "Stockholm"],
   ["Björn", 30, "Göteborg"],
   ["Cecilia", 27, "Stockholm"],
]
with open("data1.csv", "w", newline="") as file:
   writer = csv.writer(file)
   writer.writerows(data)
'''

'''
# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list:

    if n <= 0:        
        return []   #om n är 0 eller negativt tal så returneras listan tom. 
    elif n == 1:
        return[0]
    elif n == 2:        
        return [0, 1]    #om n är ett så returneras det första talet i fibbonacci talföljden
    else:        
        fib_sequense = [0, 1]
        for i in range (2, n):
            fib_sequense [i - 1] + fib_sequense [i - 2]
            
        return fib_sequense
        
print(fibonacci(5))
print(fibonacci(0))
print(fibonacci(1))

'''
'''
   elif n == 2:        
        return [0, 1] 
Else: 
list_fib = [0, 1]
for i in range (2, n):
    print(f"index är: {1}")
list_fib.append
(list_fib (1 - 1) + list_fib (1 - 2)
)
return list_fib
'''


'''
def fibonacci(n, listan):
    fib = [ ]
    if n <= 1:
        fib.append(0)
        fib.append(1)
        return fib
    sequense = fibonacci (n - 1) + (n - 2)
    print( )
    fib.append(sequense)
    return fib

print(fibonacci(0))
'''


'''

def fibonacci(n, iteration):
    print(f"iteration: {iteration}, n är: {n}")
    iteration += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + (n - 2)
    

print(fibonacci(0, 1))
'''



'''
    sequense = fibonacci (n - 1) + (n - 2)
    print( )
    fib.append(sequense)
    return fib
    '''

'''
data = {
   "Name": ["Anna", "Björn", "Cecilia"],
   "Age": [25, 30, 27],
   "City": ["Stockholm", "Göteborg", "Malmö"]
}
'''


