
<div align="center">
    <h1>Fundamentos de Web Scraping con Python y Xpath</h1>
    <img src="https://imgur.com/HHFGhMw.png" width="">
</div>

## Introducción al documento

El contenido de este documento son **apuntes prácticos** del [Curso de Fundamentos de Web Scraping con Python y Xpath](https://platzi.com/cursos/web-scraping/) y busca ser una guía para futuros trabajos personales. El mismo está dictado por [Facundo García Martoni](https://twitter.com/facmartoni), Technical Mentor en Platzi. El curso es de [Platzi](https://platzi.com).

Con el curso se trata de aprende las bases de la extracción de datos en Internet y decubrir cómo funciona una aplicación de Web Scraping internamente. Se desarrollan scripts a través de herramientas como Python y las DevTools del navegador.

## Objetivos del documento

- Crear un scraper de noticias
- Utilizar XML Path Language
- Conocer los fundamentos de la web
- Aprender los conceptos básicos de Web Scraping

## Tabla de contenido
- [Fundamentos de Web Scraping con Python y Xpath](#fundamentos-de-web-scraping-con-python-y-xpath)
  - [Introducción al web scraping](#introducción-al-web-scraping)
    - [¿Qué es el web scraping?](#qué-es-el-web-scraping)
    - [¿Por qué aprender web scraping hoy?](#por-qué-aprender-web-scraping-hoy)
    - [Python: el lenguaje más poderoso para extraer datos](#python-el-lenguaje-más-poderoso-para-extraer-datos)
      - [Principales frameworks(librerias) en python](#principales-frameworkslibrerias-en-python)
      - [Herramientas de web scrapping](#herramientas-de-web-scrapping)
      - [Otras librerais y otros lenguajes](#otras-librerais-y-otros-lenguajes)
  - [Fundamentos de la web](#fundamentos-de-la-web)
    - [Entender HTTP](#entender-http)
    - [¿Qué es HTML?](#qué-es-html)
    - [Robots.txt: permisos y consideraciones al hacer web scraping](#robotstxt-permisos-y-consideraciones-al-hacer-web-scraping)
  - [XML Path Language](#xml-path-language)

# Fundamentos de Web Scraping con Python y Xpath

## Introducción al web scraping

### ¿Qué es el web scraping?

![web_scrapping](https://imgur.com/A2tL463.png)

**[Web scraping](https://es.wikipedia.org/wiki/Web_scraping)** es una técnica usada por data scientists y backend developers para extraer información de internet, accede a esto usando el protocolo de tranferencias de hipertexto (HTTP) o a través de un navegador. Los datos extraídos usualmente son guardados en una base de datos, incluso en una hoja de cálculo para posteriores análisis. Puede hacerse de manera automática (bot) o manualmente.

**[Xpath](https://es.wikipedia.org/wiki/XPath)** es un lenguaje que sirve para apuntar a las partes de un documento XML. Xpath modela un documento XML como un árbol de nodos. Existen diferentes tipos de nodos: elementos, atributos, texto.

### ¿Por qué aprender web scraping hoy?

Las agencias de seguridad, aplicaciones que comparan precios más baratos entre hoteles, apliaciones de ecommerce que comparan precios entre diferentes competidores usan web scraping. Las agencias de marketing para analziar el contenido de tweets que se vuelven virales. En general el web scraping es una habilidad muy valiosa para cuando no tienes acceso a una API.

Es posible realizar web scraping con diferentes lenguajes de programación, como R o Js (y sus respectivas librerías) sin embargo Py es por excelencia el lenguaje de programación para esta tarea. Cuenta con la comunidad más grande para implementarlo.

### Python: el lenguaje más poderoso para extraer datos

Python es el lenguaje que mas soporte tiene en el mundo open source y en general para realizar este tipo de técnicas. Existen una cantidad de módulos para realizar por ti mismo web scrapping. Python es uno de los lenguajes que esta mas especializado para hacer ciencia de datos. Por lo tanto para los cienctificos de datos esto es una ventaja grande. Si eres backend developer y trabajas con Django puedes nuclear el conocimiento de web scraping con Django y realizar un proyecto sin irse de lenguaje en lenguaje. 

#### Principales frameworks(librerias) en python

- [Request](https://requests.readthedocs.io/es/latest/)
  - Es una librería que nos permite controlar HTTP. El conjunto de reglas o protocolos de comunicación.

  - "El gobierno de su Majestad, Amazon, Google, Twilio, Mozilla, Heroku, PayPal, NPR, Obama for America, Transifex, Native Instruments, The Washington Post, Twitter, SoundClound, Kippt, Readability y algunas organizaciones Federales de los Estados Unidos de América utilizan Requests internamente. Ha sido descargado más de 8,000,000 de veces desde PyPI. "

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
  - Es una libería de pyhton qué nos sirve para extraer información HTML y XML.  
  - Recibe este nombre debido a un poema con el mismo nombre de Lewins Carroll en Alicia en el pais de la maravillas.

    >"Beautiful Soup, so rich and green, Waiting in a hot tureen! Who for such dainties would not stoop? Soup of the evening, beautiful Soup! "

- [Selenium](https://selenium-python.readthedocs.io/)
  - Podemos crear navegadores fantasmas para controlar sitios web de manera automática. Bots.

- [Scrapy](https://scrapy.org/)
  - Permite escribir reglas para extraer los datos, es extensible por diseño,
es rápido y simple. Es usado por el UK para recolectar datos de la población.

#### Herramientas de web scrapping

Los siguientes son soluciones que no necesitan codear, y que en su mayoría tienen un propósito específico.
Enfocados ecomerce o a funciones como tomar screenshots de PDFs. Automatizar y agendar actividades, y las soluciones están dadas como pluggins en el navegador hasta servicios.

- [ParseHub](https://parsehub.com/)
- [webscraper.io](https://www.webscraper.io/)

#### Otras librerais y otros lenguajes

- [Rvest](https://www.datanalytics.com/libro_r/web-scraping.html) Es una librería inspirada en Beautiful soup, diseñada para cosechar y recolectar datos de HTML. Se usa en R studio.

- [Puppeteer](https://pptr.dev/) Es una librería de Js que puede usarse para diferentes propósitos entre los cuales el webscrapping es uno.

## Fundamentos de la web

### Entender HTTP

[El protocolo HTTP](https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto) es conjunto de reglas por el cual dos computadoras se comunican. Un cliente y un servidor. El cliente realiza peticiones a servidores.

Una petición se vería de la siguiente manera:

```shell
# Request
GET / HTTP/1.1
Host: developer.mozilla.org  Accept-Language: fr

# Response  
HTTP/1.1 200 OK
Date: Sat, 09 Oct 2010 14:28:02 GMT
Server: Apache
Last-Modified: Tue, 01 Dec 2009 20:18:22 GMT  ETag: "51142bc1-7449-479b075b2891b"
Accept-Ranges: bytes  Content-Length: 29769  Content-Type: text/html
<!DOCTYPE html... (here comes the 29769 bytes of the  requested web page)
```

**HEADERS**

Permiten al cliente y el servidor passar información adicional con un request o response HTTP.

Pueden agruparse en las siguientes categorías:

- **Generales** : Aplica para request y responses pero no tiene relación con la data transmitida en el cuerpo
- **Request** : Contienen más información acerca del recurso a ser fetch (extraer)
- **Response** : Contiene información adicional sobre respuestas. Como ubicación o el Server provider.
- **Entity** : Contien información acerca del recurso del cuerpo.

Existen muchas cabeceras o headers como:

- **Accept**
- **Authorization**
- **Link**
- **Location**
- **Save-Data**

Puedes consultar aquí toda la [documentación sobre las cabeceras o Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

HTTP nos permite transportar, HTML, CSS, webAPIs, Js. Se vale de protcolos como IP, TCP, UDP para comunicarse con el servidor, mediante TLS se hace la encriptación. Y el DNS asigna nombres a direcciones IP.

![protocolos_web](https://imgur.com/1PgtKGm.png)

**STATUS CODE**:

Los estados son la forma en que el servidor da respuesta de las peticiones.

1. Respuestas informativas (100–199).
2. Respuestas satisfactorias (200–299).
3. Redirecciones (300–399).
4. Errores de los clientes (400–499).
5. Errores de los servidores (500–599).

[Documentación de Mozilla sobre STATUS CODE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

**MANEJO DE STATUS CODES**

Una opción rápida para manejar los STATUS CODE es usar la librería **Request**.

1. Abre un ambiente virtual.
2. En la carpeta de trabajo: `pip install request`

Luego en pyhton:

```py

# Una idea sobre el manejo de los status Code.

import requests

response_platzi = requests.get('https://api.platzi.com')
print(response_platzi)
# <Response [404]>

if response_platzi.status_code == 200:
    print("Aquí tienes lo que buscas")
elif response_platzi.status_code == 400:
    print("Ups, no puedo darte nada en el momento. Nosotros nunca paramos de mejorar <3")
```

Un artículo para profundizar en cómo manejar la librería request y como manejar los status code [Request Tutorial](https://realpython.com/python-requests/#status-codes)

### ¿Qué es HTML?

[HTML](https://es.wikipedia.org/wiki/HTML) es una lenguaje que permite definir la estructura de una página web. Estrucutra, estilo, partes interactivas. En el contexto de webscraping HTML es muy importante.

**Etiquetas** está encerrado en angle brakets **< >**. Una etiqueta puede contener a otras etiquetas, las etiquetas tienen **atributos**.

El conocimiento de los **atributos** es crucial porque con ellos podremos conectar el scraper para extraer información.

La siguientes etiquetas son importantes para el web scraping y por ende se explican:

- **[< script >](https://developer.mozilla.org/es/docs/Web/HTML/Elemento/script)**: Se utiliza para insertar o hacer referencia a un script o código que ejecuta una acción dentro de un docuemnto HTML.
- **[< meta >](https://es.wikipedia.org/wiki/Etiqueta_meta)**: Los metadatos son atributos que no se muestran en la página web, pero que sirven para identificar cosas como el autor de la página, el lenguaje en que está escrito, palabras clave para que los motores de búsqueda las indexen etc. Aporta información extra al documento. Aunque no son visibles al usuario de un sitio web si se pueden analizar de forma automática por código.
- **[< iframe >](https://developer.mozilla.org/es/docs/Web/HTML/Elemento/iframe)**: Representa un contexto de navegación anidado, el cual permite incrustrar otra página HTML en la página actual.

### Robots.txt: permisos y consideraciones al hacer web scraping

Los archivos [robots.txt](https://support.google.com/webmasters/answer/6062608?hl=es&ref_topic=6061961) exiten como una forma de administrar una página web. Proporciona información a los rastreadores de los buscadores sobre las páginas o los archivos que pueden solicitar o no de tu sitio web.
Principalmente, se utiliza para evitar que tu sitio web se sobrecargue con solicitudes.

En el contexto de webscraping, le dice al scraper que puede y no extraer. Es decir hasta donde puede llegar. Ya que infrigir en la violación
de estas directivas puede acarrear un problema legal con el sitio web al que estamos scrapeando.

**robots.txt** Contiene entre otros elementos:

**USER-AGENT**: Identificadores de quienes acceden a tu sitio web, puede ser un `archivo.py` hasta un googlebot.

**DIRECTIVAS**

- **ALLOW**: Utiliza esta directiva para permitir a los motores de búsqueda rastrear un subdirectorio o una página, incluso en un directorio que de otro modo no estaría permitido.
- **DISALLOW**: Utiliza esta directiva para indicar a los motores de búsqueda que no accedan a archivos y páginas que se encuentren bajo una ruta específica.

--------------
Ejemplo:

```shell
url/robots.txt
Por ejemplo:

# Robots.txt file from http://www.nasa.gov
#
# All robots will spider the domain

User-agent: *
Disallow: /worldbook/
Disallow: /offices/oce/llis/

```
---------------
Para conocer más información de [robots.txt](https://ahrefs.com/blog/es/robots-txt/).

-------

Resumen de la sección anterior para introducirnos en la siguiente:

Se aprendio como esta conformada la estructura de un sitio web.

Sabemos que es HTTP, el protocolo de transferencia de hipertexto, el cual nos permite comunicar un cliente y un servidor en la red. En esta comunicación el servidor nos envia un documento de tipo HTML.

En este documento se define la estructura de un sitio web. Sabemos como esta conformada esta estructura y como contruir una.  

Se analizo el archivo **robots.txt**, el cual define las reglas para poder extrar información o no, dependiendo sea el caso, de un sitio web.

Sabiendo lo anterior veremos Xpath, XML Path Language.

## XML Path Language
