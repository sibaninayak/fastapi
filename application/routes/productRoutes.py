from fastapi import APIRouter
from ..controller.productController import ProductService

router = APIRouter(prefix="/products", tags=["products"])


# # !http://localhost:5000/users
@router.get('/')
async def getAllProducts():
    return ProductService.get_allProducts()


# # !http://localhost:5000/users/me
@router.get('/me')
async def getSingleProducts():
    return ProductService.getProduct()