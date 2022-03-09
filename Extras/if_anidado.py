print('Bienvenido al control de acceso')
altura_string = input('Ingrese altura en cm:> ')
if altura_string.isnumeric() == True:
    altura_int = int(altura_string)
    if altura_int > 120:
        edad_string = input('Ingrese edad:>')
        if edad_string.isnumeric() == True:
            edad_int = int(edad_string)
            if edad_int > 18:
                print('Valor entrada 18')
            else:
                print('Valor entrada: $7')
        print('Gracias por elegirnos')
    else:
        print('Acceso Restringido')
    