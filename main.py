# main.py - Todo el código de un archivo

"""
Sistema de análisis de noticias con APIs múltiples.
"""

# Imports organizados segun PEP 8
# PEP 8: Imports entandar primero, luego de terceros, luego locales
import json
import urllib.parse
import urllib.request

# PEP 8: Configuración centralizada - constantes en MAYUS con guiones bajos
API_KEY = "0648a04244c24466bd7ac7a415bba91f"
BASE_URL = "https://newsapi.org/v2/everything"
API_TIMEOUT = 30
MAX_RETRIES = 3
DEFAULT_LENGUAGE = "ES"  # PEP 8: Comillas dobles para strings


# PEP 8: Utilidades comunes del proyecto - funciones en snake_case
def clean_text(text):
    # PEP 8: 4 espacios por indentación, no tabs
    """Limpia y normaliza texto."""
    if not text:
        return ""
    return text.strip().lower()


# PEP 8: Doble líneas en blanco entre funciones para separar lógicamente
def validate_api_key(api_key):
    """Valida que la API key tenga formato correcto."""
    return len(api_key) > 10 and api_key.isalnum()


# PEP 8: Funciones principales - agrupadas después de utilidades
def fecth_news_from_api(api_name, query):
    """Obtiene noticias de una API especifica."""
    pass


def process_article_data(raw_data):
    """Procesa datos crudos de articulo."""
    pass


def newsapi_client(api_key, query, timeout=30, retries=3):
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"

    with urllib.request.urlopen(url, timeout=timeout) as response:
        data = response.read().decode("utf-8")
        return json.loads(data)  # Parse JSON
        print(f"Response data: {data[:100]}...")  # Muestra los primeros 100 caracteres
    return f"NewsAPI: {query} con timeout {timeout}"


def guardian_client(api_key, section, from_date, timeout=30, retires=3):
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def ejemplo_args(api_key, *args):
    print(f"api_key: {api_key}")
    print(f"args: {args}")
    print(f"type args: {type(args)}")
    print("=====")


def ejemplo_kwargs(**kwargs):
    print(f"kwargs: {type(kwargs)}")
    print(f"kwargs: {kwargs}")
    print("=====")


def fetch_news(api_name, *args, **kwargs):
    """
    Función flexible para conectar con la API
    """
    base_config = {
        "timeout": 30,
        "retries": 3,
    }

    config = {
        **base_config,
        **kwargs,
    }

    api_clients = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }

    client = api_clients[api_name]
    return client(*args, **config)


response_data = fetch_news("newapi", API_KEY, "Python")
for article in response_data["articles"]:
    title = clean_text(article.get("title", ""))
    print(f"Title: {title}")
