import requests
key = 'cb8f5bac8d77d470b9b538c2106817b5'
targetDt = '20190713'   #yyyymmdd
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'


response = requests.get(api_url).json()
print(response)