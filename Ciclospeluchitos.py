peluches =[
    'roshi',
    'conejito',
    'aguacatico'
]
print('')
print('pelucheria peluchitos')
print('...........................')
print('1. Agregar producto a la bodega')
print('2. Ver productos en bodega')
print('3. Obtener valor del inventario')
print('4. Ver productos más vendidos')
print('5. Salir')
print('')

opcion = 0

while opcion!=5:
    opcion=int(input('Digita un numero: '))
    if opcion==1:
        print('opcion uno')
    elif opcion==2:
        print('opcion dos')
    elif opcion ==3:
        print('opcion tres')
    elif opcion == 4:
        print('opcion cuatro')
    else: 
        if opcion>5:
            print('error de opcion')
print('Termino el programa gracias por visitarnos')
