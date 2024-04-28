from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {
        "id": 1,
        "title": "Hello title 1",
        "content": "This is a post 1",
        "published": True,
        "rating": 1,
    },
    {
        "id": 2,
        "title": "Hello title 2",
        "content": "This is a post 2 and I like pizza",
        "published": True,
        "rating": 2,
    },
    {
        "id": 3,
        "title": "Hello title 3",
        "content": "This is a post 3 and I like pizza",
        "published": True,
        "rating": 3,
    },
    {
        "id": 4,
        "title": "Hello title 4",
        "content": "This is a post 4 and I like pizza",
        "published": True,
        "rating": 4,
    },
    {
        "id": 5,
        "title": "Hello title 5",
        "content": "This is a post 5 and I like pizza",
        "published": True,
        "rating": 5,
    },
]


def find_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return post


def find_post_index(id: int):
    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index


@app.get("/")
def root():
    return {"message": "Hello guys"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = len(my_posts) + 1
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id : {id} was not found",
        )
    return {"post_detail": post}


@app.get("/posts/recents/latest")
def get_lastest_post():
    return {"lastest_post": my_posts[-1]}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_post_index(id)
    if not index:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id : {id} was not found",
        )

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
