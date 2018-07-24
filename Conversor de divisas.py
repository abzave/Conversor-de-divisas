#Creado por: Abraham Meza
#Fecha de creación: 21/07/18
#Última modificación: 22/07/18
#Versión 3.7.0
import requests

url = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_CRC&compact=y"

def obtenerTipoDeCambio(url):
    """
    Entradas: url de tipo string
    Salidas: Tipo de cambio
    Funcionamiento: Hace una petición para obtener el tipo de cambio y lo devuelve
    """
    respuesta = requests.get(url)
    respuesta = respuesta.json()
    return respuesta['USD_CRC']['val']

def convertirCRCToUSD(cantidad, url):
    """
    Entradas: cantidad de tipo flotante y  url de tipo string
    Salidas: Cantidad pasada a dolares
    Funcionamiento: Divide cantidad entre el tipo de cambio y devuelve el resultado
    """
    tipoCambio = obtenerTipoDeCambio(url)
    return cantidad / tipoCambio

def convertirUSDToCRC(cantidad, url):
    """
    Entradas: cantidad de tipo flotante y  url de tipo string
    Salidas: Cantidad pasada a colones
    Funcionamiento: Multiplica la cantidad entre el tipo de cambio y devuelve el resultado
    """
    tipoCambio = obtenerTipoDeCambio(url)
    return cantidad * tipoCambio

def opcionCRCToUSD(url):
    """
    Entradas: url de tipo string
    Salidas: Imprime lo que devuelve convertirCRCToUSD
    Funcionamiento: Pide al usuario la cantidad a convertir e imprime lo que devuelve convertirCRCToUSD
    """
    try:
        cantidad = int(input('\nIngrese la cantidad en colones: '))
        dolares = convertirCRCToUSD(cantidad, url)
        print(cantidad, 'colones son', dolares, 'dolares\n')
    except:
        print('Error: Debe ingresar un nÃºmero')
        return opcionCRCToUSD(url)
    return

def opcionUSDToCRC(url):
    """
    Entradas: url de tipo string
    Salidas: Imprime lo que devuelve convertirUSDToCRC
    Funcionamiento: Pide al usuario la cantidad a convertir e imprime lo que devuelve convertirUSDToCRC
    """
    try:
        cantidad = int(input('\nIngrese la cantidad en dolares: '))
        dolares = convertirUSDToCRC(cantidad, url)
        print(cantidad, 'dolares son', dolares, 'colones\n')
    except:
        print('Error: Debe ingresar un nÃºmero')
        return opcionCRCToUSD(url)
    return

def opcionTipoCambio(url):
    """
    Entradas: url de tipo string
    Salidas: Imprime lo que devuelve obtenerTipoDeCambio
    Funcionamiento: Imprime lo que devuelve obtenerTipoDeCambio
    """
    tipoCambio = obtenerTipoDeCambio(url)
    print('\nEl tipo de cambio es de', tipoCambio, 'colones\n')
    return

if __name__ == '__main__':
    while True:
        print('1) Convertir de colones a dolares')
        print('2) Convertir de dolares a colones')
        print('3) Ver tipo de cambio')
        print('0) Salir')
        try:
            opcion = int(input('Ingrese una opción: '))
        except:
            print('Error: Debe ingresar un número')
            continue
        if opcion == 0:
            break
        elif opcion == 1:
            opcionCRCToUSD(url)
        elif opcion == 2:
            opcionUSDToCRC(url)
        elif opcion == 3:
            opcionTipoCambio(url)
        else:
            print('Error: Debe ingresar un número del 1 al 3')
