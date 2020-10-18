import requests
import lxml.html as html

# Constantes
HOME_URL = 'https://www.larepublica.co/'

XPATH_LINK_TO_ARTICLE = '//div/a[contains(@class, "kicker")]/@href'
XPATH_TITLE = '//div[@class="mb-auto"]/h2/a/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_AUTHOR = '//div[@class="autorArticle"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p[not(@class)]/text()' 

def parse_home():
    ''' Para extraer los link de las noticias'''

    # Creamos un bloque try para manejar los errores. Y manejar los Status Code.
    try:
        response = requests.get(HOME_URL)

        # Lógica para traer los links.
        if response.status_code == 200:
            # .content trae  el HTML que necesita ser traducido con un decode para que python lo entienda
            # en terminos de caracteres, me devuelve un string que noes más que el HTML crudo.
            home = response.content.decode('utf-8')

            # En esta línea uso el parser para transformar el contentido
            # html a un archivo que sea de utilidad para las expresiones xpath
            parsed = html.fromstring(home)

            # En esta línea estoy usando el archivo parseado con la función xpath y le paso por parámetro mi constante
            # la cual almacena la expresión Xpath.
            links_to_notices = parsed.xpath(XPATH_LINK_TO_ARTICLE)
            
            # For debugg
            # print(len(links_to_notices))
            # print(type(links_to_notices))
            # print(links_to_notices)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    ''' Función principal que se va a correr cuando ejecutemos el archivo'''
    parse_home()


if __name__ == '__main__':
    run()