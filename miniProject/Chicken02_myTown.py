# -*- coding: utf-8 -*-
import squarify
import pandas as pd
import  matplotlib.pyplot as plt
from matplotlib import font_manager, rc

data=pd.read_excel('../resData/서울특별시중구_일반음식점.xlsx',engine='openpyxl')
print(data)
list={'location': data['소재지전체주소'], 'restname':data['사업장명']}
for l in list:
    for i in range(10):
        print(list[l][i])
df=pd.DataFrame(list)
print(df)

donglist=[]
galist=[]


#주소명에 '동',  '가'둘을 나누든지 , 하나 버리든지
location=df['location']
print(location.range.index)
for loc in location:
   # print(set(loc))
    loc=loc.split('중구')[1]
    dong=loc.split('동')[0]
    print(dong)##           동 개수가 너무 많음
    if (loc.find('가')==True):
        continue 
    #print(loc)
    donglist.append(dong)
    #galist.append(ga)
print(donglist)
print(galist)
        
plt.style.use('ggplot')
font_name=(font_manager.FontProperties(fname="../resData/malgun.ttf").get_name())
rc('font', family=font_name)

df["label"]=df['location']+"\n(" + df['치킨집개수'].astype(str) +")"
squarify.plot(sizes=df[''], label=df['label'], alpha=.8)
plt.axis('off')
plt.show()