from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': 'hello world'}


@app.get('/about')
def about():
    return {'data': 'i am about'}


@app.get('/list')
# query has limit in it e.g. domain.com/list?limit=10
def get_list(limit: int = 10, published: bool = True):
    if published:
        return {
            'data': f'{limit} list items but published only'
        }
    else:
        return {
            'data': f'{limit} list items only (not published excluded)'
        }
