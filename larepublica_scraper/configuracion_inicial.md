# Configuración inicial del proyecto

1. Creamos una carpeta para el proyecto. En este caso larepublica_scraper

2. Iniciamos git con `git init`. Si lo ya tenemos iniciado, no lo hacemos.

3. Creamos el entorno virtual es:
    `$ python3 -m venv venv (Linux)`
    `$ py -m venv venv (Windows)`
    El ultimo venv es el nombre del entorno.

4. Creamos el archivo `.gitignore` porque no queremos trackearlo, ya que seria bastante pesado llevarlo al control de versiones. Escribimos en él la carpeta `/venv`

5. Activamos nuestro entorno virtual desde consola con:

    `$ ven\Scripts\activate (Windows)`
    `$ source venv/bin/activate (Linux)`

6. Si trabajas en VsCode. Creamos un Workspace para tener una estructura más organizada “save as workspace” y así tener un workspace para que VS tenga idea de qué tenemos en esta capeta.

7. Instalamos las dependencias de este proyecto:
   - Request: Para realizar peticiones
   - Lxml: Para utilizar Xpath
   - Autopep8: Ayuda a formatear el código según los estilos oficiales dle lenguaej,e

    `$ pip install requests lxml autopep8`
