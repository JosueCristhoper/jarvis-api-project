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

# Primero intentamos ejecutar para poder ver los satelites de stark
if __name__ == "__main__" :
    print("Conectamos con los satelites de Stark...")
    list_satellites = get_satellites()

    if list_satellites : 
        print("Datos recibidos correctamente")
        print("Satelites encontrados: ", len(list_satellites))

        # Mostramos solo el primero para ver como vienen los datos (id, location, weather...)
        #print("Primer satelite :")
        #print(list_satellites[0])
        for s in list_satellites : 
            print("----------------------------------------------------------------------------------")
            print(s)
    
    else :
        print("No se pudo encontrar ningun satelite")