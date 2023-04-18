from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from src.auth.config import get_current_user
from src.db.services import AWSDynamoDBServices

router = APIRouter(
    prefix='/stats',
    tags=["Statistics"]
)


@router.get("/{page_id}")
async def get_stats(page_id: int, current_user: dict = Depends(get_current_user)):
    user_id = current_user["user_id"]

    data = await AWSDynamoDBServices.get_item(user_id=user_id, page_id=page_id)

    if 'Item' not in data:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You do not have permission to perform this action")

    return {
        'status': 200,
        "data": data['Item'],
        'detail': 'Data has been provided'
    }
