# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
 
def validate_password(password: str) -> bool:
 
    if len(password) < 8:     #om längden är under 8 så returneras false
        return False
   

    if not any(char.isdigit() for char in password): 
        return False

 #Lösenordet ska innehålla minst en siffra annars returneras false
    #char.isdigt kollar om det finns en siffra
    #for char in password går igenom varje tecken i lösenordet
    #any kollar om det är true
 
 
    return True 
#om båda kraven är korrekt så returneras True
 
 
print(validate_password("abc12345"))
print(validate_password("short"))      
print(validate_password("password1"))  
