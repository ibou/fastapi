from fastapi import Depends, FastAPI
import psycopg
import time
from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware


# models.Base.metadata.create_all(bind=engine)



app = FastAPI()
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# try:
#     connection = psycopg.connect(
#         "dbname=fastapi user=postgres password=root host=localhost port=5432"
#     )
#     cursor = connection.cursor()
#     print("Connection to PostgreSQL DB successful..")

# except Exception as e:
#     print(f"The error '{e}' occurred.")
#     time.sleep(10)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello guys!"}
