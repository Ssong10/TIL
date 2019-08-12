# HTML

> Hyper Text Markup Launuage
>
> 웹표준 :  ( w3c  : world wide web consortium )

* html 의 기본 구조

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!-- head 요소는 문서제목, 문자 코드와 같은
        해당문서의 정보를 담고 있으며, 
        브라우저에 나타나지 않는다.
        css 선언 혹은 외부 로딩 파일 지정등
    --!>
</head> 
<body>

</body>
</html>
```



## semantic tag

 ```html
    <header>header</header>
    <nav>Navigation</nav>
    <section>
      Section
      <article>
        article
      </article>
    </section>
    <aside>
      aside
    </aside>
    <footer>
      Footer
    </footer>
 ```

> `details`, `figure`, `main`, `mark`, `summary`, `time`
>
> 일단은 종류와 역할 만 알아두자

```html
<div> div랑 <span>span</span>은 Non Semantic Tag </div>
```

## Heading, paragraph

* Heading은 h1~ h6 까지 있다. 문서의 title을 나타내준다.

* 단락은 `<p> 단락입니다. </p>`로 나눈다.

* 텍스트를 꾸밀때는 `<b>` 로 볼드체를 줄수 있고,
  *  ` <strong>` 시맨틱 태그로 볼드체를 줄수도 있다. `</strong>`

* `<i>` 로 기울임체(이탤릭체)를 쓸수 있다.
  *  `<em>` 도 시맨틱 태그로 같은 이탤릭체이다. `</em>`

```html
<mark> 마크는 하이라이팅이다. </mark>
<del> del은 취소표시를 해준다. </del>
<ins> ins는 추가. 밑줄표기를 해준다.</ins>
<sub> sub은 아랫첨자 </sub>
<sup> sup는 윗첨자이다.</sup>
<p> 질의이다 승열 : <q>밥은언제먹죠?</q> </p>
```

## List

* `<ol>` : ordered  list - 순서가 있는 리스트입니다.

* `<ul>` : unordered  list - 순서가 없는 리스트  기본적으로  ● 로 표시합니다.

  > `<ul>` 이나 `<ol>` 태그 내에 `<li>` 태그를 이용하여 리스트 표시합니다. 

```html
<li style="list-style-type: circle"> 리스트표시 동그라미 </li>
none : 표시 없음
upper-alpha : 대문자 , lower-alpha : 소문자
upper-roman : 로마 대문자, lower-roman : 로마 소문자
```

> `<li>` 에 스타일타입 속성을 주게 되면 `<ul>` `<ol>` 상관없이 적용됩니다. 

## img 태그

```html
<img src="파일의 경로나 링크를 넣어줍니다." alt="대체 택스트" width="너비" height="높이">
```



## iframe 사진, 영상 태그

```html
<iframe width="300px" height="300px" src="링크를 넣어주세요"></iframe>
```

## 링크

```html
<a href="https://google.com"> 구글로 가기 </a>
```



## table

* 기본 구조 

  ```html
  <table>
      <caption> 대충 제목</caption>
      <thead>
      	<tr> /* table row */ 
          	<th>제목3칸</th>
              <th>th태그는 볼드체</th>
              <th>적용이됩니다.</th>
          </tr>
      </thead>
      <tbody>
      	<tr> 
          	<td>내용 3칸</td>
          	<td>table의 내용이</td>
              <td>들어갑니다.</td>
          </tr>
      </tbody>
  </table>
  ```



## form

* `<form>` 태그에 액션과 method 를 이용하여 폼 내용을 원하는 방식으로 보낼 수 있다.

* `<label for="name">` 이름 : `</label>` 

  > for 에 특정 id를 가진 input으로 포커싱이 된다. 

* text : text값을 input으로 받을 수 있다.

  ```html
  <input id="name" type="text" name="name" placeholder="이름을 입력해주세요">
  ```

  > `name`=input() 값으로 폼 내용이 전송된다.
  >
  > `placeholder`  입력칸 창에 나타나 있는 메세지를 설정 할 수 있다.

* date : 날짜를 선택할 수 있는 input입력칸이 나온다. 

* radio : 동일한 name 속성값을 가지고 있는 것 중 에 `하나만` 선택

  ``` html
  <input type="radio" name="sandwich" value="0" checked>에그 마요
  <input type="radio" name="sandwich" value="1"> 이탈리안 비엠티
  ```

  > checked 를 이용해서 선택되어 있는 값을 설정해 줄 수 있다.

* number : 숫자의 범위를 지정해 줄 수 있다.

  ``` html
  <input type="number" name="size" min="15" max="30" step="15">
  ```

  > `number` 타입에선 `min` 값과 `max` 값, `step` 을 설정해 줄 수 있다.
  
* select + option : dropdown 메뉴를 만들 수 있다.

  ```html
  <select name="bread">
        <option value="0">허니 오트밀</option>
        <option value="1" selected>플랫브래드</option>
        <option value="2" disabled>하티 이탈리안</option>
  </select>
  ```

  > select 태그에 name을 지정하고, option 에 value를 지정한다. 
  >
  > option에 selected, disabled 를 사용할 수 있다.

* checkbox

  ```html
  <input type="checkbox" name="source" value="0"> 토마토 <br>
  <input type="checkbox" name="source" value="1"> 오이 <br>
  <input type="checkbox" name="source" value="2"> 할라피뇨 <br>
  <input type="checkbox" name="source" value="3"> 핫 칠리 <br>
  <input type="checkbox" name="source" value="4"> 바베큐 <br>
  ```

  > 여러 개를 선택 할 수 있는 `checkbox`,   `radio`랑 형태는 같지만 선택요소의 갯수가 다르다.

* submit

  ```html
  	<input type="submit" value="제출합니다">
  </form>
  ```

  > submit 버튼을 누르고 해당 폼 데이터를 action 으로 전송 할 수 있다. 

  > value 값을 설정하여 `submit` 버튼의 텍스트를 정할 수 있다. 

# CSS

## style

> 내부참조(embed) head 태그 내에 style태그 활용

```html
<style>
    h1 {    /* 태그선택자*/
        color : red;
    }
    
    .blue {    /* .클래스선택자 */
        color : blue;        
    }
    
    #green {    /* #아이디선택자 */
        color : green;
    }
