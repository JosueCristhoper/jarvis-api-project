# JARVIS API Project - Infinity Gems

Este repositorio contiene la resolución de una serie de retos tecnicos de logica y programación realizados a través de una API REST. El proyecto se centra en la integración de servicios, procesamiento de datos y seguridad.

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

## Problema 1: Localización de Gemas del Infinito

### Descripción
El objetivo consiste en consumir un endpoint que devuelve una matriz de caracteres (sopa de letras) y programar un algoritmo capaz de localizar terminos específicos (Gemas del Infinito).

### Implementación Tecnica
Se ha desarrollado un algoritmo de búsqueda bidireccional:
* **Búsqueda Horizontal:** Análisis de cada fila mediante concatenación de caracteres.
* **Búsqueda Vertical:** Transposición lógica de la matriz para evaluar columnas como secuencias de texto independientes.

Una vez localizados los elementos, el sistema realiza una petición **POST** para validar la solución con el servidor.

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

## Instrucciones de Ejecución
Para iniciar los procesos de resolución:
* **Problema 1:** `python infinity_gems.py`
* **Problema 2:** `python avengers_db.py`