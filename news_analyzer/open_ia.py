"""
Módulo para interactuar con la API de OpenIA y analizar artículos de noticias.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def analyze_with_openia(articles: list[dict], query: str) -> str | None:
    """
    Analiza el texto del artículo utilizando la API de OpenIA.

    Args:
        article_text (str): Texto del artículo a analizar.

    Returns:
        dict: Resultados del análisis proporcionados por la API de OpenIA.
    """
    client = OpenAI(
        api_key=os.environ.get("OPENIA_API_KEY"),
    )

    context = "\n".join(
        f"{article['title']}: {article.get('description', '')[:100]}..."
        for article in articles[:10]  # Limitar a los primeros 10 artículos
    )

    prompt = f"""
        Basado en los siguientes artículos de noticias:
        {context}

        Pregunta: {query}

        Responde de manera concisa y relevante en español.
    """

    print(prompt)

    response = client.responses.create(
        model="gpt-5",
        instructions="Analiza el siguiente texto y proporciona un resumen",
        input=prompt,
    )

    print(response.output_text)
