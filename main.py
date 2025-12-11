"""
Sistema de análisis de noticias con APIs múltiples.
"""

# Imports organizados segun PEP 8
# PEP 8: Imports entandar primero, luego de terceros, luego locales
from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError
from news_analyzer.utils import get_sources

response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"{e}")

if response_data:
    sources_list = get_sources(response_data["articles"])
    for index, source in enumerate(sources_list, start=1):
        print(f"No:{index} -- {source}")

    for article in response_data["articles"]:
        print(article["title"])
