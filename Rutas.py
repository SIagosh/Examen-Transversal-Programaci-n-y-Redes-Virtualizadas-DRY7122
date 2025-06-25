import urllib.parse
import requests

def obtener_ruta(origen, destino, transporte):
    """Obtiene los datos de la ruta desde la API de MapQuest"""
    
    main_api = "https://www.mapquestapi.com/directions/v2/route?"
    key = "C3eBuDL8KEXW33OtYpCoqaSI3bqFYZxr"  
    

    params = {
        "key": key,
        "from": origen,
        "to": destino,
        "locale": "es_ES",
        "unit": "k"
    }
    
    if transporte == "bicicleta":
        params["routeType"] = "bicycle"
    elif transporte == "peatonal":
        params["routeType"] = "pedestrian"
    
    url = main_api + urllib.parse.urlencode(params)
    response = requests.get(url)
    return response.json()

def mostrar_resultados(data, transporte):
    """Muestra los resultados de la ruta calculada"""
    
    if data["info"]["statuscode"] != 0:
        print("\nError al calcular la ruta:", data["info"]["messages"][0])
        return
    
    ruta = data["route"]
    
    print("\n" + "="*50)
    print(f"Viaje en {transporte} desde {ruta['locations'][0]['adminArea5']} (Chile) a {ruta['locations'][1]['adminArea5']} (Argentina)")
    print("="*50)
    
    # Conversión de unidades
    km = ruta["distance"] * 1.61
    millas = ruta["distance"]
    horas = int(ruta["time"] / 3600)
    minutos = int((ruta["time"] % 3600) / 60)
    
    print(f"\nDISTANCIA: {millas:.2f} millas | {km:.2f} kilómetros")
    print(f"DURACIÓN: {horas} horas y {minutos} minutos")
    
    # Narrativa del viaje
    print("\nINSTRUCCIONES DE VIAJE:")
    for i, paso in enumerate(ruta["legs"][0]["maneuvers"], 1):
        print(f"\nPaso {i}: {paso['narrative']} ({paso['distance']*1.61:.2f} km)")

def main():
    print("CALCULADOR DE RUTAS CHILE-ARGENTINA")
    print("="*50)
    
    while True:
        print("\nMedios de transporte disponibles:")
        print("1 - Automóvil")
        print("2 - Bicicleta")
        print("3 - Peatonal")
        print("S - Salir")
        
        opcion = input("\nElija medio de transporte (1-3) o S para salir: ").lower()
        
        if opcion == "s":
            print("\n¡Hasta luego!")
            break
        
        if opcion not in ["1", "2", "3"]:
            print("\nOpción no válida. Intente nuevamente.")
            continue
        
        transporte = "automóvil" if opcion == "1" else "bicicleta" if opcion == "2" else "peatonal"
        
        print(f"\nHa seleccionado viaje en {transporte}")
        origen = input("Ciudad de Origen (Chile): ")
        if origen.lower() == "s":
            break
            
        destino = input("Ciudad de Destino (Argentina): ")
        if destino.lower() == "s":
            break
        
        try:
            datos_ruta = obtener_ruta(origen, destino, transporte)
            mostrar_resultados(datos_ruta, transporte)
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Verifique su conexión a internet o los nombres de las ciudades.")

if __name__ == "__main__":
    main()