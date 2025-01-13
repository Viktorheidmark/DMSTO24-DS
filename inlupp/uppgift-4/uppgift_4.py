# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(n: int) -> list:

    if n <= 0:        
        return []   #om n är 0 eller negativt tal så returneras listan tom. 
    elif n == 1:        
        return [0]    #om n är ett så returneras det första talet i fibbonacci talföljden
    else:        
        list_fib = [0, 1]    #start värderna i talföljden    
        while len(list_fib) < n:    #while len ger längden på listan
             next_fib = list_fib[-1] + list_fib[-2]      #Senaste två talen      
             list_fib.append(next_fib)        
    return list_fib

print(fibonacci(5))
print(fibonacci(0))
print(fibonacci(1))

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
