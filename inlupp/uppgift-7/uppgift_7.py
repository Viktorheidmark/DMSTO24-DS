# Uppgift 7
# Skapa en funktion validate_password(password) som kontrollerar att lösenordet är minst 8 tecken långt och innehåller minst en siffra.
 
def validate_password(password: str) -> bool:
 
    if len(password) < 8:     #om längden är under 8 så returneras false
        return False
   

    if not any(char.isdigit() for char in password): #Lösenordet ska innehålla en siffra minst
        return False
    
    #char.isdigt kollar om det finns en siffra
    #for char in password går igenom varje tecken i lösenordet
    #any kollar om det är true
 
 
    return True 
#Returneras True ifall båda villkoren är korrekt
 
 
print(validate_password("abc12345"))
print(validate_password("short"))      
print(validate_password("password1"))  