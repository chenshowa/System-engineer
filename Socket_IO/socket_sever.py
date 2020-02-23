# server

import socket
from flask import Flask, jsonify, request


app = Flask(__name__)
s = socket.socket()


host = '140.116.39.174' #ip of raspberry pi
port = 12345

s.bind((host, port))
s.listen(5)

print('Engine start !')



# 示意JSON file
alarms = [{ 
    "result":"True",  
    "message":"",  
    "data": [   
        {    
            "device-id": 205, # SIO2508    
            "timestamp": "2018-06-07T11:30:48+0800",    
            "disconnected": False,         
            "chennals": [     
                {      
                    "id": 1,      
                    "name": "lighting",      
                    "state": 1     
                }
            ]
        }
        ]
        }
        ] 


# 示意JSON file
response15m = {

 
            "device-id": "20508", # PM210         
            "timestamp": "2019-11-17T11:30:48+0800",
            "disconnected": "False",
            "measures": [
                {
                    "name": "Vr", # A 相電壓(2 秒鐘)
                    "value": "115.3",
                    "unit": "V"
                }
            ]
            }


# 示意JSON file
response2s = {
	

	"response2s":[
                {
                    "name": "Vr", # A 相電壓(2 秒鐘)
                    "value": "115.3",
                    "unit": "V"
                }
            ]
}




import json


while True:
  c, addr = s.accept()
  print ("[*] Acepted connection from: %s:%d" % (addr[0],addr[1]))
  request = c.recv(1024)
  request = request.decode().split('&')

  d = request[0].split('=')[1]
  m = request[1].split('=')[1]
  device_id = request[2].split('=')[1]



  print("d          ", d)
  print("m          ", m)
  print("device_id  ", device_id)

  if d=="data":
    if m=="measure":
      print(response2s)
      c.send(str(response2s).encode())
    elif m=="electricity":
      print(response15m)
      c.send(str(response15m).encode())

  elif d=="unusual":
    if m=="status":
      print(response15m)
      c.send(str(alarms).encode())
    elif m=="alarm":
      print(alarms)
      c.send(str(alarms).encode())
  print("\n")

  c.send("Server receive your messenger ".encode())
  c.close()



#post /store/<name> data: {name :}
@app.route('/store' , methods=['POST'])
def create_item_in_store(name):
   return jsonify(stores)

 