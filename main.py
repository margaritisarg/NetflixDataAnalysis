import numpy as np
import pandas as pd
#import pandas_profiling as pp

df = pd.read_csv('netflix_dataset/titles.csv')
df2 = df
#df2 = df2.dropna()
#print(df.sort_values(by="imdb_score", ascending="False"))

#print(df2.columns)

#print(df2.head(50))

#hey = pd.pivot_table(df2, values = 'imdb_score', index=['title','genres', 'imdb_votes'], columns = 'type').reset_index()
#print(hey)

df3 = df2.loc[(df2["imdb_score"] >= 9) & (df2["type"] == "SHOW") & (df2["imdb_votes"] > 100) ] 
#df4 = df3.loc[df3["genres"] == "animation"]
#df3_not_include = df3.loc[~df3["title"].str.contains('Breaking')]

df4 = (df3.loc[:, ["title", "type", "imdb_score", "genres", "seasons", "imdb_votes"]]).sort_values("imdb_votes", ascending=False).head(10)
print( (df3.loc[:, ["title", "type", "imdb_score", "genres", "seasons", "imdb_votes"]]).sort_values("imdb_votes", ascending=False).head(10) )


series = (df4.loc[:, "genres"])
#for index, array in series.items():
#    print(f"{index}: {array}")

#print( series.loc["drama"] )
#print(len(df3.head(10)))

#print( df2.loc[:, ["title", "type", "genres",  "release_year", "runtime", "imdb_score", "imdb_votes"]] )

