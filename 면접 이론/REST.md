# REST

## REST의 정의

* Representational State Transfer 의 약자
* 자원의 이름으로 구분하여 해당 자원의 상태를 주고 받는 모든것
* www 과 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 개발 아키텍처의 한 형식



## REST 의 구체적 개념

> HTTP URI ( Uniform Resource Identifier)를 통해 자원(Resource) 을 명시하고, 
>
> HTTP Method(POST,GET,PUT,DELETE)를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다

## REST의 장단점

* 장점
	* HTTP프로토콜의 인프라를 그대로 사용하므로 REST API 사용을 위한 별도의 인프라를 구축할 필요가 없다.
	* HTTP 프로토콜의 표준을 최대한 활용하여 여러 추가적인 장점을 함께 가져갈 수 있게 해준다.
	* HTTP표준 프로토콜에 따르는 모든 플랫폼에서 사용 가능하다
	* REST API 메시지가 의도하는 바를 명확하게 나타내므로 의도하는 바를 쉽게 파악할 수 있다.
	* 서버와 클라이언트의 역할을 명확하게 분리한다.

* 단점
	 * 표준이 존재하지 않는다.
	* 사용할수 있는 메소드가 4가지 밖에 없다
## REST 구성 요소
1. 자원(Resource) : URI
	* 모든 자원에 고유한 ID가 존재하고, 이 자원은 Server에 존재한다.
	* Client는 URI를 이용해서 자원을 지정하고 해당 자원의 상태에 대한 조작을 Server에 요청한다.
2. 행위 (Verb) : HTTP Method
	* HTTP 프로토콜은 GET, POST, PUT, DELETE 와 같은 메서드를 제공한다.
3. 표현(Representation of Resource)
	* Client가 자원의 상태에 대한 조작을 요청하면 Server는 이에 적절한 응답(Representation)을 보낸다.
	* REST에서 하나의 자원 `JSON` , `XML` , `TEXT`, `RSS` 등 여러 형태의 응답으로 나타낼 수 있다.

## REST 특징
1. Server-Client(서버-클라이언트 구조)
	* 자원이 있는 쪽이 Server, 자원을 요청하는 쪽이 Client가 된다
		* REST Server : API를 제공하고 비즈니스 로직 처리 및 저장을 책임진다
		* Client : 사용자 인증이나 Context(세션, 로그인 정보) 등을 직접 관리하고 책임진다
	* 서로 간의 의존성이 줄어든다

2. Stateless(무상태)
   * HTTP 프로토콜은 Stateless Protocol 이므로 REST 역시 무상태성을 갖는다.
   * Client 의 context 를 Server에 저장하지 않는다
   * Server는 각각의 요청을 완전히 별개의 것으로 인식하고 처리한다
3. Cacheable(캐시 처리 가능)
   * 웹 표준 HTTP프로토콜을 그대로 사용하므로 웹에서 사용하는 기존의 인프라를 그대로 활용할 수 있다. 
     * HTTP가 가진 가장 강력한 기능 중 하나인 캐싱 기능을 적용할 수 있다
   * 대량의 요청을 효율적으로 처리하기 위해 캐시가 요구된다
   * 캐시 사용을 통해 응답시간이 빨라지고 REST Server 트랜잭션이 발생하지 않기 때문에 전체 응답시간, 성능, 서버의 자원 이용률을 향상시킬 수 있다.
4. Layered System(계층화)
   * Client 는 REST API Server만 호출한다.
   * REST Server 는 다중 계층으로 구성될 수 있다.
   * PROXY, 게이트웨이 같은 네트워크 기반의 중간 매체를 사용할 수 있다.
5. Uniform Interface(인터페이스 일관성)
   * URI 로 지정한 Resource에 대한 조작을 통일되고 한정적인 인터페이스로 수행한다.
   * HTTP 표준 프로토콜에 따르는 모든 플랫폼에서 사용 가능하다