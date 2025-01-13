# Uppgift 3
# Hitta det största talet i en lista

def max_in_list(numbers: list[int]) -> int:
    
    #Returnerar det största talet i listan.
    
    return max(numbers)

print(max_in_list([1, 2, 3]))
print(max_in_list([-5, 0, 5]))
print(max_in_list([10]))
