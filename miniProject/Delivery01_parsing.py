import requests, json

url= "https://openapi.gg.go.kr/GGEXPSDLV?" #데이터api 주소
params=dict(
    Type='json',
    pSize='10',
    KEY='c66fd9599a564e698dfa68e3e20b3a80'
)

raw_data=requests.get(url=url, params=params)
binary_data= raw_data.content
json_data=json.loads(binary_data)
# print(json_data, end=' ') 데이터 변환 확인

for js in json_data['GGEXPSDLV'][1]['row']:
#        for i in datalist[js]['row']:
    SIGUN_NM=js['SIGUN_NM']
    STR_NM=js['STR_NM']   # 업체명
    REFINE_ROADNM_ADDR =js['REFINE_ROADNM_ADDR']   # 도로주소명
    INDUTYPE_NM =js['INDUTYPE_NM']   # 업종명
    LAT = js['REFINE_WGS84_LAT']  # 위도
    LOGT =js ['REFINE_WGS84_LOGT'] # 경도'''
    print(SIGUN_NM, STR_NM, REFINE_ROADNM_ADDR,INDUTYPE_NM,LAT, LOGT)