</style>
```

> 선택자 적용 순위
>
> important >>> 인라인(style)선택 > #아이디선택자 > .클래스선택자 > 태그선택자



## selector

* 인접 선택자 

  ```css
  .blue + .red + div {
  	background-color : purple;
  }
  ```

  > `+` 를 이용해서 설정한 위치에 해당하는 요소에 설정을 할 수 있다.
  >
  > 위에선 .blue클래스 + .red클래스 뒤에오는 div는 보라색 배경으로 된다.

* 자식 선택자

  ```css
  .parent > li {
      color : red;
  }
  ```

  > .parent 클래스 바로 아래있는 `<li>` 는 빨간색으로 나타난다.

* 후손 선택자

  ```css
  .ancestor li {
      color : blue;
  }
  ```

  > .ancestor 클래스 밑에 있는 `<li>` 모두 바뀐다

* nth-child(n)

* nth-of-type(n)

  ```html
  <style>
    #ssafy > p:nth-of-type(2) {
      color:blue;
    }
  </style>
  <div id="ssafy">
    <h2>어떻게 선택될까?</h2>
    <p>첫번째 단락</p>
    <p>두번째 단락</p>
  ```

  > 상위요소 > p:nth-of-type(2) {
  >
  > ​	설정
  >
  > }   ==> 해당 요소 중에서 2번째인 `<p>두번째 단락</p>` 이 변하게 된다.
  >
  > 
  >
  > 상위요소 > p:nth-child(2) {
  >
  > ​	설정
  >
  > }   ==> 자식 중에서 2번째인 `<p>첫번째 단락</p>` 이 변하게 된다.
  >
  > nth-child(1) ==> 1번째 자식이 h2이므로 변하지 않는다.

## Unit

*  rem

  *  root 요소의 배수

  *  html : 16px (브라우저 기본)

  *  ol : 2rem -> 32px (16*2)

  *  li : 2rem -> 32px (16*2)

* em 

  * 상위 요소의 배수

  * html : 16px

  * ul : 2em -> 32px

  * li : 원래 ul 밑에 있어서 32px

  * 2em -> 32px * 2 -> 64px

* vw, vh

  > vw, vh 는 현재 화면 크기에 따라 달라지는 배율을 나타낸다.
  >
  > vw 는 너비에 따라 변화하는 사이즈이고
  >
  > vh 는 높이에 따라 변화하게 된다.
  >
  > vmin 은 작은 값을 따라 맞춰지게된다.

## box model

> 기본적으로 div를 사용하여 박스를 만들어 준다.
>
> margin = div밖 범위 
>
> padding = div안 범위 ( bg적용이 된다.)

>  padding, margin 
>
> 한개 - 상하좌우
>
> 두개 - 상하 / 좌우
>
> 3개 - 상/ 좌우 / 하
>
> 4개 - 상 / 우 / 하 / 좌



## display

> display : block 등 설정을 통하여 보여지는 형태를 설정할 수 있다. 

* block -> 기본적으로 가질 수 있는 영역의 100%를 가진다!

  ```css
  margin-left:auto;  /* 오른쪽으로 붙어있다 */
  margin-right : auto;  /* 왼쪽으로 붙어있다 */
  margin : 0 auto ; /* 가운데에 있다 */
  ```

* inline 영역

  > `<span>` `<input>` `<a>` `<img>`  등 

  > 기본적으로 컨텐트 영역만큼을 가진다. 줄바꿈이 되지 않음.

  > 내용없이 존재할 수 없고, width나 height 적용되지 않는다.

* inline-block속성

  > block속성 -  width, height 를 가지고
  >
  > inline 속성 - 우측 margin이 사라진다.

* none : 해당 공간자체가 0이 되고 표시되지도 않는다.

  > visibility : hidden;  -> 공간은 유지되지만 표시되지 않는다.



## position

* absolute 는 부모 혹은 조상요소를 기준으로 위치

  * 가까운 조상 중 static이 아닌 요소

  * 부모가 static이면 상위요소를 찾아간다.

  * 부모의 위치에 따라 바뀌게 된다.

* relative

  * 자기가 원래 있어야 할 위치(static)을 기준으로 이동함

* fixed , sticky

  * 브라우저 위치에 따라 변경

    > fixed는 공간을 차지하지 않아서 header부분이 아래로 겹쳐진다.
    >
    > sticky는 맨위 공간을 차지해서 header와 겹치지 않는다.

## float

* float 는 y축의 공간을 inline 형태로 y축에 겹치게 된다. 



## background

````html
.header {
  background-image : url("images.jpg")
  height: 500px;
  background-size : cover;
}
````

* background-size:  300px 500px  -> width, height 순으로 지정을 해준다.

  > 값 하나만 지정하면 width 지정값으로 된다.

  > background-repeat : no-repeat / repeat 설정을 통해 반복설정을 할수 있다.

* background-size : cover -> 배경이미지 크기의 비율을 고정, 제일 크게 덮고 남는 부분은 짜른다.

* background-size:  contain  -> 배경 이미지 크기의 비율을 고정한다. 

  >  이미지가 보이지 않는 영역이 없도록 조정하고, 반복이 될 수 있다.



## font 

```html
.font-1 {
  font-size:2em;
  font-family: 'Times New Roman', Times, serif;
  font-weight:lighter;
  font-style: italic;
}

