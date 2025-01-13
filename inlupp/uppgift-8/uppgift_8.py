# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary 
# med varje bokstav som nyckel och antalet förekomster som värde.
 
 
def count_letters(string: str) -> dict:

    letter_count = {}  # Skapar en tom dictionary 

    for char in string:  #Går igenom varje tecken i strängen
        if char.isalpha():  
            char = char.lower()  
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
   
    return letter_count
 
 
print(count_letters("hello"))
print(count_letters(""))
print( count_letters("aaa"))
