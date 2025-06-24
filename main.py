from fastapi import FastAPI
from pydantic import BaseModel # function hota h class create krne k liye (basemdel)


app=FastAPI()
data=[]

class Book (BaseModel):
    id:int
    Title:str
    author:str
    publisher:str

# @app.post("/book")
# def add_book(Book:book):
#     data.append(book.dict())
#     return data 

@app.post("/book")
def add_book(book:Book): 
    data.append(book.dict())
    return data


@app.get("/lists")
def get_book():
 return data 

@app.put("/book/{id}")
def add_book (id:int,book:Book):
   data[id-1]=book
   return data

@app.delete("/book/{id}")
def delete_book(id:int):
   data.pop(id-1)
   return data
