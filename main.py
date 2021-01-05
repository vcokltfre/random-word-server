from fastapi import FastAPI

import src.preinit # Not actually unused, makes sure word list is downloaded.

app = FastAPI(docs_url=None)

@app.get("/")
async def get_index():
    return {"status":"ok"}