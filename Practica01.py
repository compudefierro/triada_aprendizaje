# TODO: desarrollar un programa que recibe datos de una variable y los procesa:
# la variable es de tipo String
# Si es un numero asume que es la edad, la fecha de nacimiento o su dni
# dependiendo de lo que sea (edad, fecha nac., o dni) grabar en una variable con ese nombre
# Si no es un numero, formatear la cadena de texto como .title() guardandola en su propia variable
# Luego pedir que el usuario elija si quiere ver todos los datos de corrido (1) o si quiere
# todo separado (2). Imprimir toda la informacion dependiendo de la opcion elegida por el usuario.

# Para facilitar el desarrollo, ya se dan las variables de entrada:
varInputN1 = '38'
varInputN2 = '20121980'
varInputN3 = '43098196'
varInputN4 = 'Romualdo Rafa Manguerto'

class person1:
    age = varInputN1
    birthday = varInputN2
    id_n = varInputN3
    name = varInputN4.title()

print("Elije una opción para continuar:\n 1: Leer toda la información de Corrido\n 2: Leer toda la información por separado")
user = int(input("opción: "))
print()
if user == 2:
    print("Age:", person1.age)
    print("Birthday:", person1.birthday)
    print("Id Number:", person1.id_n)
    print("Name:", person1.name)
if user == 1:
    print(person1.age, person1.birthday, person1.id_n, person1.name)