#!/usr/bin/env python
import pika
import sys
import time
import random

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='lights')

while True:
	channel.basic_publish(exchange='', routing_key='lights', body=str(1))
	time.sleep(5)