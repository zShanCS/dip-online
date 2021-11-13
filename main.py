from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
import random

from starlette.requests import Request
app = FastAPI()


async def get_neighbors(limit: int, file: File):
    list = []
    for i in range(limit):
        list.append(random.randint(0, 10000))
    return list


@app.post("/uploadFile")
async def create_upload_files(request: Request, resultLimit: int = Form(...), file: UploadFile = File(...)):
    res = await get_neighbors(resultLimit, file.file)
    return res


app.mount('/', StaticFiles(directory='static', html=True), name='static')
