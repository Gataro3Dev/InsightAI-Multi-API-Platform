"""
Configuración para el analizador de noticias.
"""

import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://newsapi.org/v2/everything"
