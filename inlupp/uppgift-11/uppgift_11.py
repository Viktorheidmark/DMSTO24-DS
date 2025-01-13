# Uppgift 11
# Skapa en funktion word_count(text) som returnerar antalet ord i en given text.


def word_count(text: str) -> int:
 
    words = text.split()
 
    return len(words) 
 #return Len för att räkna ut antal ord
 
print(word_count("hello world"))
print(word_count(""))                          
print(word_count("Python är fantastiskt!"))