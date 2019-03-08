from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

'''
카메라 id 기반으로 찾아서 그순간부터 원하는 만큼의 영상정보 다운로드를 요청한다.
'''

id = 'API_TEST04'
pw = '1q2w3e4r5t'
driver =  webdriver.PhantomJS('/Users/hyunggeunahn/Desktop/MyGit/Flask/phantomjs')    #팬텀소환. 주소는 자신의phantomjs 절대주소로 바꾸세요

driver.get('https://cloudcam.skbroadband.com/do/front/dashboard/cameraInfo?camId=117252')
delay=30
driver.implicitly_wait(delay)

#로그인
print('로그인합니다.')
driver.find_element_by_name('userId').send_keys(id)
driver.find_element_by_name('password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
time.sleep(10)


#로그인 후 캠id로 찾아온 화면.
driver.find_element_by_xpath('//*[@id="btn-popup-down"]').send_keys(Keys.ENTER) #다운로드 버튼 찾아 클릭
time.sleep(5)


#녹화시간을 현재시간 기준 몇분간 녹화할 건지 설정
select = Select(driver.find_element_by_xpath('//*[@id="sbox_min"]'))  #영상녹화시간 드롭박스 선택
select.select_by_value('01')    #value 기준 선택 -> 01로 예시


# [다운로드요청] 버튼 클릭
driver.find_element_by_xpath('//*[@id="export_popup"]/div/div/input[1]').send_keys(Keys.ENTER)
time.sleep(5)

# 다운로드를 요청하시겠습니까? 에 [확인] 버튼 클릭
driver.find_element_by_xpath('//*[@id="pop-cnfm-camChange"]/div/div[2]/input[1]').send_keys(Keys.ENTER)
time.sleep(5)
driver.save_screenshot("Broadband_test2.png") # 잘 되었나 스크린샷을 남겨보자.


source = driver.page_source #페이지 소스 분석용
print(source)   #그냥 지금 페이지 확인용
