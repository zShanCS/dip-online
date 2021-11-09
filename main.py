from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import random

from starlette.requests import Request
app = FastAPI()


async def get_neighbors(limit: int):
    list = []
    for i in range(limit):
        list.append(random.randint(0, 10000))
    return list

templates = Jinja2Templates(directory='templates')


@app.post("/uploadfiles/", response_class=HTMLResponse)
async def create_upload_files(request: Request, resultLimit: int = Form(...), file: UploadFile = File(...)):
    res = await get_neighbors(resultLimit)
    print(res)
    return templates.TemplateResponse('first.html',
                                      {"request": request,
                                       "list": res,
                                       "limit": resultLimit}
                                      )


app.mount('/', StaticFiles(directory='static', html=True), name='static')
