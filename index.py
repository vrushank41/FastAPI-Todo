from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


from routes.note import note

from config.db import conn
from schemas.note import noteEntity,notesEntity 

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(note)