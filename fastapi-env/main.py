from fastapi import FastAPI

app=FastAPI()
# decorate is needed otherwise path will not be specifies
@app.get('/')


def index():
    return {
        'data':'soumu'
    }


# suppose i want to create a page for about so i create another function about
# everytime a page is made you need to add @app.get
# now for about page add app.get(/about) for info add app.get(/info)
@app.get('/about')
def about():
    return {'data':{'Nirbhay god'}}