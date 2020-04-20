from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import Adafruit_DHT
from pyrebase import pyrebase
from time import sleep
import datetime

config = {
    "apiKey": "AIzaSyB0uOWyGYjD4Q0FUEbsZ7TBD21SzcNDGRg",
    "authDomain": "raspberry-5a998.firebaseapp.com",
    "databaseURL": "https://raspberry-5a998.firebaseio.com",
    "projectId": "raspberry-5a998",
    "storageBucket": "raspberry-5a998.appspot.com",
    "messagingSenderId": "171055053170",
    "appId": "1:171055053170:web:a38e03ef7c6eaa5f1305eb"
  }

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# db.child('/sensor/dht').push({"name": "saleh"})

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(23, GPIO.IN)


# # Set sensor type : Options are DHT11,DHT22 or AM2302
# sensor=Adafruit_DHT.DHT11
 
# # Set GPIO sensor is connected to
# gpio=18
 
    # # Use read_retry method. This will retry up to 15 times to
    # # get a sensor reading (waiting 2 seconds between each retry).
    # humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    # # Reading the DHT11 is very sensitive to timings and occasionally
    # # the Pi might fail to get a valid reading. So check if readings are valid.
    # if humidity is not None and temperature is not None:
    #     print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        
    # else:
    #     print('Failed to get reading. Try again!')







    

# {{url}}/led?status=on
@app.route('/', methods=['GET'])
def led():

    status = request.args.get('status')
    if status == "on":
        GPIO.output(17, GPIO.HIGH)
        return jsonify({"message": "Led successfully turned on" , "23 status": GPIO.input(23)}, )

    elif status == "off":
        GPIO.output(17, GPIO.LOW)
        return jsonify({"message": "Led successfully turned off" , "23 status": GPIO.input(23)})
    else:
        return jsonify({"message": "Not a valid status" ,  "23 status": GPIO.input(23)})




# def update_firebase():

# 	humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
# 	if humidity is not None and temperature is not None:
# 		sleep(5)
# 		str_temp = ' {0:0.2f} *C '.format(temperature)	
# 		str_hum  = ' {0:0.2f} %'.format(humidity)
# 		print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))	
			
# 	else:
# 		print('Failed to get reading. Try again!')	
# 		sleep(10)

# 	data = {"temperature": temperature, "humidity": humidity}
# 	db.child('/sensor/dht').push(data)
	

# while True:
# 		update_firebase()
		
#         #sleepTime = int(sleepTime)
# 		sleep(5)