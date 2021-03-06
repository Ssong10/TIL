# Protocol

* 통신규약이라 함은 상호간의 접속이나 전달방식, 통신방식, 주고받을 자료의 형식, 오류검출방식, 코드변환방식, 전송속도 등에 대하여 정하는 것을 말한다.

* 일반적으로 기종(機種)이 다른 컴퓨터는 통신규약도 다르기 때문에, 기종이 다른 컴퓨터간에 정보통신을 하려면 표준 프로토콜을 설정하여 각각 이를 채택하여 통신망을 구축해야 한다. 

* 대표적인 표준 프로토콜의 예를 든다면 인터넷에서 사용하고 있는 TCP/IP가 이에 해당된다.



# TCP / IP

> transmission control protocol / internet protocol

참고링크 - [TCP/IP](https://velog.io/@conatuseus/2019-09-10-2009-작성됨-xsk0ds2eqf)

> TCP/IP에서 중요한 개념 중 하나가 계층(Layer)입니다. TCP/IP는 **애플리케이션 계층, 트랜스포트 계층, 네트워크 계층, 링크 계층 이렇게 4계층**으로 나뉘어 있습니다

## 계층

> 계층을 나눠눈 이유
>
> * 사양이 변경되면 해당 계층만 바꾸면 되므로 자유롭다.
> * 설계가 편하다.

- 애플리케이션 계층(Application Layer)**
  애플리케이션 계층은 유저에게 제공되는 애플리케이션에서 사용하는 통신의 움직임을 결정하고 있습니다.
  TCP/IP에는 여러 가지의 공통 애플리케이션이 있습니다. 예를 들면, [FTP](https://ko.wikipedia.org/wiki/파일_전송_프로토콜)와 DNS 등도 애플리케이션의 한 가지 입니다. HTTP도 이 계층에 포함됩니다.
- **트랜스포트 계층(Transport Layer)**
  트랜스포트 계층은 애플리케이션 계층에 **네트워크로 접속되어 있는 2대의 컴퓨터 사이의 데이터 흐름을 제공**합니다. 트랜스포트 계층에서는 서로 다른 성질을 가진 **TCP(Transmission Control Protocol)와 UDP(User Data Protocol) 두 가지 프로토콜**이 있습니다.
- **네트워크 계층(혹은 인터넷 계층)**
  네트워크 계층은 네트워크 상에서 패킷의 이동을 다룹니다. 패킷이란 전송하는 데이터의 최소 단위입니다. 이 계층에서는 어떠한 경로를 거쳐 상대의 컴퓨터까지 패킷을 보낼지를 결정하기도 합니다.
  인터넷의 경우라면 상대 컴퓨터에 도달하는 동안에 여러 대의 컴퓨터와 네트워크 기기를 거쳐 상대에게 배송됩니다. 그러한 **여러 가지 선택지 중에서 하나의 길을 결정하는 것이 네트워크 계층의 역할**입니다.
- **링크 계층(혹은 데이터 링크 계층, 네트워크 인터페이스 계층)**
  네트워크에 접속하는 하드웨어적인 면을 다룹니다. 하드웨어적 측면은 모두 링크 계층의 역할입니다.