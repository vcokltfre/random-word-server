from fastapi import FastAPI

from src.models import RandomWordData
from src.randword import WordGenerator
import src.preinit # Not actually unused, makes sure word list is downloaded.

app = FastAPI(docs_url=None)
rwd = WordGenerator()

@app.get("/")
async def get_index():
    return {"status":"ok"}

@app.get("/random")
async def get_random(data: RandomWordData):
    return rwd.generate(data)