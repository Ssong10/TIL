# Vue

## Vue 기본 설치

* npm
  
    ```bash
    $npm init
    ```
* 비어있는 `pachage.json` 생성
  
* vue, webpack 설치
    ```bash
    $ npm install vue
    ```
    ```bash
    $ npm install webpack webpack-cli -D
    ```

    * webpack은 개발환경에서 모듈 번들러로써 활용하기 위한 것이므로 `-D` 옵션을 통해 `package.json`에서 `devDependencies` 에 추가

## Vue 개발환경

### 1. vue 파일

```bash
$ npm install vue-loader vue-template-compiler -D
```

* vue-loader : vue파일을 불러오는 역할
* vue-template-compiler : 해석하는 역할

### 2. style

```bash
$ npm install vue-style-loader css-loader -D
```

* vue-style-loader : vue의 style
* css-loader: webpack css를 불러오는 로더

### npm install -g @vue/cli

### vue create { 프로젝트이름 }

enter

* default(babel, eslint)

## $emit : 자식컴포넌트에서 상위 컴포넌트로 이벤트발생

### App - SearchBar

* input 태그에 등록된 이벤트인 (@input)
* trigger : input값이 변경되면,
* 인자로 `event`
* `onInput` method 실행

---

* search-bar 컴포넌트에 등록된 이벤트(@input-change-event)

* trigger : `$emit` 메소드 실행되면, (자식컴포넌트)
* 인자로 `event.target.value`
* `onInputChange` method 실행



## Vue 설치시 사용가능한 npm

#### Project setup

```
npm install
```

#### Compiles and hot-reloads for development

```
npm run serve
```

#### Compiles and minifies for production

```
npm run build
```

#### Lints and fixes files

```
npm run lint
```