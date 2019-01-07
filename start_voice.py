import json
import os
import subprocess
import threading
import time
from threading import Thread

import Adafruit_DHT
import RPi.GPIO as gpio
import flask
import lcd_driver
from flask_cors import CORS, cross_origin

gpio.setmode(gpio.BCM)


def button_callback(channel):
    print("Button was pushed!")
    start_browser()


gpio.setup(19, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.add_event_detect(19, gpio.FALLING, callback=button_callback)

cmd = ''


def start_browser():
    os.system('espeak "Starting browser"')
    os.system('killall chromium-browser')
    subprocess.Popen(['chromium-browser --args --ignore-certificate-errors "hungank.com/devices"'], shell=True)


lcd = lcd_driver.lcd()

from flask import Flask

app = Flask(__name__)

s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'


def remove_accents(input_str):
    s = ''
    print(input_str.encode('utf-8'))
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s


cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

humidity, temperature = 0, 0

lock = threading.Lock()


@app.route('/')
@cross_origin()
def disp_word():
    text = flask.request.args.get('text')
    print(text)
    lcd = lcd_driver.lcd()
    lcd.lcd_clear()
    async_display(remove_accents(text)[:15])
    return 'Hello World!'


@app.route('/temphumi')
@cross_origin()
def disp_temp():
    return json.dumps({'temp': temperature, 'humi': humidity})


def run_app():
    app.run(ssl_context=('cert.pem', 'key.pem'))


Thread(target=run_app).start()


def async_display(text, line=1):
    lock.acquire()
    lcd.lcd_display_string(text, line)
    lock.release()


while True:
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 21)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        async_display('%0.1f%%  %0.1f*C       ' % (humidity, temperature), 2)
    time.sleep(1)
