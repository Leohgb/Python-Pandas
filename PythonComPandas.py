import pandas as pd
import json

df = pd.read_csv('tmdb_5000_credits.csv')
print(df.columns.tolist())

def extract_characters(cast_str):
    cast_list = json.loads(cast_str)
    return [actor['character'] for actor in cast_list]

for index, row in df.iterrows():
    title = row['title']
    characters = extract_characters(row['cast'])
    if index <= 10:
        for character in characters:
            print(f'{title} | {character}')
