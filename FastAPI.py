from fastapi import FastAPI, HTTPException
from app.routes.issues import router as issues_router
app = FastAPI()
app.include_router(issues_router)
























# items = [
#     {"id": 1, "name": "Laptop", "status": "available"},
#     {"id": 2, "name": "Phone", "status": "sold"},
#     {"id": 3, "name": "Tablet", "status": "available"}
# ]

# @app.get("/items")
# def get_items():
#     return items

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     for item in items:
#         if item["id"] == item_id:
#             return item
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.post("/items")
# def create_item(item: dict):
#     items.append(item)
#     return {"message": "Item added successfully", "item": item} 


















































# from fastapi import FastAPI
# from pydantic import BaseModel,HttpUrl
# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
# # from app.routes.issues import router as issues_router
# app = FastAPI()
# # app.include_router(issues_router)


# class Course(BaseModel):
#     name: str
#     instructor:str
#     duration: float
#     website: HttpUrl

# while True:
#     try:
#         conn = psycopg2.connect(host ='localhost',database='Python', user='postgres', password='root',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connected successfully")
#         break
#     except Exception as error:
#             print("database connection failed")
#             print("Error:",error)
#             time.sleep(1)



# @app.post("/post")
# def create_post(post: Course):
#     cursor.execute("""insert into course(name,instructor,duration,website) values(%s,%s,%s,%s) RETURNING *""",(post.name,post.instructor,post.duration,str(post.website)))
#     new_post= cursor.fetchone()
#     conn.commit()
#     return {"Data": new_post}


# @app.get("/")
# def Python():
#     cursor.execute("""Select * from course""")
#     data=cursor.fetchall()
#     return {"Data": data}
