from fastapi import APIRouter
from ..controller.cartController import cartService

router = APIRouter(prefix="/cart", tags=["cart"])


# # !http://localhost:5000/users
@router.get('/')
async def getAllCart():
    return cartService.get_allCart()


# # !http://localhost:5000/users/me
@router.get('/me')
async def getSingleCart():
    return cartService.getUser()