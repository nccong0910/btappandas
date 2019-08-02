import pandas as pd
import statistics as sts
from collections import Counter

df = pd.read_csv("/home/cong/PycharmProjects/hocpython/day4-9-7-19/movies.csv")
genres_list = df["genres"].apply(lambda x: x.split('|'))
print(list(genres_list))
S = []
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
#print(list(dedupe(genres_list)))

for i in genres_list:
    if "Adventure" in i:
        S.append(1)
    else:
        S.append(0)
print(S)
T = []
for i in genres_list:
    if "Fantasy" in i:
        T.append(1)
    else:
        T.append(0)
df2 = pd.DataFrame({
    'Adventure': S,
    'Fantasy': T
})
print(df2)
mean_X = sts.mean(S)
mean_Y = sts.mean(T)
#print(mean_X)
std_X = sts.stdev(S)
std_Y = sts.stdev(T)
print("độ lệch chuẩn Y: ", std_Y)
print("độ lệch chuẩn X: ", std_X)

#hàm tính covariance
def cov(x, y):
    for i in S:
        for j in T:
            return ((i - mean_X)*(j - mean_Y))/len(S)

GG = cov(S, T)
print("Covariance: ", GG)
cor = GG/(std_X*std_Y)

#hàm tính correlation
print("Hệ số tương quan 2 đại lượng : ",cor)
