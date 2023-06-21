from fastapi import FastAPI
from typing import Optional
app=FastAPI()
# decorate is needed otherwise path will not be specifies
@app.get('/blog')


def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {
        'data':f'{limit} published blogs from the database '
        }
    else :
        return {
            'data':f'{limit} blogs from the database '
        }

# suppose i want to create a page for about so i create another function about
# everytime a page is made you need to add @app.get
# now for about page add app.get(/about) for info add app.get(/info)

# similare to express js dynamic routing where we use /:id here we use paranthesis {id}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished' }

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id }



@app.get('/blog/{id}/comments')
def comments(id,limit=10):
    return limit
    return {'data':{'1','hellu'}}