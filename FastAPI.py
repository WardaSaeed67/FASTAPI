from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl
from app.routes.issues import router as issues_router

app = FastAPI()

app.include_router(issues_router)

#______________ 2 April 2026_________________

# items=[
# {"id":1, "name":"item one"},
# {"id":2, "name":"item two"},
# {"id":3, "name":"item three"}
# ]

# @app.get("/items")
# def get_items():
#     return items











































#______________ 1 April 2026___________
#______define request body scheme_______


# class Course(BaseModel):
#     name: str
#     instructor:str
#     duration: float
#     website: HttpUrl

# @app.post("/post")
# def create_post(post: Course):
#     return {"data": post}







#____________30 March 2026_________________


# @app.get("/")
# def read():
#     return {"Django": "API"}

# @app.get("/item/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/course")
# def func():
#     return {"courses": "API&SDA"}