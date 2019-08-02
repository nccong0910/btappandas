import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

df = pd.read_csv("/home/cong/PycharmProjects/hocpython/day4-9-7-19/movies.csv")
df["year"] = df["title"].apply(lambda x: x[-5:-1])

df_drama = df[df["genres"] == 'Drama']
#print(df_drama)
df_comedy = df[df["genres"] == 'Comedy']
#print(df_comedy)
df_documentary = df[df["genres"] == 'Documentary']
#print(df_documentary)
s1 = Counter(df_drama["year"])
s2 = Counter(df_comedy["year"])
s3 = Counter(df_documentary["year"])
#print(s1)
'''def ham(s,s0):
    for j in s0:
        if j.isnumeric():
            s.append(j)
        else:
            pass
ss1 = []
ss2 = []
ss3 = []
ham(ss1,s1)
ham(ss2,s2)
ham(ss3,s3)
print(ss1)'''
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
#print(list(dedupe(sorted(s1))))
#print(list(sorted(ss1)))

plt.plot(sorted(list(dedupe(s1))),sorted(list(s1.values())), label='drama')
plt.plot(sorted(list(dedupe(s2))),sorted(list(s2.values())), label='comedy')
plt.plot(sorted(list(dedupe(s3))),sorted(list(s3.values())), label='documentary')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("câu4_B1")
plt.legend()
plt.show()
