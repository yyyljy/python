from pprint import pprint
import requests
key = 'AIzaSyCGeHJGv4QmhCt6fyQNFiA-Yj4q1IN_30A'

# string interpolation
search = input("검색어를 입력해주세요 : ")
q = f'q={search}'
my_type = 'type=video'
part = 'part=snippet'
url = f'https://www.googleapis.com/youtube/v3/search?key={key}&{part}&{my_type}&{q}&maxResults=20'
print(url)

response = requests.get(url)
datas = response.json()
#pprint(data)

# 1. 검색어를 입력하면
# 2. 영상들을 검색할 것
# 그 영상들의 제목과 채널명

for data in datas['items'][:10]:
    print(data['snippet']['title'], end=' 채널명 : ')
    print(data['snippet']['channelTitle'])