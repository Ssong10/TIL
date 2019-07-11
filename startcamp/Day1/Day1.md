# Startcamp Day1

## Python 기초 문법

1. 저장

   ```python
   # 저장은 =을 통해서 한다.
   dust = 64 # 숫자(integar)
   name = '홍길동' # 문자열(string)
   is_summer = True #참/거짓, Boolean(True,False)
   ```

   ```python
   # 리스트 활용법
   my_list = [1, 2, 3, '정지수', '이승열']
   print(my_list[0]) # => 1
   # 딕셔너리 활용법
   my_dictionary = {'정지수':'남자', '이승열':'남자'}
   print(my_dictionary['이승열']) # => '남자'
   ```

   

2. 조건문

   ```python
   if dust > 150:
       print('매우나쁨')
   elif dust > 80:
       print('나쁨')
   else:
       print('보통')
   ```

   

3. 반복문

   ```python
   lunch_box = ['짬뽕', '유산슬덮밥', '돈육제육']
   # 정해진 리스트 반복
   for menu in lunch_box:
       #menu = lunch_box[0], .... , lunch_box[2]
       print(menu)
   # n번 반복
   for menu in range(5)
       print('hello!!')
   ```

   

4. 내장함수

   > 내장함수는 별도로 import 구문이 필요없다.

   ```python
   print('hi')
   print(max([2,4,1])) #=> 4
   print(min([1,2,6])) #=> 1
   print(abs(-5)) #=> 5
   print(len([1,2,3])) #=> 3
   ```

   

5. 외장함수

   > 외장함수는 반드시 import가 필요하다.
   >
   > 다만, 파이썬을 설치하면 자동으로 그냥 불러서 쓸 수 있다.

   ```python
   import random
   numbers = range(1,46)
   lotto = random.sample(numbers, 6)
   print(sorted(lotto))  #=> 1~45까지 무작위 6개 정렬
   ```

   

6. 패키지

   > 패키지는 반드시 설치를 필요로 한다. 

   `pip install 패키지명` 으로 설치를 한다.

   ```bash
   $ pip install requests
   ```

   

   ```python
   import requests
   requests.get(url)
   ```



## 파이썬을 통한 크롤링

1. 필수 설치 패키지

   * `requests` : 파이썬으로 요청을 보내주는 패키지

   * `bs4` : 문자열을 html 등으로 구조화(파싱)를 해주는 패키지

      ```bash
     $ pip install requests
     $ pip install bs4
      ```

2. 네이버에서 코스피 지수 가져오기

   ```python
   # 0. 활용할 패키지를 불러온다.
   import requests
   from bs4 import Beautifulsoup
   # 1. url을 설정한다.
   url = 'http://finance.naver.com/sise/'
   # 2. 요청을 보내고, 그 결과를(text) response에 저장한다.
   response = requests.get(url).text
   # 3. html 문서로 변환한다.
   soup = BeautifulSoup(response, 'html.parser')
   # 4. 원하는 값을 선택자(selector)를 활용해서 가져온다.
   kospi = soup.select_one('#KOSPI_now').text
   print(kospi)
   ```

   