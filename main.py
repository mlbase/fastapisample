import os
from typing import Union, Optional
from fastapi import FastAPI, Request
from model.sampleModel import SampleModel
from routes.test import router as test_router

app = FastAPI()
app.include_router(test_router)

sample_list = []


@app.get('/db_test')
def index():
    return {
        "Python": "Framework",
    }


@app.get('/')
def root():
    return sample_list


@app.post('/')
def create(sample: SampleModel):
    sample = {
        "id": len(sample_list),
        "sample": sample,
        "success": "true",
        "message": "create success"
    }
    sample_list.append(sample)
    return sample


@app.put('/{item_id}')
def update(item_id: int, sample: SampleModel):
    sample = {
        "id": item_id,
        "name": sample.name,
        "description": sample.description,
        "price": sample.price,
        "success": "true",
        "message": "update success"
    }
    sample_list[item_id] = sample
    return sample


@app.patch('/{item_id}')
def update_sample(item_id: int, sample: SampleModel):
    sample = {
        "id": item_id,
        "name": sample.name,
        "description": sample.description,
        "price": sample.price,
        "success": "true",
        "message": "update success"
    }
    sample_list[item_id] = sample
    return sample


@app.delete('/{item_id}')
def delete(item_id: int):
    del sample_list[item_id]
    return {
        "message": "delete success"
    }
