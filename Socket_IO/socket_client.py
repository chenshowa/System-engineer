# client
# https://raspberrypi.stackexchange.com/questions/13425/server-and-client-between-pc-and-raspberry-pi

import socket, json #, demjson


s = socket.socket()   

host = '140.116.39.174'# ip of raspberry pi 
port = 12345 

s.connect((host, port))

request = "d=data&m=measure&device-id=5"       # 請求2秒鐘的資料
request = "d=data&m=electricity&device-id=5"   # 請求15分鐘的資料

request = "d=unusual&m=status&device-id=5"     # 請求末端設備的狀態
request = "d=unusual&m=alarm&device-id=5"      # 查詢末端設備是否異常

s.send(request.encode('ascii'))


# 接收到資料，接著解碼，再經過字串處理，之後再轉為JSON
print(json.loads(s.recv(1024).decode().replace("'", '"'))["response2s"])

# print(s.recv(1024).decode())

s.close()

 