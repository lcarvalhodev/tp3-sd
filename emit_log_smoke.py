#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='smoke')

while True:
    channel.basic_publish(exchange='', routing_key='smoke', body=str(1))
    time.sleep(2)
    channel.basic_publish(exchange='', routing_key='smoke', body=str(0))
    time.sleep(2)