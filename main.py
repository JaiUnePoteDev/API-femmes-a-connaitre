''' (py -m uvicorn main:app --reload) -> lance serveur '''
'''http://127.0.0.1:8000'''
''' http://127.0.0.1:8000/docs '''
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

import json


app = FastAPI(docs_url=None, redoc_url=None)

'''Personnalisation favicon fastapi'''

@app.get("/docs", include_in_schema=False)
def overridden_swagger():
	return get_swagger_ui_html(openapi_url="/openapi.json", title="FastAPI", swagger_favicon_url="https://avatars.githubusercontent.com/u/105969133?s=400&u=1271d14a9a31ab11af310459ffdc476f4a034647&v=4")

@app.get("/redoc", include_in_schema=False)
def overridden_redoc():
	return get_redoc_html(openapi_url="/openapi.json", title="FastAPI", redoc_favicon_url="https://avatars.githubusercontent.com/u/105969133?s=400&u=1271d14a9a31ab11af310459ffdc476f4a034647&v=4")

''' Fin'''


class Women(BaseModel):
    id: Optional[int] = None
    name: str
    field: str
    biography: str

with open('women.json', encoding='utf-8') as f:   
    women = json.load(f)

@app.get('/')
def get_allWomen():
    return women

@app.get('/person/{w_id}')
def get_women(w_id: int):
    person = [p for p in women if p['id'] == w_id]
    return person[0] if len(person) > 0 else {}
''' http://127.0.0.1:8000/person/1 '''

@app.post('/add', status_code=201)
def add_person(person: Women):
    w_id = max([p['id'] for p in women]) + 1
    new_person = {
        "id": w_id,
        "name": person.name,
        "field": person.field,
        "biography": person.biography
    }

    women.append(new_person)

    with open('women.json', 'w') as f:
        json.dump(women, f)
    return new_person

@app.put('/change', status_code=204)
def change_person(person: Women):
    new_person = {
        "id": person.id,
        "name": person.name,
        "field": person.field,
        "biography": person.biography
    }

    person_list = [p for p in women if p['id'] == person.id]
    if len(person_list) > 0:
        women.remove(person_list[0])
        women.append(new_person)
        with open('women.json', 'w') as f:
            json.dump(women, f)
        return new_person
    else:
        return HTTPException(status_code=404, detail=f"Personne avec id {person.id} n'existe pas")

@app.delete('/suppr/{w_id}', status_code=204)
def delete_person(w_id: int):
    person = [p for p in women if p['id'] == w_id]
    if len(person) > 0:
        women.remove(person[0])
        with open('women.json', 'w') as f:
            json.dump(women, f)
    else:
        raise HTTPException(status_code=404, detail=f"Il n'y a aucune personne avec l'id {w_id}")