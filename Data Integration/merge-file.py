import pandas as pd

wiki_df = pd.read_csv('wikidata_data.csv')
dbpedia_df = pd.read_csv('dbpedia_data.csv')

wiki_clean = wiki_df[['filmLabel', 'actorLabel']].copy()
wiki_clean.columns = ['film', 'actor']

dbpedia_clean = dbpedia_df.copy()
dbpedia_clean['film'] = dbpedia_clean['film'].str.split('/').str[-1].str.replace('_', ' ')
dbpedia_clean['actor'] = dbpedia_clean['actor'].str.split('/').str[-1].str.replace('_', ' ')

combined_df = pd.concat([wiki_clean, dbpedia_clean], ignore_index=True)

combined_df['film'] = combined_df['film'].str.replace(r'\s\(film\)$', '', regex=True).str.strip()
combined_df['actor'] = combined_df['actor'].str.strip()

combined_df = combined_df.drop_duplicates(subset=['film', 'actor']).reset_index(drop=True)

combined_df.to_csv('combined_data_final.csv', index=False)