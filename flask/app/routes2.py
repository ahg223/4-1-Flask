from flask import Flask, render_template, request
from werkzeug import secure_filename
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from flask import Flask

from firebase import firebase


app = Flask(__name__)

thread=None
firebase=firebase.FirebaseApplication("https://skb-cctv.firebaseio.com/",None)

@app.route('/upload')
def render_file():
   return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'uploads Success!'
 
@app.route('/start')
def start():
    return 'start'
 
 
@app.route('/select/<name>')
def select(name):
    return 'hi %s' % name
 
 
@app.route('/')
def login():
    id = 'API_TEST04'
    pw = '1q2w3e4r5t'
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('window-size=1920x1080')
    #options.add_argument("disable-gpu")
    #options.add_argument("--disable-gpu")
    driver =  webdriver.Chrome('/Users/hyunggeunahn/Desktop/MyGit/Flask/flask/chromedriver')
    #driver =  webdriver.Chrome('/Users/hyunggeunahn/Desktop/MyGit/Flask/flask/chromedriver',chrome_options=options)
    driver.get('https://cloudcam.skbroadband.com/do/front/dashboard/cameraInfo?camId=117252')
    delay=30
    driver.implicitly_wait(delay)


    driver.find_element_by_name('userId').send_keys(id)
    driver.find_element_by_name('password').send_keys(pw)
    driver.find_element_by_xpath('//*[@id="loginBtn"]').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="loginBtn"]').send_keys(Keys.ENTER)


    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[2]/input[1]').send_keys(Keys.ENTER)


    #time.sleep(10)


    driver.find_element_by_xpath('//*[@id="btn-popup-down"]').send_keys(Keys.ENTER)
    #time.sleep(5)

    select = Select(driver.find_element_by_xpath('//*[@id="sbox_min"]'))
    select.select_by_value('01')


    driver.find_element_by_xpath('//*[@id="export_popup"]/div/div/input[1]').send_keys(Keys.ENTER)
    #time.sleep(5)

    driver.find_element_by_xpath('//*[@id="pop-cnfm-camChange"]/div/div[2]/input[1]').send_keys(Keys.ENTER)
    #time.sleep(5)
    driver.save_screenshot("Broadband_test2.png")


    source = driver.page_source
    time.sleep(20)
    driver.get('https://cloudcam.skbroadband.com/do/front/mypage/serviceDownloadList')
    #time.sleep(40)
    driver.find_element_by_xpath('//*[@id="section"]/div/div/div/div/table/tbody/tr[1]/td[5]/div/button').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="section"]/div/div/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/input').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[2]/input[1]').click()
    time.sleep(20)
    
    firebase.post("https://skb-cctv.firebaseio.com/","/Users/hyunggeunahn/Downloads/117252_27871_145699_03131435_1436.mp4")


if __name__ == '__main__':
    app.run(debug = True)
