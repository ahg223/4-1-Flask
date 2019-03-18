from flask import *
from werkzeug import secure_filename
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import sys, paramiko
from scp import SCPClient
import os
#import tcpServer
#import executer
import Queue
import time
import re
import socket, threading
from multiprocessing import Queue
#import tcpServerThread

import sys
from socket import *

ECHO_PORT = 50000 + 7

BUFSIZE = 1024

def start():
    if len(sys.argv) < 2:
        usage()
    
    if sys.argv[1] == '-s':
        server()
    
    elif sys.argv[1] == '-c':
        client()
    
    else:
        usage()

def usage():
    sys.stdout = sys.stderr
    print ('Usage: udpecho -s [port]            (server)')
    print ('or:    udpecho -c host [port] <file (client)')
    sys.exit(2)

def server():
    if len(sys.argv) > 2:
        port = eval(sys.argv[2])
    
    else:
        port = ECHO_PORT

    s = socket(AF_INET, SOCK_DGRAM)
    
    s.bind(('', port))
    
    print ('udp echo server ready')

while 1:
    data, addr = s.recvfrom(BUFSIZE)
    
    print ('server received %r from %r' % (data, addr))
        
        s.sendto(data, addr)


def client():
    if len(sys.argv) < 3:
        usage()
    
    host = sys.argv[2]

if len(sys.argv) > 3:
    port = eval(sys.argv[3])
    
    else:
        port = ECHO_PORT

addr = host, port
    
    s = socket(AF_INET, SOCK_DGRAM)
    
    s.bind(('', 0))
    
    print ('udp echo client ready, reading stdin')
    
    while 1:
        line = sys.stdin.readline()
        if not line:
            break
    
        s.sendto(line, addr)
        
        data, fromaddr = s.recvfrom(BUFSIZE)
    print ('client received %r from %r' % (data, fromaddr))

class TCPServerThread(threading.Thread):
    def __init__(self, commandQueue, tcpServerThreads, connections, connection, clientAddress):
        threading.Thread.__init__(self)
        
        self.commandQueue = commandQueue
        self.tcpServerThreads = tcpServerThreads
        self.connections = connections
        self.connection = connection
        self.clientAddress = clientAddress
    def run(self):
        try:
            while True:
                data = self.connection.recv(1024).decode()
                
                # when break connection
                if not data:
                    print ('tcp server1 :: exit :',self.connection)
                    break
                    
                    
                    print ('tcp server :: client :', data)
                    self.commandQueue.put(data)
        except:
            self.connections.remove(self.connection)
            self.tcpServerThreads.remove(self)
            exit(0)
        self.connections.remove(self.connection)
        self.tcpServerThreads.remove(self)

    def send(self, message):
        print ('tcp server :: ',message)
        try:
            for i in range(len(self.connections)):
                self.connections[i].sendall(message.encode())
        except:
            pass


class Executer:
    def __init__(self, tcpServer):
        self.andRaspTCP = tcpServer
    
    def startCommand(self, command):
        
        if command == "123\n":
            self.andRaspTCP.sendAll("321\n")

    '''
    def startCommand(self, command,filename):
        
        if command == "123\n":
            filename='/Users/hyunggeunahn/Downloads' + filename
            with open(filename, 'rb') as f:
                try:
                    data=f.read(1024)
                    while data:
                        data_transferred += self.request.send(data)
                        data = f.read(1024)
                except Exception as e:
                    print(e)
        print('Success: [%s], Byte: [%d]' %(filename,data_transferred))
'''

class TCPServer(threading.Thread):
    def __init__(self, commandQueue, HOST, PORT):
        threading.Thread.__init__(self)
        
        self.commandQueue = commandQueue
        self.HOST = HOST
        self.PORT = PORT
        print(HOST,PORT)
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.HOST, self.PORT))
        self.serverSocket.listen(1)
        
        self.connections = []
        self.tcpServerThreads = []
    
    def run(self):
        try:
            while True:
                print ('tcp server2 :: server wait...')
                connection, clientAddress = self.serverSocket.accept()
                print ('tcp server3 :: server wait...')
                self.connections.append(connection)
                print ("tcp server :: connect :", clientAddress)
                
                subThread = tcpServerThread.TCPServerThread(self.commandQueue, self.tcpServerThreads, self.connections, connection, clientAddress)
                subThread.start()
                self.tcpServerThreads.append(subThread)
        except:
            print ("tcp server :: serverThread error")

    def sendAll(self, message):
        try:
            self.tcpServerThreads[0].send(message)
        except:
            pass


app = Flask(__name__)

'''
@app.route('/upload')
def render_file():
   return render_template('upload.html')

@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'uploads Success!'
 '''
'''
def upload_file(filename):
    if request.method == 'POST':
        f = request.files[filename]
        f.save(secure_filename(f.filename))
        return 'uploads Success!'
'''
@app.route('/start')
def start():
    return 'start'
 
 
@app.route('/select/<name>')
def select(name):
    return 'hi %s' % name
 
 
@app.route('/')
def login():
    '''
    id = 'API_TEST04'
    pw = '1q2w3e4r5t'
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('window-size=1920x1080')
    #options.add_argument("disable-gpu")
    #options.add_argument("--disable-gpu")
    driver =  webdriver.Chrome('/Users/hyunggeunahn/Desktop/MyGit/4-1_Flask/flask/chromedriver')
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
    #driver.save_screenshot("Broadband_test2.png")


    source = driver.page_source
    time.sleep(20)
    driver.get('https://cloudcam.skbroadband.com/do/front/mypage/serviceDownloadList')
    #time.sleep(40)
    driver.find_element_by_xpath('//*[@id="section"]/div/div/div/div/table/tbody/tr[1]/td[5]/div/button').send_keys(Keys.ENTER)
    driver.find_element_by_xpath('//*[@id="section"]/div/div/div/div/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/input').send_keys(Keys.ENTER)
    
    source = driver.page_source
    target = '<div class="txtLeft mal10">'
    p = re.compile(target + '[a-z0-9!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+' + '.mp4')
    findname = p.findall(source)
    filename=findname[0][len(target):]
    
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[2]/input[1]').click()
    time.sleep(5)
    
    #return '/Users/hyunggeunahn/Downloads/' + filename
    #driver.get('/Users/hyunggeunahn/Downloads/' + filename)
    
    '''
    # make public queue
    commandQueue = Queue()

    # init module
    andRaspTCP = TCPServer(commandQueue, "172.30.1.29", 8011)
    andRaspTCP.start()


    # set module to executer
    commandExecuter = Executer(andRaspTCP)


    while True:
        try:
            command = commandQueue.get()
            commandExecuter.startCommand(command,filename)
        except:
            pass

if __name__ == '__main__':
    app.run(debug = True)
