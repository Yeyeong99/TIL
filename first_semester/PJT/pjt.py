import requests
import pprint

# 하드 코딩하는 변수
URL = 'https://fakestoreapi.com/carts' #요청 주소
data = requests.get(URL) #URL 주소에 요청을 보내는 메서드

print(data) 
# <Response [200]> -> 정상적으로 응답했다는 의미 / 404: URL이 잘못됨, 주소를 찾을 수 없음음
# print(type(data))

json_data = data.json()
print(json_data)

pprint.pprint(json_data) # dictionary를 정돈된 형태로 출력해줌
