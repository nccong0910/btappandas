import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
df = pd.read_csv("/home/cong/PycharmProjects/hocpython/day4-9-7-19/movies.csv")


df["year"] = df["title"].apply(lambda x: x[-5:-1]) #tạo column year dùng hàm lambda tách ra khỏi cột title

'''df_1995 = df[df['year'] == '1995'] #chọn column year lấy năm 1995
#print(df_1995)
#genres_list = df_1995["genres"].apply(lambda x: x.split('|'))   #nam 1995'''
genres_list = df["genres"].apply(lambda x: x.split('|'))   #tat ca cac nam
#print(genres_list)
flat_list = [item for sublist in genres_list for item in sublist]   #list cac genres
#print(flat_list)
#s = Counter(flat_list)
s = Counter(flat_list)
print(sorted(s.values())[::-1])

#ham bo cac gia tri trung
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print(list(dedupe(flat_list)))

cc = pd.DataFrame({
    'Genres': list(dedupe(flat_list)),
    'Freq': sorted(s.values())[::-1]
})
cc.plot(kind='bar', x='Genres', y='Freq')
plt.show()
