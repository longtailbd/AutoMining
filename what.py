import pyautogui
import time

#f6를 누르면 시작 / 좌클릭을 지속적(time을 사용) / 일정 시간마다 enter, /tnfl 를 입력 & 우클릭(파괴자) / f7을 누르면 멈춤
#명령 속도도 설정 가능? 0.1초 정도인듯

#f6누르기
#Mining
pyautogui.drag(0, 0, 5, button='left') #얘를 f7을 눌러서 break가 되기 전까지 "반복"

#300초마다 enter, /tnfl, enter 입력
fixing=['enter', '/', 't', 'n', 'f', 'l', 'enter']
pyautogui.press(fixing)

#200초마다 우클릭 후 다시 Mining
pyautogui.click(button='right')

#위 과정을 반복, f7을 누르면 break