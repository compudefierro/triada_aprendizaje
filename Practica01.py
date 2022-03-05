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
# Consejo: Usar funciones atomicas para los distintos procesos

# Formato entrada de datos estandarizada.
# datosEntrada = [edad:String, fecha:String, dni:int, nombre:String]
datosEntrada = ['38', '20121980', 43098196, 'Romualdo Rafa Manguerto']

# Funcion que recibe la lista, la procesa y retorna las variables

def proceso(lista):
    return lista[0],lista[1],lista[2],lista[3],
    
edad, fecha, dni, nombre = proceso(datosEntrada)        

    
# TODO: presentar la informacion filtrada:
# variables: edad, dni, fecha, nombre
print('=' * 10)
print(f'Bienvenido {nombre}!!')
print('=' * 10)
print('Elija una opcion: ')
print('1- Ver datos sin formato.')
print('2- Ver datos ordenados.')
print('-' * 10)
opcion = input('> ')
print(f'Opcion >{opcion}< ingresada.')
print('Procesando...')
print('*' * 10)
if opcion == '1':
    print(f'Datos: {edad} / {fecha} / {dni}')
elif opcion == '2':
    print(f'Nombre completo: {nombre}\n Edad: {edad}\n DNI Nro:{dni}\n Fecha Nacimiento: {fecha}')
else:
    print('Opcion inexistente...Chauuuuuuu')
