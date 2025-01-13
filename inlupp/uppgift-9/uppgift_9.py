# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en
#  given sträng är ett palindrom (dvs. samma framifrån och bakifrån).
 
 
def is_palindrome(string: str) -> dict:
    letter_count = {}  
   
    for char in string:  
        if char.isalpha():   
            char = char.lower()
            if char in letter_count:  
                letter_count[char] += 1
            else:  
                letter_count[char] = 1
   
    return letter_count
 #skapar en funktion för att kolla som värdet är samma åt båda hållen
 
print(is_palindrome(""))  
print(is_palindrome("radar"))  
print(is_palindrome("python"))

