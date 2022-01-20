#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='air')

while True:
	channel.basic_publish(exchange='', routing_key='air', body=str(1))
	time.sleep(5)