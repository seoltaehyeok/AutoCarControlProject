# Auto Car Control 2 DC Motor and Ultrasonic Sensor 
# Jonathan Suh www.creapple.com

#Import GPIO, time library
import RPi.GPIO as GPIO                    
import time                                

#Set GPIO BCM(Broadcom SoC) pin number 
GPIO.setmode(GPIO.BCM)      

TRIG = 23       #GPIO 23번핀                           
ECHO = 24       #GPIO 24번핀                           

GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN)

#오른쪽과 왼쪽 모터를 제어하기 위한 GPIO칩 번호 선정
RIGHT_FORWARD = 26   #GPIO 26번                               
RIGHT_BACKWARD = 19  #GPIO 19번                            
RIGHT_PWM = 13       #GPIO 13번(세기조정)
LEFT_FORWARD = 21    #GPIO 21번                              
LEFT_BACKWARD = 20   #GPIO 20번                               
LEFT_PWM = 16        #GPIO 16번(세기조정)


#두개의 핀은 출력용, 나머지 PWM은 주파수100 설정 후 시작
#좌우 동일하게 설정값 세팅
GPIO.setup(RIGHT_FORWARD,GPIO.OUT)                  
GPIO.setup(RIGHT_BACKWARD,GPIO.OUT)
GPIO.setup(RIGHT_PWM,GPIO.OUT)
GPIO.output(RIGHT_PWM, 0)
RIGHT_MOTOR = GPIO.PWM(RIGHT_PWM, 100)
RIGHT_MOTOR.start(0)
RIGHT_MOTOR.ChangeDutyCycle(0)

GPIO.setup(LEFT_FORWARD,GPIO.OUT)                  
GPIO.setup(LEFT_BACKWARD,GPIO.OUT)
GPIO.setup(LEFT_PWM,GPIO.OUT)
GPIO.output(LEFT_PWM, 0)
LEFT_MOTOR = GPIO.PWM(LEFT_PWM, 100)
LEFT_MOTOR.start(0)
LEFT_MOTOR.ChangeDutyCycle(0)

#Get distance from HC-SR04 
def getDistance(): 
  GPIO.output(TRIG, GPIO.LOW)      #트리거 핀 LOW할당하고 1초 기다림
  time.sleep(1)                            

  GPIO.output(TRIG, GPIO.HIGH)     #트리거 핀 출력하여 초음파 보냄             
  time.sleep(0.00001)              #아주 짧은시간 이후 신호를 다시 끔        
  GPIO.output(TRIG, GPIO.LOW)

  #When the ECHO is LOW, get the purse start time
  while GPIO.input(ECHO)==0:      #초음파센서에 들어오는 ECHO값을 입력받아 초음파를 발생하는 시간          
    pulse_start = time.time()               
  
  #When the ECHO is HIGN, get the purse end time
  while GPIO.input(ECHO)==1:               
    pulse_end = time.time()                 

  #Get pulse duration time
  pulse_duration = pulse_end - pulse_start  #출력된 초음파가 사물과 부딪혀서 돌아오는 시간계산
  #Multiply pulse duration by 17150 to get distance and round
  distance = pulse_duration * 17150        
  distance = round(distance, 2)        #거리 측정 후 소숫점 2자리로 반올림한 값을 받아 return값으로 반환   
 
  return distance

#Right Motor Control 
def rightMotor(forward, backward, pwm): #전진 후진 세기(main문 참조)
  GPIO.output(RIGHT_FORWARD,forward)
  GPIO.output(RIGHT_BACKWARD,backward)
  RIGHT_MOTOR.ChangeDutyCycle(pwm)

#Left Motor Control 
def leftMotor(forward, backward, pwm): #전진 후진 세기(main문 참조)
  GPIO.output(LEFT_FORWARD,forward)
  GPIO.output(LEFT_BACKWARD,backward)
  LEFT_MOTOR.ChangeDutyCycle(pwm)


if __name__ == '__main__':
  try:
    while True:
      distance_value = getDistance()
      #Check whether the distance is 70 cm
      if distance_value > 70:  #초음파 센서거리가 70cm 이상인 경우    
          #Forward 1 seconds
          print ("Forward " + str(distance_value))
          rightMotor(1, 0, 70) #우측 [전진 후진 세기] (true / false / 출력 세기 70)
          leftMotor(1, 0, 70)  #좌측 [전진 후진 세기] (true / false / 출력 세기 70)
          time.sleep(1)        #1초간 동작 지속
      else:
          #Left 1 seconds
          print ("Left " + str(distance_value))
          rightMotor(0, 0, 0) #사물과 거리가 70cm 이하인 경우 우측 모터 작동 중지
          leftMotor(1, 0, 70) #사물과 거리가 70cm 이하인 경우 좌측 모터만 작동 => 우회전
          time.sleep(1)
      
      #Ctrl + C 누르면 작업종료
  except KeyboardInterrupt:
    print ("Terminate program by Keyboard Interrupt")
    GPIO.cleanup()

