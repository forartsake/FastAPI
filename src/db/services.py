from typing import Optional
from src.db.database import AccountStats


class AWSDynamoDBServices:
    @staticmethod
    async def add_new_item_to_db(user_id: int, page_id: int,
                                 posts_count: Optional[int] = None,
                                 followers_count: Optional[int] = None,
                                 likes_count: Optional[int] = None):

        update_expression_parts = []
        expression_attribute_values = {}
        if posts_count is not None:
            update_expression_parts.append('posts_count = :val1')
            expression_attribute_values[':val1'] = posts_count
        if likes_count is not None:
            update_expression_parts.append('likes_count = :val2')
            expression_attribute_values[':val2'] = likes_count
        if followers_count is not None:
            update_expression_parts.append('followers_count = :val3')
            expression_attribute_values[':val3'] = followers_count

        update_expression = 'SET ' + ', '.join(update_expression_parts)

        try:
            response = AccountStats.update_item(TableName='AccountStats',
                                                Key={
                                                    'user_id': user_id,
                                                    'page_id': page_id
                                                },
                                                UpdateExpression=update_expression,
                                                ExpressionAttributeValues=expression_attribute_values
                                                )
        except Exception as e:
            return f"Error during updating item in DynamoDB: {e}"

    @staticmethod
    async def get_item(user_id: int, page_id: int):
        item = AccountStats.get_item(
            Key={'user_id': user_id, 'page_id': page_id}
        )
        return item
