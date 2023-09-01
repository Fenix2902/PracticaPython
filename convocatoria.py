#programa que permita registrar invitados a la fiesta
#ingresar gente
#ver quienes se apuntaron
#ver quienes pagaron
#ver quienes no pagaron
#cambiar información
#Retirarse
#salir

print('')
print('------FIESTA BESTIA-----')
print('************************')
print('0. Salir')
print('1. Registrar Invitado')
print('2. Ver lista invitados')
print('3. Ver invitados VIP')
print('4. Cobranza')
print('5. Editar información')
print('5. Retirar invitados')
print('************************')

opcion = 6
invitados =[]

while opcion!=0:
    invitado={ }
    opcion = int(input('Digita una opción: '))
    if opcion == 1:
        invitado['nombre'] = input('Ingrese su nombre: ')
        #invitado['id'] = range(1,10,1)
        invitado['id'] = input('Ingrese su codigo de invitación: ')#investigar para que sea aleatorio
        invitado['cedula'] = input('Ingresa tu numero de cedula: ')
        invitado['eps'] = input('Ingrese su EPS: ')
        invitado['pago'] =bool(input('Ya pago?: '))
        invitado['valorcuota'] = float(input('Ingrese su cuota: '))
        invitado['edad'] = int(input('Ingresa tú edad: '))
        
        invitados.append(invitado)
    elif opcion == 2:
        #recorriendo una lista
        for persona in invitados:
            print(f"***persona: {persona['nombre']}")
            print(f"***Id: {persona['id']}")
    elif opcion == 3:
        for persona in invitados:
            if persona['pago']==True:
                print(persona)
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass
    else:
        print('opcion invalida')
        
        #tareas:
        #como recibir los datos tipo booleano y que los guarde correctamente
        #Editar un dicionario dentro de una lista
        #Como eliminar un elemento