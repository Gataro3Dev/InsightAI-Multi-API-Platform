"""Módulo para interactuar con APIs de noticias."""

import json
import urllib
import urllib.parse
import urllib.request
from typing import Callable

from .config import BASE_URL
from .exceptions import APIKeyError


def validate_api_key(api_key: str) -> bool:
    """Valida que la API key tenga formato correcto.

    Args:
        api_key (str): La API key a validar.
    Returns:
        bool: True si la API key es válida, False en caso contrario.
    """
    return len(api_key) > 10 and api_key.isalnum()


def guardian_client(api_key, section, from_date, timeout=30, retries=3):
    """
    Cliente para la API de The Guardian.
    Args:
        api_key (str): La API key para autenticación.
        section (str): Sección de noticias a consultar.
        from_date (str): Fecha desde la cual obtener noticias (formato YYYY-MM-DD).
        timeout (int, optional): Tiempo máximo de espera para la respuesta. Por defecto es
        30 segundos.
        retries (int, optional): Número de reintentos en caso de fallo. Por defecto
        es 3.
    Raises:
        APIKeyError: Si la API key no es válida o hay un error en la conexión
    Returns:
        dict: Datos de la respuesta en formato JSON.
    """
    return f"Guardian {section} desde {from_date} con timeout {timeout}"


def newsapi_client(api_key, query, timeout=30, retries=3):
    """
    Cliente para la API de NewsAPI.
    Args:
        api_key (str): La API key para autenticación.
        query (str): Término de búsqueda.
        timeout (int, optional): Tiempo máximo de espera para la respuesta. Por defecto es
        30 segundos.
        retries (int, optional): Número de reintentos en caso de fallo. Por defecto
        es 3.
    Raises:
        APIKeyError: Si la API key no es válida o hay un error en la conexión
    Returns:
        dict: Datos de la respuesta en formato JSON.
    """
    query_string = urllib.parse.urlencode({"q": query, "apiKey": api_key})
    url = f"{BASE_URL}?{query_string}"
    try:
        with urllib.request.urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except urllib.error.HTTPError:
        raise APIKeyError("Ocurrió un error, no se pudo conectar con la API")
    return f"NewsAPI: {query} con timeout {timeout}"


def fetch_news(api_name: str, *args: tuple, **kwargs: dict) -> dict:
    """
    Función que recibe el nombre de la API y sus parámetros, y llama al cliente
    correspondiente.
    Args:
        api_name (str): Nombre de la API a utilizar ("newapi" o "guardian
    """

    if api_name not in ("newapi", "guardian"):
        raise ValueError(f"API '{api_name}' no soportada.")

    base_config = {"timeout": 30, "retries": 3}
    config = {**base_config, **kwargs}
    api_clients: dict[str, Callable] = {
        "newapi": newsapi_client,
        "guardian": guardian_client,
    }
    client = api_clients[api_name]
    return client(*args, **config)