
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

## XML Path Language
