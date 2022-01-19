#!/usr/bin/env python
#!/usr/bin/python 
import socket
import threading
import grpc
import pika, sys, os
import light_pb2
import light_pb2_grpc
import air_pb2
import air_pb2_grpc
import smoke_pb2
import smoke_pb2_grpc
import json
IP = "127.0.0.1"
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((str(IP), int(PORT)))
sock.listen(10)
sock.setblocking(False)
clientes = []

light_sensor = []
light_sensor.append(0)
light_value = []
light_value.append(0)

air_sensor = []
air_sensor.append(0)
air_value = []
air_value.append(0)

smoke_sensor = []
smoke_sensor.append(0)
smoke_value = []
smoke_value.append(0)

def initConnection():
    global light_sensor
    global light_value
    global clientes
    global sock
    while True:
        try:
            light_status = ""
            smoke_status = ""
            conn, addr = sock.accept()
            conn.setblocking(False)
            clientes.append(conn)
            if int(air_value[len(air_value)-1]) >= 0 and len(air_value)>1:
                valueTemp = int(air_value[len(air_value)-1])
            else:
                valueTemp = air_sensor[len(air_sensor)-1]
            
            if len(light_value)>1:
                if light_value[len(light_value)-1] >= 1:
                    light_status = "On"
                else:
                    light_status = "Off"
            else:
                light_status = "Off"
            
            if len(smoke_value)>1:
                if smoke_value[len(smoke_value)-1] >= 1:
                    smoke_status = "Fire!!!"
                else:
                    smoke_status = "No Fire"
            else:
                smoke_status = "No Fire"
            conn.send(('HTTP/1.0 200 OK\n').encode('utf-8'))
            conn.send(('Content-Type: text/html\n').encode('utf-8'))
            conn.send(('\n').encode('utf-8'))
            conn.send(("""
                <html>
                <meta charset="utf-8"/>
                    <body>
                        <h1>TP3 - SD</h1>
                        <h3>Lights: {}</h3>
                        <h3>Temperature (C°): {}</h3>
                        <h3>Smoke sensor: {}</h3>
                        <br><a href="http://localhost:8080/">Change Values</a>
                    </body>
                </html>
            """).format(light_status, valueTemp, smoke_status).encode('utf-8'))
        except:
            pass


def proccess():
    global clientes
    while True:
        if len(clientes) > 0:
            for c in clientes:
                try:
                    data = c.recv(1024)
                    dataDecoded = data.decode('utf-8')
                    if data:
                        dataJson = json.loads(dataDecoded)
                        print(dataJson)
                        form(dataJson)
                        
                except:
                    pass

def form(dataJson):
    if int(dataJson['lights']) == 1:
        light(1)
    else:
        light(0)
    if int(dataJson['air']) == 1:
        air(float(dataJson['temperature']))
    else:
        air(0)
    if int(dataJson['smoke']) > 0:
        smoke(int(dataJson['smoke']))
    else:
        smoke(int(dataJson['smoke']))

def sub_light():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='lights')

    def callback(ch, method, properties, body):
        valor = int(float(body.decode()))
        global light_sensor 
        light_sensor.append(valor)

    channel.basic_consume(queue='lights', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

def sub_air():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='air')
    def callback(ch, method, properties, body):
        valor = int(float(body.decode()))
        global air_sensor
        air_sensor.append(valor) 

    channel.basic_consume(queue='air', on_message_callback=callback, auto_ack=True)
    
    channel.start_consuming()

def sub_smoke():

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='smoke')
    def callback(ch, method, properties, body):
        valor = body.decode()
        global smoke_sensor
        smoke_sensor.append(int(valor))
    
    channel.basic_consume(queue='smoke', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()

def smoke(comando):
    
    channel = grpc.insecure_channel('localhost:50053')
    stub = smoke_pb2_grpc.SmokeStub(channel)
    if float(comando)>=0:
        status = smoke_pb2.SmokeStatus(status=float(comando))
        response = stub.turnOn(status)
    else:
        status = smoke_pb2.SmokeStatus(status=float(comando))
        response = stub.turnOff(status)


    smoke_value.append(response.status)


def air(comando):
    channel = grpc.insecure_channel('localhost:50051')
    stub = air_pb2_grpc.AirStub(channel)

    if float(comando)>0:
        status = air_pb2.AirTemperature(temperature=float(comando))
        response = stub.turnOn(status)
    else:
        status = air_pb2.AirTemperature(temperature=-1)
        response = stub.turnOff(status)

    air_value.append(response.temperature)

def light(comando):
    channel = grpc.insecure_channel('localhost:50052')
    stub = light_pb2_grpc.LightStub(channel)
    status = light_pb2.LightStatus(status=1)
    
    if float(comando)>0:
        response = stub.turnOn(status)
    else:
        response = stub.turnOff(status)

    light_value.append(response.status)
    

t = threading.Thread(target=sub_light)
t.start()

t2 = threading.Thread(target=sub_air)
t2.start()

t3=threading.Thread(target=sub_smoke)
t3.start()

aceptar = threading.Thread(target=initConnection)
aceptar.start()

procesar = threading.Thread(target=proccess)
procesar.start()

while True:
    try: 
        comando = input('')
    
    except KeyboardInterrupt:
        print('Proccess Finished')
        try:
            sys.exit(0)
            sock.close()
        except SystemExit:
            sock.close()
            os._exit(0)

