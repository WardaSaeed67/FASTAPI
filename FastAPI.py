from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl
import psycopg2
from psycopg2.extras import RealDictCursor
import time
# from app.routes.issues import router as issues_router
app = FastAPI()
# app.include_router(issues_router)


class Course(BaseModel):
    name: str
    instructor:str
    duration: float
    website: HttpUrl

while True:
    try:
        conn = psycopg2.connect(host ='localhost',database='Python', user='postgres', password='root',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("Database connected successfully")
        break
    except Exception as error:
            print("database connection failed")
            print("Error:",error)
            time.sleep(1)



@app.post("/post")
def create_post(post: Course):
    cursor.execute("""insert into course(name,instructor,duration,website) values(%s,%s,%s,%s) RETURNING *""",(post.name,post.instructor,post.duration,str(post.website)))
    new_post= cursor.fetchone()
    conn.commit()
    return {"Data": new_post}


@app.get("/")
def Python():
    cursor.execute("""Select * from course""")
    data=cursor.fetchall()
    return {"Data": data}
