import pandas as pd

df = pd.read_csv('tmdb_5000_credits.csv')

print(df.head())

# Mostrar os dados das colunas 'title' e 'cast'
print(df[['title', 'cast']])

# Desafio: Demonstrar a disposição de nomes de alguns atores baseados em seus respectivos filmes
for index, row in df.iterrows():
    title = row['title']
    cast = row['cast']
    # Supondo que a coluna 'cast' contenha nomes separados por vírgula
    actors = cast.split(', ')
    for actor in actors:
        print(f'{title} | {actor}')