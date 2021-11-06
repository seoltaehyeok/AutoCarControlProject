# AutoCarControlProject


### 준비물
* 모터드라이버(L293D)
* 초음파센서(HC-SR04)
* 미니 브레드보드
* 자동차모형(바퀴, 바디)
* 보조 배터리
* 점퍼선(암&수)
* 라즈베리파이 키트
<br/>
<div>
<image src="https://user-images.githubusercontent.com/83220871/140602509-eaaf8f4a-8f83-4c5c-b04a-30cf0ed1ef32.png" width="100" height="100"/>
<image src="https://user-images.githubusercontent.com/83220871/140602514-d9dbff8f-1e2b-4c0f-963e-d3c36c8dd7a7.png" width="100" height="100"/>
<image src="https://user-images.githubusercontent.com/83220871/140602516-db1bdbcc-b4a8-4f9f-9a3e-018f179f1fc9.png" width="100" height="100"/>
<image src="https://user-images.githubusercontent.com/83220871/140602518-f95408a4-3efa-4cfb-85ae-428eb275f14c.png" width="100" height="100"/><br>
<image src="https://user-images.githubusercontent.com/83220871/140602519-19f9504d-101d-4f46-966a-b8062ef49f2d.png" width="100" height="100"/>
<image src="https://user-images.githubusercontent.com/83220871/140602521-fa9917bc-7343-46c4-a180-4a1884e58935.png" width="100" height="100"/>
<image src="https://user-images.githubusercontent.com/83220871/140602523-6230ebd6-0ccf-437d-a905-8a6dd0a21d07.png" width="100" height="100"/>
<image src="https://user-images.githubusercontent.com/83220871/140602598-405cc8cd-d4a2-457c-9b3a-62ee9b865239.png" width="100" height="100"/>
</div>
<br/><br/>

### 제작과정(GPIO 연결)

<div> 
<image src="https://user-images.githubusercontent.com/83220871/140602757-403e48e5-68bf-42e4-a857-059d7e36848b.png" width="200" height="200"/>▶
<image src="https://user-images.githubusercontent.com/83220871/140602760-5dd0fdae-6aae-44f7-a09e-c06101299b60.png" width="200" height="200"/>▶
<image src="https://user-images.githubusercontent.com/83220871/140602763-7213a821-de86-43a1-a544-d6ab7ce2993e.png" width="200" height="200"/>
</div>
<br/><br/>


### 제작과정(바디키트 연결)

<div>
<image src="https://user-images.githubusercontent.com/83220871/140602819-7157c3f1-823d-4cce-afaa-89554e19866d.png" width="200" height="200"/>▶
<image src="https://user-images.githubusercontent.com/83220871/140602820-36164dcb-6cd9-4e66-93e6-9479a25b8036.png" width="200" height="200"/>▶

</div>
<br/><br/>

### GPIO 회로 설계도 및 설명
<image src="https://user-images.githubusercontent.com/83220871/140603410-042e9a2f-e995-4f3c-b0c5-10d01bcc0034.png" width="300" height="200"/>

L293D : 4.5 ~36V 중 라즈베리파이에서 제공하는 5V사용

검정색 : 그라운드 빨간색 : VCC

<br/>
<image src="https://user-images.githubusercontent.com/83220871/140603439-eb21624d-92a8-4ce0-8bde-0b218d50d444.png" width="300" height="200"/>

GPIO 16 20 21번 파란색

GPIO 13 19 26번 자주색

13 16 19번 핀은 PWM핀(13번과 16번은 두 모터의 힘의 세기를 조정한다.)

<br/>
<image src="https://user-images.githubusercontent.com/83220871/140603476-58ef1a27-e298-46fe-bb35-a6cd4c98b57b.png" width="300" height="200"/>

모터1 : L293D의 3번과 6번 핀 

모터2 : L293D의 11번 14번 핀

<br/>
<image src="https://user-images.githubusercontent.com/83220871/140603485-c996e69c-e805-4c0c-817a-64a942d12b5f.png" width="300" height="200"/>

1번 핀(VCC) : 라즈베리파이의 5V

4번 핀(Gnd) : 접지의 역할

2번 핀(Trig) : 라즈베리파이의 신호를 받는 역할(초음파 발생하고 다시 수신)

3번 핀(Echo) : 2번 핀의 값을 3번 핀에서 출력

<br/>
<image src="https://user-images.githubusercontent.com/83220871/140603495-05673d30-85cf-4bd1-8031-b41619740afa.png" width="300" height="200"/>

#### 주의할 점 
: echo 핀에서 5V의 전압이 발생함 하지만 라즈베리파이는 3.3V 사용

3.3V 이상의 전원이 지속적으로 입력되면 회로가 손상받을 수 있다.

=> 1K옴 이상의 저항을 거쳐서 3.3V이하의 전압으로 발생시켜야 한다. (본인은 10K옴 사용)

전원과 그라운드는 모터에서 사용하는 입력값을 같이 사용

트리거 핀은 GPIO 23번핀

에코핀은 GPIO 24번핀과 저항을 거쳐서 연결

### 완성 및 시현 영상

<div>
  <a href="https://drive.google.com/file/d/1Xw4PQJYBGYA3tEzydnJysQD5hcmx9tNo/view?usp=sharing">
<image src="https://user-images.githubusercontent.com/83220871/140603000-af438a33-0810-4ed9-9408-593e9d0ce455.png" width="200" height="200"/>
    클릭 시 이동합니다.
  </a>
</div>
<br/><br/><br/>
움직일 때 너무 흔들려서 임시로 사탕봉지를 끼웠다는...








