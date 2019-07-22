import requests
import csv
director_info={}
key = 'cb8f5bac8d77d470b9b538c2106817b5'

director = '봉준호'
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={director}'
response = requests.get(api_url).json()
a = response['peopleListResult']['peopleList'][0] if response['peopleListResult']['peopleList'] else None
director_info[a['peopleCd']] = {'영화인 코드' : a['peopleCd'] if a['peopleCd'] else None,
            '영화인명' : a['peopleNm'] if a['peopleNm'] else None,
            '분야' : a['repRoleNm'] if a['repRoleNm'] else None, 
            '필모리스트' : a['filmoNames'] if a['filmoNames'] else None}

with open('director_info.csv', 'w', encoding= 'utf-8') as f:
    fieldnames = ['영화인 코드', '영화인명','분야', '필모리스트']
    csv_writer = csv.DictWriter(f, fieldnames = fieldnames)
    csv_writer.writeheader()
    for item in director_info.values():
        csv_writer.writerow(item)