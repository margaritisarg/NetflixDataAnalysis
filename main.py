import numpy as np
import pandas as pd
#import pandas_profiling as pp

df = pd.read_csv('netflix_dataset/titles.csv')
df2 = df
df2 = df2.dropna()
#print(df.sort_values(by="imdb_score", ascending="False"))

hey = pd.pivot_table(df2, values = 'imdb_score', index=['title','genres', 'imdb_votes'], columns = 'type').reset_index()
print(hey)

#print( df2.loc[:, ["title", "type", "genres",  "release_year", "runtime", "imdb_score", "imdb_votes"]] )