.font-2 {
  font-size:130%;
  font-family:Arial, Helvetica, sans-serif;
  font-weight: bolder;
}
```

* font-size : 폰트 사이즈를 설정해 준다.

  > px, em, rem, % 등을 사용할 수 있다.

* font-family :  폰트의 묶음으로 설정할 수 있다. 

  >  첫번째 폰트가 사용자의 컴퓨터에 없으면 다음 폰트가 적용이 된다.

* font-weight : 폰트 굵기 설정을 할수 있다.

  > lighter, bolder 로 설정 할 수 있다.

* font-style : italic 체로 기울임꼴 설정을 할 수 있다. 



# bootstrap

## spacing 

* mt-1 

  > mt-1 => 0.25rem
  >
  > mr-2  => 0.5rem
  >
  > ml-3  => 1 rem
  >
  > mx-4  => 1.5 rem
  >
  > mb-5 => 3rem

## color

  ```
  dark - 검
  secondary -회
  primary - 파
  warning - 노
  danger - 빨
  success - 초
  info - 청
  light - 흰
  ```

## border

  > `border` - > 테두리 설정
  >
  > `border-color`  => 색상 설정 가능
  >
  > `border-right`  => 테두리 위치설정
  >
  > `rounded-circle` => 달걀느낌
  >
  > `rounded-pill` => 원형 -> 나머지 직선
  >
  > `rounded` => 각진 부분 둥글게

## display

  > `d-inline `: display inline 설정
  >
  > `d-block` : display block설정

  > `d-sm(or md)-none` : 사이즈 이상이면 안보이게 하는 설정

## position

  > `fixed-top` : 맨 위에 고정
  >
  > `fixed-bottom` : 맨 아래 고정
  >
  > `position-relative `
  >
  > `position-absolute`

## component

  > `nav` 
  >
  > `alert`
  >
  > `form`
  >
  > `card`
  >
  > `modal`
  >
  > `pagenation`

## grid 

  ```html
  <div class="container">
      <div class="row">
          <div class="col-4">    
          </div>
          <div class="col-4">
          </div>
          <div class="col-4">
          </div>
      </div> 
  </div>
  ```

## offset 

```html
<div class="row">
    <div class="col-2 offset-5">
        가운데
    </div>
</div>
```

## 틀린거

1. box-sizing:border-box
2. 색상 rgb
3. form 엔 input만 사용가능
4. charset="UTF-8"
5. bootstrap -> text-align-center 가 아니라 text-center