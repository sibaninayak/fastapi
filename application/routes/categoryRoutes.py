from fastapi import APIRouter
from ..controller.categoryController import catogoryService

router = APIRouter(prefix="/category", tags=["category"])


# # !http://localhost:5000/users
@router.get('/')
async def getAllCategory():
    return catogoryService.get_allCatogory()


# # !http://localhost:5000/users/me
@router.get('/me')
async def getSinglecategory():
    return catogoryService.getCatogory()