from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
import strawberry
import uvicorn 
from fastapi.staticfiles import StaticFiles
from strawberry.fastapi import GraphQLRouter
from fastapi.templating import Jinja2Templates

from application.routes import productRoutes,userRoutes,cartRoutes,categoryRoutes

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users. The **login** logic is also here.",
    },
    {
        "name": "items",
        "description": "Manage items. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Items external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello World"


schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)



app = FastAPI(title="E-commerce",
              description=description,
              version=2.0,
              contact= {
                       "name":"sibani nayak",
                       "url":"https://sibani-nayak.netlify.app/",
                       "email":"sibaninayak1808@gmail.com"
},
license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
    openapi_url='/kittycommerce.json',
    docs_url='/docs'
)

# # !mount in the browser
app.mount("/static",StaticFiles(directory="dist"),name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/" , response_class=HTMLResponse)
async def read_item(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})
@app.get("/about" , response_class=HTMLResponse)
async def read_item(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})
@app.get("/contact" , response_class=HTMLResponse)
async def read_item(request:Request):
    return templates.TemplateResponse("index.html", {"request":request})

# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id})

# @app.get("/items/")
# async def read_items():
#     return [{"name": "Kitty"}]
# @app.get('/')
# def users():
#     return {
#         "hello":"kitty"
#     }

# ?endpoints (RESTAPI)
app.include_router(productRoutes.router)
app.include_router(userRoutes.router)
app.include_router(cartRoutes.router)
app.include_router(categoryRoutes.router)

# ?endpoints (GRAPHQLAPI)
app.include_router(graphql_app, prefix="/graphql")


if __name__ == '__main__':
    uvicorn.run(app="main:app",port=5000,reload=True,workers=1)
