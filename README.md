# JARVIS API Project - Infinity Gems

Este repositorio contiene la resolución de una serie de retos técnicos de lógica y programación realizados a través de una API REST. El proyecto se centra en la integración de servicios, procesamiento de datos y seguridad.

---

## Tecnologías Utilizadas

* Lenguaje: Python 3.
* Librerías:
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

## Instrucciones de Ejecución
Para iniciar el proceso de resolución:
```bash
python infinity_gems.py
```