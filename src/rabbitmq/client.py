import pika
from aio_pika import connect_robust
import json


class ConsumerClient:
    PARAMETERS = pika.URLParameters('amqp://rabbit:rabbit@rabbitmq:5672')

    def __init__(self, process_callable):
        self.queue_name = 'hello'
        self.connection = pika.BlockingConnection(self.PARAMETERS)
        self.channel = self.connection.channel()
        self.queue = self.channel.queue_declare(self.queue_name)
        self.callback_queue = self.queue.method.queue
        self.process_callable = process_callable

    async def consume(self, loop):
        """Setup message listener with the current running loop"""

        connection = await connect_robust("amqp://rabbit:rabbit@rabbitmq:5672/",
                                          loop=loop)
        channel = await connection.channel()
        queue = await channel.declare_queue('hello')
        await queue.consume(self.process_incoming_message, no_ack=False)

        return connection

    async def process_incoming_message(self, message):
        """Processing incoming message from RabbitMQ"""
        await message.ack()

        body = message.body

        if body:
            await self.process_callable(json.loads(body))
