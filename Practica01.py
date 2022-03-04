# TODO: desarrollar un programa que recibe datos de una variable y los procesa:
# la variable es de tipo String
# Si es un numero asume que es la edad, la fecha de nacimiento o su dni
# dependiendo de lo que sea (edad, fecha nac., o dni) grabar en una variable con ese nombre
# Si no es un numero, formatear la cadena de texto como .title() guardandola en su propia variable
# Luego pedir que el usuario elija si quiere ver todos los datos de corrido (1) o si quiere
# todo separado (2). Imprimir toda la informacion dependiendo de la opcion elegida por el usuario.

# Version 0.1

# PROBLEMAS conocidos: codigo repetitivo/duplicado.
# La entrada de datos deberia ser de tipo list.
varInputN1 = '38'
varInputN2 = '20121980'
varInputN3 = '43098196'
varInputN4 = 'Romualdo Rafa Manguerto'

if varInputN1.isdigit() == True:
    if len(varInputN1) == 2:
        print('es edad')
        edad = varInputN1
    elif type(varInputN1 == int):
        print('es dni')
        dni = varInputN1
    else:
        print('es fecha')
        fecha = varInputN1

if varInputN2.isdigit() == True:
    if len(varInputN2) == 2:
        print('es edad')
        edad = varInputN2
    elif type(int(varInputN2)) == int:
        print('es dni')
        dni = varInputN2
    else:
        print('es fecha')
        fecha = varInputN2

if varInputN3.isdigit() == True:
    if len(varInputN3) == 2:
        print('es edad')
        edad = varInputN3
    elif type(varInputN3) == int:
        print('es fecha')
        fecha = varInputN3
    else:
        print('es fecha')
        fecha = varInputN3

if varInputN4.isdigit() == True:
    if len(varInputN3) == 2:
        print('es edad')
        edad = varInputN3
    elif type(varInputN3) == int:
        print('es fecha')
        fecha = varInputN3
    else:
        print('es fecha')
        fecha = varInputN3
else:
    nombre = varInputN4.title()
    print('es nombre')
    
# TODO: presentar la informacion filtrada:

