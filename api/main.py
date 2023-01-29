from fastapi import FastAPI

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = FastAPI()


@app.get("/")
async def root():
    return {'message': 'Everything works fine!'}

@app.get("/add")
async def add():
    cred = credentials.Certificate("licenta-b9043-9411aff00f92.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    ref = db.collection('users').document('dragos')
    
    ref.set({
        'name':'Dragos',
        'age':22
    })
    
    return {'message': 'User Dragos, age 22 has been added in the database!'}




