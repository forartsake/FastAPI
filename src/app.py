from fastapi import FastAPI
from src.db.services import AWSDynamoDBServices
from src.rabbitmq.client import ConsumerClient


class App(FastAPI):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pika_client = ConsumerClient(self.incoming_message)

    @classmethod
    async def incoming_message(cls, message: dict):
        try:
            await AWSDynamoDBServices.add_new_item_to_db(user_id=message.get('user_id'),
                                                         page_id=message.get('page_id'),
                                                         posts_count=message.get('posts_count', None),
                                                         followers_count=message.get('followers_count', None),
                                                         likes_count=message.get('likes_count', None)
                                                         )

        except Exception as e:
            return f"Something goes wrong: {e}"
