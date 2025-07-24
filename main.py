from typing import list
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.request import Request
from starlette.reponses import Reponse,JSONRepons

app =FastAPI()
#1
@app.get("\hello")
def read_hello():
     return JSONRepons({"message": "hello world"}),statut_code =200)
#2
@app.get("\welcome")
def read_welcome():
    return JSONRepons({"message: f"welcom{name}"},statut_code=200)

#3
@app.get("\student")
    def list():
        class liste(baseModel):
            reference:str
            firstname:str
            lastname:str
            age:int
events_store:list[liste]=[]
return JSONRepons[{ "events": events_store}],statut_code=100)

#4
@app.get("\student")
def read_student_list
    return JSONRepons({"events"}),statut_code=100)












