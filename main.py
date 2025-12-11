"""
Sistema de análisis de noticias con APIs múltiples.
"""

# Imports organizados segun PEP 8
# PEP 8: Imports entandar primero, luego de terceros, luego locales
from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError
from news_analyzer.open_ia import analyze_with_openia

response_data = None
try:
    response_data = fetch_news("newapi", api_key=API_KEY, query="Python")
except APIKeyError as e:
    print(f"{e}")

if response_data:
    print(
        analyze_with_openia(
            response_data.get("articles", []),
            query="Resumir las tendencias principales en las noticias sobre Python.",
        )
    )
