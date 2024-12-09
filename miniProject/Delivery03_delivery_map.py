from sys import exception

import folium
import cx_Oracle as cx

host_name= 'localhost'
oracle_port=1521
service_name='xe'

connect_info=cx.makedsn(host_name, oracle_port, service_name)
conn=cx.connect('education', '1234', connect_info) #db 사용 계정  /시퀀스 전에거(myboard
cursor=conn.cursor()
print("DB 연결됨")

# search=input("시(또는군)명을 입력하세요._ ")
restLoc=folium.Map(location=[37.40,127.38], zoom_start=12)
# restLoc.save('../savefiles/restaurant_Locate.html')

sql="select * from  delivery_apps order by idx asc"
cursor.execute(sql)
# while
for rs in cursor:
    search = input("시(또는군)명을 입력하세요._ ").strip()
    idx=rs[0]
    sigun=rs[1]
    sname=rs[2]
    addr=rs[3]
    indutype=rs[4]
    latitude=rs[5]
    longitude=rs[6]
    folium.Marker([latitude,longitude], popup=sname).add_to(restLoc)
    print(search, sigun)
    if (search==sigun):
        try:
            query="select * from delivery_apps where SIGUN_NM like :search_param ".format(search)
            cursor.execute(query, search_param=f"%{search}%")
            restLoc.save(f"../savefiles/{search}_deliver_marker.html")
            print("검색한 시의 식당을 찾았어요!")
        except Exception as e:
            print("")
            conn.rollback()

    elif (search!=sigun):
         print("시(군)명을 다시입력하세요")
         break
# restLoc.save('../savefiles/restaurant_deliver_marker.html')
# print('배달 맵 생성됨~')