import pyautogui
import time

# width, height = pyautogui.size()
# print(width, height)


# 마우스 x,y 좌표
# x_lo, y_lo = pyautogui.position()
# print(x_lo,y_lo)

# pyautogui.moveTo(29,46)
'''
pyautogui.moveTo(x=27,y=49)
pyautogui.click(x=27,y=49) # ppt - 파일
time.sleep(1)

pyautogui.click(x=60,y=372) # ppt - 파일 - 인쇄
time.sleep(0.5)


pyautogui.click(x=404,y=256) # ppt - 파일 - 인쇄 - 프린트 설정
time.sleep(1)

pyautogui.click(x=307,y=406) # ppt - 파일 - 인쇄 - 프린트 설정 - pdf
time.sleep(0.5)

pyautogui.click(x=329,y=455) # ppt - 파일 - 인쇄 - 프린트 설정 - pdf - 슬라이드 분할 선택 
time.sleep(0.5)

pyautogui.click(x=255,y=693) # ppt - 파일 - 인쇄 - 프린트 설정 - pdf - 슬라이드 분할 선택 - 4쪽 분할
time.sleep(0.5)

pyautogui.click(x=330,y=553) # ppt - 파일 - 인쇄 - 프린트 설정 - pdf - 슬라이드 분할 선택 - 4쪽 분할 - 방향 선택
time.sleep(0.5)

pyautogui.click(x=313,y=651) # ppt - 파일 - 인쇄 - 프린트 설정 - pdf - 슬라이드 분할 선택 - 4쪽 분할 - 방향 선택 - 가로 방향
time.sleep(0.5)


pyautogui.click(x=227,y=162) # ppt - 파일 - 인쇄 - 프린트 설정 - pdf - 슬라이드 분할 선택 - 4쪽 분할 - 방향 선택 - 가로 방향 - 인쇄
time.sleep(0.5)
'''

location_x = [27,60,404,307,329,255,330,313,227 ] 
location_y = [49,372,256,406,455,693,553,651,162 ]


for x,y in zip(location_x,location_y):
    pyautogui.click(x,y) 
    time.sleep(0.5)