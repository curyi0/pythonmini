# 오라클 연동 쿼리 실행
from warnings import catch_warnings

import  cx_Oracle as cx

host_name= 'localhost'
oracle_port=1521
service_name='xe'

connect_info=cx.makedsn(host_name, oracle_port, service_name)
conn=cx.connect('education', '1234', connect_info) #db 사용 계정  /시퀀스 전에거(myboard
cursor=conn.cursor()
print("DB 연결됨")

#예시 데이터
SIGUN_NM='광명시' # 시군명
STR_NM='아들내미 떡볶이'  # 매장명
ADDR='경기도 광명시 오리로964번길 22-1'  # 도로주소명
INDUTYPE_NM='1인분,분식' #  업종명
LAT=37.4808602201   #위도
LOGT=126.8570411315  #경도

sql= """INSERT INTO delivery_apps(idx, SIGUN_NM ,SNAME, ADDR, INDUTYPE,LATITUDE,LONGITUDE) 
       VALUES (myboard_seq.nextval, :SIGUN_NM, :SNAME, :ADDR,:INDUTYPE,:LATITUDE,:LONGITUDE) """

try:
    cursor.execute(sql, SIGUN_NM=SIGUN_NM, SNAME=STR_NM, ADDR=ADDR,
                   INDUTYPE=INDUTYPE_NM, LATITUDE=LAT, LONGITUDE=LOGT)
    conn.commit()
    print("1개 업체 db추가 완료!")
except Exception as e:
    conn.rollback()
    print("쿼리문 오류 발생",e)

conn.close()