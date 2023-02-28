from fastapi import FastAPI
import uvicorn 

from application.routes import productRoutes,userRoutes,cartRoutes,categoryRoutes

app = FastAPI()


@app.get('/')
def users():
    return {
        "hello":"kitty"
    }

app.include_router(productRoutes.router)
app.include_router(userRoutes.router)
app.include_router(cartRoutes.router)
app.include_router(categoryRoutes.router)

if __name__ == '__main__':
    uvicorn.run(app="main:app",port=5000,reload=True,workers=1)
