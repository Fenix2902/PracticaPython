nivelAguaActual = int(input('Digita el nivel actual del agua en la represa: '))

# if nivelAguaActual>=450:
#     print("Nivel del agua muy alto de los limites recomendados")
# elif  nivelAguaActual>=200 and nivelAguaActual<450:
#     print ("el agua está en los límites recomendados.")
# elif nivelAguaActual<200 and nivelAguaActual>=0:
#     print ("Nivel del agua muy debajo de los limites recomendados")
# else:
#     print ('No se ha podido determinar el estado del agua')

print("Nivel del agua muy alto de los límites recomendados") if nivelAguaActual >= 450 else (print("el agua está en los límites recomendados.") if nivelAguaActual >= 200 else (print("Nivel del agua muy debajo de los límites recomendados") if nivelAguaActual >= 0 else print('No se ha podido determinar el estado del agua')))
