"""
Deficiones de excepciones personalizadas para el manejo de errores en la aplicación.
"""


class NewsSystemError(Exception):
    """Excepción base para errores en el sistema de noticias."""

    pass


class APIKeyError(Exception):
    """Excepción para errores relacionados con la clave de API."""

    pass
