# JARVIS API Project - Infinity Gems

Este repositorio contiene la resolución de una serie de problemas tecnicos de logica y programación realizados a través de una API REST. El proyecto se centra en la integración de servicios, procesamiento de datos y seguridad.

---

## Tecnologías Utilizadas

* Lenguaje: Python 3.13.7
* Librerias:
    * requests: Comunicación con la API (métodos GET y POST).
    * python-dotenv: Gestión de variables de entorno y seguridad de credenciales.
* Herramientas de desarrollo: Git, VS Code.

---

## Configuración y Seguridad

Este proyecto sigue las mejores prácticas de seguridad, evitando la exposición de claves de acceso en el sistema de control de versiones.

### Requisitos previos
1. Instalacion de dependencias:

   ```bash
   pip install requests python-dotenv
   ```

2. Configuracion de credenciales:
    Crear un archivo llamado `.env`en el directorio raíz del proyecto con la siguiente estructura:

    ```text
    BASE_URL= https://jarvis.visiotechsecurity.com
    CANDIDATE_KEY= tu_clave
    ```

    El archivo `.env` está excluido del repositorio mediante `.gitignore`.

---

## Problema 1: Encontrar las Gemas del Infinito

### Descripción
El objetivo consiste en trabajar con un endpoint que devuelve una matriz de caracteres y programar un algoritmo capaz de encontrar ciertas palabras requeridas (Gemas del Infinito).

### Implementación Tecnica
Se implemento un algoritmo de busqueda en dos direcciones: 
* **Búsqueda Horizontal:** Recorri cada fila uniendo los caracteres para poder identificar las palabras dentro de ellas.
* **Búsqueda Vertical:** Converti las columnas en filas para poder analizarlas de la misma manera que las horizontales

Una vez encontré todas las palabras necesarias, envie el resultado al servidor mediante una petición  **POST** para comprobar si la solución era correcta.

---

## Problema 2: Bloquear el aviso a los vengadores (Base de Datos)

En este reto he tenido que trabajar con la base de datos de J.A.R.V.I.S. para sacar información de los Vengadores y gestionar el estado de los satélites de Stark.

### Implementación Técnica
Se desarrollaron tres consultas SQL para resolver las peticiones del sistema:

* **Consulta A (Conseguir el nombre de las ubicaciones actuales de los Vengadores):** He usado un `JOIN` para unir la tabla de Vengadores con la de localizaciones y así sacar el nombre real de donde se encuentran.
* **Consulta B (Conseguir el nombre de las ubicaciones donde ha estado un vengador más de 3 veces):** Para saber qué sitios visitan más, he agrupado los datos (`GROUP BY`) y contado las veces que aparecen, filtrando solo los que tienen más de 3 visitas con `HAVING`.
* **Consulta C (Marcar como en mantenimiento los satélites cuyas ubicaciones coincidan con la ubicación actual de los Vengadores. No se podrían bloquear todos ya que haría saltar las alarmas.):** Aqui he usado un `UPDATE` con una subconsulta para marcar como "en mantenimiento" solo los satélites que coinciden con la ubicación actual de los Vengadores.

Al final, envio estas tres sentencias en una lista a traves de un **POST** a la API, reutilizando la lógica de conexión segura que ya preparé en el primer problema.

---

## Problema 3: Pasar al ataque - Localizar a Ironman

En este problema, el objetivo era encontrar a Tony Stark usando la red de satélites y calcular la mejor ruta para llegar hasta él desde New York.

### ¿Cómo funciona mi solución?
He programado un sistema que no solo busca a Ironman, sino que decide la ruta paso a paso basándose en dos reglas muy sencillas:

1. **Radar de proximidad:** Lo primero que hace mi programa en cada parada es mirar si Ironman está en un satélite de al lado. Si lo ve, va directo a por él.
2. **Ahorro por clima:** Si Ironman todavia esta lejos, el programa mira el tiempo en los satélites cercanos y elige el que menos combustible gasta (porque no gasta lo mismo volar con clima despejado que con tormenta o lluvia).

### Puntos clave del proyecto:
* **Seguridad:** El programa recuerda por donde ha pasado para no quedarse dando vueltas en círculo (bucle).
* **Adaptabilidad:** No importa si Ironman se mueve o si el tiempo cambia; el código consulta la información en tiempo real antes de cada movimiento.
* **Eficiencia:** El sistema prioriza llegar al destino de la forma más lógica posible, adaptandose a cualquier cambio si en el futuro cambia el origen de partida y e destino, incluso si se modifica los satelites.
* **Reporte de Telemetría:** Una vez alcanzado el objetivo o finalizada la ruta, el sistema envía un informe final a la API de Stark que incluye la ruta completa recorrida y el combustible restante, asegurando que J.A.R.V.I.S. tenga los datos actualizados.

---

## Instrucciones de Ejecución
Para ver los resultados en la consola, solo hay que ejecutar:
* **Problema 1:** `python infinity_gems.py`
* **Problema 2:** `python avengers_db.py`
* **Problema 3:** `python ironman_route.py`