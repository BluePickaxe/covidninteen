from bs4 import BeautifulSoup
import requests

URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do"
response = requests.get(URL)
corona = response.text
coronabs = BeautifulSoup(corona, 'html.parser')
htmlparse1 = coronabs.find('div', attrs={'class':'wrap nj'})
htmlparse2 = htmlparse1.find('form', attrs={'name':'form1', 'id':'form1', 'method':'post'})
htmlparse3 = htmlparse2.find('p', attrs={'class':'inner_value'})
print("오늘 신규 확진자는"+htmlparse3.contents[0]+"명입니다")
print("누적 확진자는 "+htmlparse2.find('dd', attrs={'class':'ca_value'}).contents[0]+"명입니다")