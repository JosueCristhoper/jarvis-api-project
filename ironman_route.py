# Para la conexion de la API reutilizaremos codigo de infinity_gems.py
import os
import requests
from dotenv import load_dotenv

# Cargamos variables de entorno desde .env
load_dotenv()

# Credenciales API REST (forma segura)
url_base = os.getenv("BASE_URL")
headers = {
    "candidate-key" : os.getenv("CANDIDATE_KEY")
}

# Ojo aqui con /problem/3 --> Antes puse /problem/get/3 y me dio un error found 404
def get_satellites():
    url = f"{url_base}/problem/3"
    response = requests.get(url, headers=headers)
    return response.json().get("satellites")

# Pasamos a '/where_is_ironman'
def get_location_ironman() :
    url = f"{url_base}/where_is_ironman"
    try : 
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("ironman_location")
    except Exception as e :
        print(f"Error al intentar localizar a Ironman: {e}")
        return None


# Primero intentamos ejecutar para poder ver los satelites de stark
if __name__ == "__main__" :
    print("Conectamos con los satelites de Stark...")
    list_satellites = get_satellites()

    # Creamos variable y guardamos la funcion get_location_ironman, para proceder realizar una condicion
    ironman_location = get_location_ironman()

    if list_satellites : 
        print("Datos recibidos correctamente")
        print("Satelites encontrados: ", len(list_satellites))

        # Mostramos solo el primero para ver como vienen los datos (id, location, weather...)
        #print("Primer satelite :")
        #print(list_satellites[0])
        for s in list_satellites : 
            print("----------------------------------------------------------------------------------")
            print(s)
        
        # Procedemos a imprimir la ubicacion de Ironman, llamamos la funcion
        if ironman_location :
            print(f"Ironman se encuentra en: {ironman_location}")
        else : 
            print(f"No se pudo localizar a Ironman...")
    
    else :
        print("No se pudo encontrar ningun satelite")

    # Calculamos la mejor ruta
    if list_satellites and ironman_location :
        # Pasamos la lista a un diccionario para la busqueda rapida
        sats_dict = {s["id"]: s for s in list_satellites}

        origin_location_id = 1 # Desde New York 
        intial_fuel = 100.0
        location_I = ["New York"]
        visited_ids = [1]

        print(f"Empezamos el viaje hacia: {ironman_location}...\n")

        # Realizamos bucle hasta llegar al destino teniendo combustible
        while sats_dict[origin_location_id]["location"] != ironman_location and intial_fuel > 0 : 

            near_sats = sats_dict[origin_location_id]["nearest_sats"]
            best_sat = None
            cost_min = 999 # Le ponemos un dato alto como referencia

            # Buscamos el satelite conectado mas barato
            for b_sat in near_sats :
                if b_sat not in visited_ids:
                    weather = sats_dict[b_sat]["weather"]
                    base_cost = 10.0

                    if weather == "Lluvia":
                        base_cost += 0.2
                    elif weather == "Viento en contra" :
                        base_cost += 1.5
                    elif weather == "Tormenta":
                        base_cost += 2.0

                    if base_cost < cost_min :
                        cost_min = base_cost
                        best_sat = b_sat

            # Si no encontramos ruta paramos
            if best_sat is None : 
                print("No hay satelites disponibles, nos detenmos")
                break

            # Realizamos el salto
            origin_location_id = best_sat
            # Guardamos ID para no volver
            visited_ids.append(best_sat)
            intial_fuel -= cost_min
            city = sats_dict[origin_location_id]["location"]
            location_I.append(city)

            print(f"Vamos a {city} (gastamos {cost_min}u)")

        # Resultado final
        print(f"\n** Resultado de la ruta **")
        print("Ruta recorrida: ", " = ".join(location_I))
        print("Combustible restante: ", round(intial_fuel,2))

        if sats_dict[origin_location_id]["location"] == ironman_location and intial_fuel >= 30 :
            print("Mision cumplida, buen reto")
        else:
            print("La mision fallo, el consumo total fue superior al que teniamos planteado utilizar.")





