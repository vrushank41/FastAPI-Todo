from fastapi import APIRouter
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from models.note import Note
from fastapi.templating import Jinja2Templates
from config.db import conn
from schemas.note import noteEntity,notesEntity 
from fastapi.responses import RedirectResponse

note=APIRouter()

templates = Jinja2Templates(directory="templates")


@note.get("/",response_class=HTMLResponse)
async def read_item(request: Request):
    doc=conn.notes.notes
    data=doc.find({})
    # print(data)
    newDoc=[]
    for dat in data:
        newDoc.append({
            "id":dat["_id"],
            "title":dat["title"],
            "description":dat["description"],
            "status":dat["status"]
        })
    return templates.TemplateResponse("index.html", {"request": request,"newDoc":newDoc})

@note.post("/")
async def add_note(request: Request):
    form=await request.form()
    # print(form)
    formData=dict(form)
    if len(formData)==2:
        formData["status"]=False
    print(formData)
    formData["status"]=True if formData["status"]=="on" else False
    conn.notes.notes.insert_one(formData)
    return RedirectResponse(url="http://127.0.0.1:8000", status_code=200)