"""
Demostación de cómo numerar elementos en una lista utilizando un contador manual y la función `enumerate`.
"""

from sample_data import sample_articles

counter = 1

for article in sample_articles:
    print(f"{counter}. {article['title']}")
    counter += 1

sample_articles_enum = enumerate(sample_articles, start=1)

for index, article in sample_articles_enum:
    print(f"{index}. {article['title']}")
