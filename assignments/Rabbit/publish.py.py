import os
import pika

import amqpkey
amqp_url=amqpkey.key

url=os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 15

connection = pika.BlockingConnection(params)

channel = connection.channel();
channel.queue_declare(queue='hello')
msg=channel.basic_publish(exchange='',routing_key='hello',body='Hello World')

print("[x] Sent 'Hello world")
connection.close()
