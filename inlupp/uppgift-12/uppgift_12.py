# Uppgift 12
# Skapa en funktion create_student_register(students) som tar emot en lista
# med namn och ålder och returnerar en dictionary där namnet är nyckeln och åldern är värdet.


def create_student_register(students: list) -> dict:
 
    student_register = {} #för att skapa en tom lista
   
 
    for name, age in students:
        student_register[name] = age
   
    return student_register
 
 
students_list = [("Anna", 20), ("Bertil", 25), ("Cecilia", 22)]
print(create_student_register(students_list))  