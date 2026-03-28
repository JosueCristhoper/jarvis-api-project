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

def send_solution(problem_id, query_sql) : 
    url = f"{url_base}/problem/solution/{problem_id}"
    data = {"solution": query_sql}

    try : 
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e : 
        print(f"Se ha producido un error al enviar: {e}")
        return None
    
if __name__ == "__main__" : 
    # Guardamos las sentencias SQL
    query_A =  '''SELECT location.name
                   FROM avenger
                   JOIN location ON avenger.current_location_id = location.id;'''
    
    query_B = '''SELECT location.name
                 FROM avenger_location_log
                 JOIN location ON avenger_location_log.location_id = location.id
                 GROUP BY location.name
                 HAVING COUNT(*) > 3;'''
    
    query_C = '''UPDATE stark_satellite
                 SET in_manintenance = 1
                 WHERE location_id IN (SELECT current_location_id
                                       FROM avenger);'''

    queries = [query_A, query_B, query_C]

    print("Sentencia SQL a JARVIS ")
    result = send_solution(2, queries)

    if result :
        print(result)