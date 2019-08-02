import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from fnmatch import fnmatch

df = pd.read_csv("/home/cong/PycharmProjects/hocpython/day4-9-7-19/movies.csv")
df["year"] = df["title"].apply(lambda x: x[-5:-1]) #lay ra nam tu` title
genres_list = df["genres"].apply(lambda x: x.split('|'))
#print(genres_list)
df_drama = df[df["genres"] == 'Drama']
print(df_drama)

s1 = Counter(df_drama["year"])
#print(s1.keys())
G = list(s1.keys())
#print(G)
H = []
for j in G:
    if j.isnumeric():
       H.append(j)
    else:
        pass

print(sorted(s1.values())[::-1])
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
so_nam = sorted(list(dedupe(H)))
print(so_nam)
aq1 = pd.DataFrame({
    'ngang': so_nam,
    'doc': sorted(s1.values())[::-1]
})
aq1.plot(kind='line', x='ngang', y='doc')
plt.show()
