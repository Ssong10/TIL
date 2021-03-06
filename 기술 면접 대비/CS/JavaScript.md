# JavaScript





## ES 6

### Update

* spread

  * 원본 배열을 바꾸지 않고 열거 가능한 요소를 하나씩 전개 
* New set()
* 비구조화 할당
  * 속성값을 이용하여 객체의 값을 가져올수 있다.
* 템플릿 문자열
  * backtick(`) 을 이용해 새로운 문자열을 만들수 있다
* 객체 리터럴 
  * object 객체에 동적으로 속성을 추가

### Babel 

>  JavaScript Transfiler/Compiler

ES6 이상의 최신 문법으로 작성한 자바스크립트 코드를 ES 5 이하의 예전 문법으로 작성한 것처럼 소스 코드 내의 문법의 형태를 변경할 수 있습니다.
ES6에서 도입된 arrow function 같은 경우

```javascript
;[1, 2, 3].map((n) => n + 1)
```
이 코드가 돌아가지 않는 브라우저에서는 Babel을 이용하여 아래의 function 문법으로 변경됩니다
```javascript
;[1, 2, 3].map(function (n) {
return n + 1
```



## Ajax

>  JavaScript의 라이브러리중 하나이며 Asynchronous Javascript And Xml(비동기식 자바스크립트와 xml)의 약자입니다.

*  브라우저가 가지고있는 XMLHttpRequest 객체를 이용해서 전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위한 데이터를 로드하는 기법

*  JavaScript를 사용한 비동기 통신, 클라이언트와 서버간에 XML 데이터를 주고받는 기술이라고 할 수 있겠습니다.

기본적으로 HTTP프로토콜은 클라이언트쪽에서 Request를 보내고 Server쪽에서 Response를 받으면 이어졌던 연결이 끊기게 되어있습니다. 그래서 화면의 내용을 갱신하기 위해서는 다시 request를 하고 response를 하면서 페이지 전체를 갱신하게 됩니다. 하지만 이렇게 할 경우 페이지의 일부분만 갱신할 경우에도 페이지 전체를 다시 로드해야하는데 엄청난 자원낭비와 시간낭비를 초래하고 말것입니다. 하지만 ajax는 html 페이지 전체가아닌 일부분만 갱신할수 있도록 XML HttpRequest객체를 통해 서버에 request를 합니다. 이 경우 Json이나 xml형태로 필요한 데이터만 받아 갱신하기 때문에

**Ajax의 장점**

1. 웹페이지의 속도향상

2. 서버의 처리가 완료 될때까지 기다리지 않고 처리 가능하다.

3. 서버에서 Data만 전송해면 되므로 전체적인 코딩의 양이 줄어든다.

4. 기존 웹에서는 불가능했던 다양한 UI를 가능하게 해준다. 사진공유 사이트 Flickr의 경우 사진의 제목이나 태그를 페이지 리로드 없이 수정할 수 있다.

 **Ajax 의 단점**

1. 히스토리 관리가 안 된다. (보안에 좀 더 신경을 써야한다.)

2. 연속으로 데이터를 요청하면 서버 부하가 증가할 수 있다.

3. XMLHttpRequest를 통해 통신을 하는 경우사용자에게 아무런 진행 정보가 주어지지 않는다. 그래서 아직 요청이 완료되지 않았는데 사용자가 페이지를 떠나거나 오작동할 우려가 발생하게 된다. 



## axios

>  Promise based HTTP client for the browser and node.js

axios는 node.js와 브라우저를 위한 http통신 javascript 라이브러리입니다.

아래와 같이 모든 브라우저를 지원합니다. (Fetch와 달리 크로스 브라우징에 최적화)



![callbacktopromist](image/callback-to-promise.png)

## CallBack function





## Promise ( 좀더 알아보기 )

콜백 함수로 처리하면 되는 문제였지만 요즘에는 프론트엔드의 규모가 커지면서 코드의 복잡도가 높아지는 상황이 발생하였다. 이러면서 콜백이 중첩되는 경우가 따라서 발생하였고, 이를 해결할 방안으로 등장한 것이 Promise 패턴이다. Promise 패턴을 사용하면 비동기 작업들을 순차적으로 진행하거나, 병렬로 진행하는 등의 컨트롤이 보다 수월해진다. 또한 예외처리에 대한 구조가 존재하기 때문에 오류 처리 등에 대해 보다 가시적으로 관리할 수 있다.





## Async/Await





## Arrow Function

화살표 함수 표현식은 기존의 function 표현방식보다 간결하게 함수를 표현할 수 있다. 화살표 함수는 항상 익명이며, 자신의 this, arguments, super 그리고 new.target을 바인딩하지 않는다. 그래서 생성자로는 사용할 수 없다.

- 화살표 함수 도입 영향: 짧은 함수, 상위 스코프 this

