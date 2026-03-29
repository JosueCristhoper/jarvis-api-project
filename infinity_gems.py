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

def get_problem_data(problem_id):
    """Obtiene los datos del problemas desde la API de JARVIS."""
    url = f"{url_base}/problem/{problem_id}"

    try: 
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        # Imprimimos por si hay algun error
        print(f"Error en la conexion con la API: {e}")
        return None

def send_solution(problem_id, list_solution):
    """Envía la lista de gemas encontradas a la API mediante POST."""
    url = f"{url_base}/problem/solution/{problem_id}"
    # Procedemos a crear paquete de datos
    data = {"solution": list_solution} 

    try: 
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e: 
        print(f"Hay error al enviar la solucion: {e}")
        return None
    
def find_gems_in_matrix(matrix): 
    """Lógica para localizar las gemas dentro de la sopa de letras."""
    list_gems = ["SPACE", "MIND", "REALITY", "TIME", "POWER", "SOUL"]
    found = []
    size = len(matrix)

    # Buscamos en Horizontal
    for row in matrix:
    # Convertimos la lista separada en texto concatenado para facilitar la busqueda
        row_tex = "".join(row)
        for gema in list_gems: 
            if gema in row_tex: 
                found.append(gema)

    # Buscamos en Vertical
    for col in range(size): 
        # Procedemos a crear una palabra con las letras de arriba a abajo
        column_tex = "".join([matrix[row][col] for row in range(size)])
        for gema in list_gems :
            if gema in column_tex and gema not in found:
                found.append(gema)
    
    return found

    
if __name__ == "__main__":
    # Iniciamos problema 1
    data = get_problem_data(1)

    if data : 
        # Imprimimos por pantalla si la conexion fue realizado con exito
        print("*** Conexion exitosa ***")
        # Aqui vamos a extraer la matriz que nos dio la API
        matrix = data.get("matrix")

        # Procedemos a realizar comprobacion visual (Añadimos)
        for fila in matrix:
            print(" ".join(fila))

        results = find_gems_in_matrix(matrix)
        print(f"Gemas encontradas : {results}")

        # Procedemos a enviar la solucion
        print("\nEnviando respuesta a JARVIS...")
        result = send_solution(1, results)

        if result:
            print("*** Respuesta del Servidor ***")
            print(result)
