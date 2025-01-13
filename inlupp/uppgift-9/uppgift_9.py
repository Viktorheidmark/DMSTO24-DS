# Uppgift 9
# Skapa en funktion is_palindrome(string) som kontrollerar om en given sträng är ett palindrom (dvs. samma framifrån och bakifrån).

def is_palindrome(string: str) -> bool:

    #tar bort mellanslag, punkt, komma tecken osv och gör alla till små bokstäver

    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())

    
    return cleaned_string == cleaned_string[::-1]
#skapar en omvänd kopia

 #returnerar True om strängen är ett palindrom annars false
print(is_palindrome("radar")) 
print(is_palindrome("python")) 
print(is_palindrome(""))  
