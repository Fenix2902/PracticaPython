# https://blog.hubspot.es/website/diccionario-python   Uso de diccionarios en Python
mesDelAño = input('Digita el mes del año a consultar: ')
diaDelMes = int(input('Digita el dia del mes: '))

def get_season(mesDelAño, diaDelMes):
    seasons = {
        ('enero', 'febrero', 'marzo'): "Invierno",
        ('abril', 'mayo', 'junio'): " Primavera",
        ('julio', 'agosto', 'septiembre'): "Verano",
        ('octubre', 'noviembre', 'diciembre'): "Otoño"
    }

    for key, value in seasons.items():
        if mesDelAño in key and diaDelMes >= 1 and diaDelMes <= 31:
            return value
    return "Fecha inválida"

season = get_season(mesDelAño, diaDelMes)
print(f"La estación del año para {mesDelAño}/{diaDelMes} es {season}.")