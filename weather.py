import requests
import re

url = "https://www.weather.go.kr/w/rss/dfs/hr1-forecast.do?zone=4623054000"
response = requests.get(url)

wfor = re.findall("<wfKor>(.+)</wfKor>", response.text)[0]
temp = re.findall("<temp>(.+)</temp>", response.text)[0]
humi = re.findall("<reh>(.+)</reh>", response.text)[0]

wfor2 = re.findall("<wfKor>(.+)</wfKor>", response.text)[24]
temp2 = re.findall("<temp>(.+)</temp>", response.text)[24]
humi2 = re.findall("<reh>(.+)</reh>", response.text)[24]

print("=======실시간 날씨 예보=======")
print("기상상태: {}".format(wfor))
print("현재온도: {}℃".format(temp))
print("현재습도: {}%".format(humi))
print("=======24시간 후 날씨 예보=======")
print("기상상태: {}".format(wfor2))
print("예상온도: {}℃".format(temp2))
print("예상습도: {}%".format(humi2))